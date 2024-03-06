{
    "name": "Link Pickings on Invoice / Bill",
    "summary": "Link Pickings on Invoice / Bill",
    "description" : """
        Link Pickings on Invoice / Bill by Adding Pickings on Invoice / Bill 
        and Calculate the Invoice / Bill Details by Picking Information
    """,
    "version": "17.0.1.0.0",
    "category": "Accounting/Pickings",
    "author": "Nur Kholid",
    "maintainers": ["nrkholid"],
    "website": "https://github.com/nrkholid",
    "license": "OPL-1",
    "depends": ["base", "purchase", "sale", "stock", "account"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/account_add_picking_wizard_view.xml",
        "views/sale_inherit_view.xml",
        "views/purchase_inherit_view.xml",
        "views/stock_inherit_view.xml",
        "views/account_move_inherit_view.xml",
    ],
    "auto_install": False,
    "installable": True,
    "application": False,
    "external_dependencies": {"python": []},
}
