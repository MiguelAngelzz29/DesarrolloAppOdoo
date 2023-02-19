# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class GarantiaCategoria(models.Model):
    _name = 'garantia.categoria'
    _description = 'Categoría Garantías'

    

    descripcion = fields.Char('Descripcion', required=True)
    fecha_inicio = fields.Date('Fecha Inicio')
    fecha_fin = fields.Date('Fecha Fin')


    _parent_store = True
    _parent_name = "parent_id"  # optional if field is 'parent_id'

    name = fields.Char('Category')
    parent_id = fields.Many2one(
        'garantia.categoria',
        string='Categoría Padre',
        ondelete='restrict',
        index=True
    )
    child_ids = fields.One2many(
        'garantia.categoria', 'parent_id',
        string='Categorías Hijas')
    parent_path = fields.Char(index=True)

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('Error! You cannot create recursive categories.')