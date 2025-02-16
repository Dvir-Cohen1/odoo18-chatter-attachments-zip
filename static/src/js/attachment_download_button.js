/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { useService } from "@web/core/utils/hooks";
import { Chatter } from "@mail/chatter/web_portal/chatter";
import { patch } from "@web/core/utils/patch";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(Chatter.prototype, {
  setup() {
    super.setup();
    this.dialog = useService("dialog");
  },

  async onDownloadAttachments(ev) {
    const url = `/download/attachments/zip/${this.props.threadId}`;
    var fileName;
    fetch(url)
      .then((response) => {
        if (response.ok) {
          const contentDisposition = response.headers.get(
            "Content-Disposition"
          );
          if (contentDisposition) {
            const extractedFilename =
              contentDisposition.split("filename*=UTF-8''")[1] ||
              contentDisposition.split("filename=")[1];
            fileName = extractedFilename;
            console.log("Filename from header:", extractedFilename);
          } else {
            fileName = `attachments${this.props.threadId}`;
          }
          return response.blob();
        } else {
          Promise.reject("Failed to fetch");
        }
      })
      .then((blob) => {
        if (blob.size === 0) {
          this.dialog.add(AlertDialog, {
            title: _t("Info"),
            body: _t("לא צורפו קבצים למשימה."),
          });
        } else {
          const blobUrl = URL.createObjectURL(blob);
          const link = document.createElement("a");
          link.href = blobUrl;
          link.download = `${fileName}.zip`;
          link.click();
          URL.revokeObjectURL(blobUrl);
        }
      })
      .catch((error) => {
        console.error("Download failed:", error);
      });
  },
});
