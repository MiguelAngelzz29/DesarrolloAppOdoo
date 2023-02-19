# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _

class Garantia(models.Model):
    _name = 'garantia.garantia'
    _description = 'garantia'

    descripcion = fields.Char('Descripción', required=True)
    fecha_inicio = fields.Date('Fecha Inicio')
    fecha_fin = fields.Date('Fecha Fin')
    productos_ids = fields.Many2many('product.template', string='Productos')
    categoria_id = fields.Many2one('garantia.categoria',string='Categoria')
    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True)
    venta_id = fields.Many2one('sale.order', string='Orden de venta', required=True)
    

    @api.onchange('sale_order_id')
    def onchange_sale_order_id(self):
        if self.sale_order_id:
            self.partner_id = self.sale_order_id.partner_id


    
    state = fields.Selection([
        ('borrador', 'Tramitada'),
        ('EnProceso', 'En Proceso'),
        ('enRevision', 'En Revisión'),
        ('Terminada', 'Terminada')],
        'State', default="borrador")

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('borrador', 'EnProceso'),
                   ('EnProceso', 'enRevision'),
                   ('enRevision', 'EnProceso'),
                   ('EnProceso', 'Terminada'),
                   ('enRevision', 'Terminada'),
                   ('Terminada', 'EnProceso')]
        return (old_state, new_state) in allowed

    def change_state(self, new_state):
        for garantia in self:
            if garantia.is_allowed_transition(garantia.state, new_state):
                garantia.state = new_state
            else:
                message = _('Moving from %s to %s is not allowed') % (garantia.state, new_state)
                raise UserError(message)

    def make_EnProceso(self):
        self.change_state('EnProceso')

    def make_enRevision(self):
        self.change_state('enRevision')

    def make_Terminada(self):
        self.change_state('Terminada')


    def create_categories(self):
        categ1 = {
            'name': 'Child category 1',
            'description': 'Description for child 1'
        }
        categ2 = {
            'name': 'Child category 2',
            'description': 'Description for child 2'
        }
        parent_category_val = {
            'name': 'Parent category',
            'description': 'Description for parent category',
            'child_ids': [
                (0, 0, categ1),
                (0, 0, categ2),
            ]
        }
        
        record = self.env['garantia.categoria'].create(parent_category_val)
        return True


class GarantiaExtendida(Garantia):
    _name = 'garantia.garantia.extendida'
    _description = 'Garantia extendida'

    dias_extra = fields.Integer('Dias extra', required=True)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    garantia_extendida_ids = fields.Many2many('garantia.garantia.extendida', string='Garantías extendidas')