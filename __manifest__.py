# __manifest__.py
{
    'name': 'Chatter Attachments ZIP',
    "version": "1.0.2",
    'category': "Productivity",
    'summary': 'Easily download all chatter attachments as a ZIP file with a single click.',
    'description': """
        Chatter Attachments ZIP enhances Odoo's chatter functionality by adding a 
        convenient button in the chatter top bar, allowing users to download all 
        attachments related to a record as a single ZIP file. 

        Key Features:
        - One-click download of all attachments in a chatter thread.
        - Seamless integration with Odoo's mail module.
        - Enhances productivity by reducing manual download effort.
        - Fully compatible with Odoo 18.

        Ideal for teams that frequently share and manage attachments within tasks, projects, and discussions.
    """,
    'author': 'Dvir Cohen',
    'website': 'https://github.com/Dvir-Cohen1',
    'maintainers': ['Dvir Cohen'],
    'support': 'https://github.com/Dvir-Cohen1',
    'depends': ['mail'],
    "assets": {
        'web.assets_backend': [
            'odoo18-chatter-attachments-zip/static/src/js/attachment_download_button.js',
            'odoo18-chatter-attachments-zip/static/src/xml/chatter.xml',
        ],
    },
    'images': ['static/description/banner.png'],
    "license": "AGPL-3",
    'installable': True,
    'auto_install': False,
    'application': False,
}
