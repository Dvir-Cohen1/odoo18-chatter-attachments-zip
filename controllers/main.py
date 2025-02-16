import base64
import io
import zipfile
import logging
from odoo import http
from odoo.http import request
import urllib.parse


_logger = logging.getLogger(__name__)

class AttachmentController(http.Controller):
    @http.route('/download/attachments/zip/<int:task_id>', website=True, page=True,
                auth='public', csrf=False)
    def download_attachments_zip(self, task_id, **kwargs):
        task = request.env['project.task'].browse(task_id)

        if not task.exists():
            _logger.warning(f"Task ID {task_id} does not exist.")
            return {'error': 'Task not found.'}

        attachments = task.attachment_ids
        if not attachments:
            _logger.warning(f"No attachments found for task ID {task_id}.")
            # Return a JSON response to indicate the error
            return request.make_response('{"error": "No attachments found for this task."}', 
                headers=[('Content-Type', 'application/json')])

        try:
            # Generate the filename based on task name and partner name
            task_name = task.name.replace(' ', '_') if task.name else f'task_{task_id}'
            partner_name = getattr(task.partner_id, 'name', '').replace(' ', '_') if task.partner_id else ''
            zip_filename = f"{task_name}_{partner_name}"

            # Encode the filename in UTF-8 and then URL-encode it
            zip_filename_utf8 = zip_filename.encode('utf-8')
            zip_filename_encoded = urllib.parse.quote(zip_filename_utf8)
            
            zip_data = io.BytesIO()
            with zipfile.ZipFile(zip_data, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for attachment in attachments:
                    attachment_data = base64.b64decode(attachment.datas)
                    zipf.writestr(attachment.name, attachment_data)

            response = request.make_response(
                zip_data.getvalue(),
                headers=[
                    ('Content-Type', 'application/zip'),
                    ('Content-Disposition', f'attachment; filename*=UTF-8\'\'{zip_filename_encoded}'),
                ]
            )
            zip_data.close()
            return response

        except Exception as e:
            _logger.error(f"Error generating ZIP for task ID {task_id}: {str(e)}")
            return request.make_response('{"error": "An error occurred while generating the ZIP file."}', 
                headers=[('Content-Type', 'application/json')])
