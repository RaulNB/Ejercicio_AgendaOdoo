# -*- coding: utf-8 -*- 
from odoo import models, fields 
class agendamodel(models.Model):
    _name = 'agenda.app'
    _description = 'Gestina una agenda'
    
    name = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    numero_telefono = fields.Char('Telefono', required=True)
    
    fecha_nacimiento = fields.Date('Fecha nacimiento')
    edad = fields.Integer('Edad')
    direccion = fields.Char('Direccion')
    provincia = fields.Selection([('alicante','Alicante'),('valencia','Valencia'),('castellon','Castellon')])

    correo = fields.Char('Email')
    pagina_web = fields.Char('Página web')

    hobbie_ids = fields.Many2many('clase.hobbie', 'agenda_hobbies_rel', 'contactos_id', 'hobbie_id', string="Hobbie")

class hobbie(models.Model):
	_name = 'clase.hobbie'
	name = fields.Char('Nombre', required=True)
	descripcion = fields.Char('Descripción')