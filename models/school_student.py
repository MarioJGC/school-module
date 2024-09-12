from odoo import models,fields,api

class SchoolStudent(models.Model):

    _name = 'school.student'
    _description = 'Estudiantes de escuela'

    name = fields.Char(string="Nombre de estudiante", required=True)
    birth_date = fields.Date(string="Fecha de nacimiento")
    age = fields.Integer(string="Año")
    final_exam_grade = fields.Float(string="Nota de examen final")
    subject_ids = fields.Many2many('school.subject',string="Cursos") 