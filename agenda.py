
# -*- coding: utf-8 -*- 
from odoo import models, fields 
class agendamodel(models.Model):
    _name = 'agenda.app'
    _description = 'Gestina una agenda'
    
    _sql_constraints = [('agenda_numero_unico', 'UNIQUE(numero_telefono)', 'Ese número de teléfono ya existe')]

    name = fields.Char('Nombre', required=True)
    apellidos = fields.Char('Apellidos', required=True)
    numero_telefono = fields.Char('Telefono', required=True)
    
    fecha_nacimiento = fields.Date('Fecha nacimiento')
    edad = fields.Integer('Edad')
    direccion = fields.Char('Direccion')
    provincia = fields.Selection([('alicante','Alicante'),('valencia','Valencia'),('castellon','Castellon')])

    correo = fields.Char('Email')
    pagina_web = fields.Char('Página web')

    nota = fields.Text()

    hobbie_ids = fields.Many2many('hobbie.class', 'agenda_hobbie_rel', 'nombre_agenda_id', 'nombre_hobbie_id', string = "Hobbie")
    vehiculos_ids = fields.One2many('vehiculos.class', 'propietario', 'Propietario')

class hobbie(models.Model):
    _name = 'hobbie.class'
	
    _sql_constraints = [('hobbie_nombre_unico', 'UNIQUE(name)', 'Ese hobbie ya existe')]

    name = fields.Char('Nombre', required=True)
    descripcion = fields.Char('Descripción')

class vehiculo(models.Model):
    _name = 'vehiculos.class'
	
    _sql_constraints = [('vehiculo_matricula_unica', 'UNIQUE(name)', 'Ese vehiculo ya existe')]

    name = fields.Char('Matricula', required=True)
    propietario = fields.Many2one('agenda.app', 'Propietario')

