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
    const url = `/download/attachments/zip/${this.props.threadModel}/${this.props.threadId}`;

    fetch(url)
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          this.dialog.add(AlertDialog, {
            title: _t("Error"),
            body: _t(data.error),
          });
          return;
        }

        const { filename, file } = data;
        if (!file) {
          this.dialog.add(AlertDialog, {
            title: _t("Info"),
            body: _t("לא צורפו קבצים למשימה."),
          });
          return;
        }

        // Convert base64 to Blob
        const byteCharacters = atob(file);
        const byteNumbers = new Array(byteCharacters.length);
        for (let i = 0; i < byteCharacters.length; i++) {
          byteNumbers[i] = byteCharacters.charCodeAt(i);
        }
        const byteArray = new Uint8Array(byteNumbers);
        const blob = new Blob([byteArray], { type: "application/zip" });

        // Download the file
        const blobUrl = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = blobUrl;
        link.download = filename;
        link.click();
        URL.revokeObjectURL(blobUrl);
        link.remove()
      })
      .catch((error) => {
        console.error("Download failed:", error);
      });
  },
});
