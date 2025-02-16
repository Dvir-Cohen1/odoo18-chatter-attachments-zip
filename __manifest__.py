# __manifest__.py
{
    'name': 'Chatter Attachments ZIP',
    "version": "1.0.2",
    'category': "Extra Tools",
    'description': 'Adds a button to download task attachments as a ZIP file.',
    'summary': 'Download chatter attachments as zip',
    'author': 'Dvir Cohen',
    'website': 'https://github.com/Dvir-Cohen1',
    'depends': ['mail'],
    "assets": {
        'web.assets_backend': [
            'odoo18-chatter-attachments-zip/static/src/js/attachment_download_button.js',
            'odoo18-chatter-attachments-zip/static/src/xml/chatter.xml',
        ],
    },
    "license": "AGPL-3",
    'installable': True,
    'auto_install': False,
    'application': False,
}
