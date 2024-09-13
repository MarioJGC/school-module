from odoo import models,fields,api

class SchoolSubject(models.Model):

    _name = 'school.subject'
    _description = 'Cursos de escuela'

    name = fields.Char(string="Nombre del curso", required=True)
    credits = fields.Integer(string="Creditos del curso")
    max_students = fields.Integer(string="Cantidad maxima de estudiantes")
    activate = fields.Boolean(string="Estado")
    student_ids = fields.Many2many('school.student',string="Estudiantes")
    teacher_id = fields.Many2one('school.teacher',string="Profesores")