import base64
import io
import zipfile
import logging
from odoo import http
from odoo.http import request
import json

_logger = logging.getLogger(__name__)

class AttachmentController(http.Controller):
    @http.route('/download/attachments/zip/<string:thread_model>/<int:thread_id>', website=True, page=True, auth='public', csrf=False)
    def download_attachments_zip(self, thread_model, thread_id, **kwargs):
        record = request.env[thread_model].browse(thread_id)

        if not record.exists():
            _logger.warning(f"Record ID {thread_id} does not exist in model {thread_model}.")
            return request.make_response(json.dumps({'error': 'Record not found.'}), 
                                         headers=[('Content-Type', 'application/json')])

        # Use ir.attachment to get attachments related to the record
        attachments = request.env["ir.attachment"].search([
            ("res_model", "=", thread_model),
            ("res_id", "=", thread_id),
        ])

        if not attachments:
            _logger.warning(f"No attachments found for record ID {thread_id}.")
            return request.make_response(json.dumps({'error': 'No attachments found for this record.'}), 
                                         headers=[('Content-Type', 'application/json')])

        try:
            record_name = record.name.replace(' ', '_') if hasattr(record, 'name') and record.name else f"{thread_model}_{thread_id}"
            zip_filename = f"{record_name}.zip"

            zip_data = io.BytesIO()
            with zipfile.ZipFile(zip_data, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for attachment in attachments:
                    if attachment.datas:
                        attachment_data = base64.b64decode(attachment.datas)
                        zipf.writestr(attachment.name, attachment_data)

            zip_data.seek(0)
            zip_base64 = base64.b64encode(zip_data.getvalue()).decode('utf-8')

            return request.make_response(
                json.dumps({"filename": zip_filename, "file": zip_base64}),
                headers=[('Content-Type', 'application/json')]
            )

        except Exception as e:
            _logger.error(f"Error generating ZIP for record ID {thread_id}: {str(e)}")
            return request.make_response(json.dumps({'error': 'An error occurred while generating the ZIP file.'}), 
                                         headers=[('Content-Type', 'application/json')])
