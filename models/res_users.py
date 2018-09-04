from odoo import api, fields, models

# Héritage du model user pour ajouter une liste de marque autoriser
class ResUsers(models.Model):
    _inherit = 'res.users'
    
    marque_ids = fields.Many2many('brand_model.marque', string="Modele autoriser pour l'utilisateur")
