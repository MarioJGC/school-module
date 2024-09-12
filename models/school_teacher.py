from odoo import models,fields,api

class SchoolTeacher(models.Model):

    _name = 'school.teacher'
    _description = 'Profesores de escuela'

    name = fields.Char(string="Nombre de Profesor", required=True)
    profile = fields.Text(string="Perfil")
    subject_ids = fields.One2many('school.subject',string="Cursos")