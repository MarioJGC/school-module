from odoo import models,fields,api

class SchoolStudent(models.Model):

    _name = 'school.student'
    _description = 'Estudiantes de escuela'

    name = fields.Char(string="Nombre de estudiante", required=True)
    birth_date = fields.Date(string="Fecha de nacimiento")
    age = fields.Integer(string="Edad", compute="_compute_age", store=True)
    final_exam_grade = fields.Float(string="Nota de examen final")
    subject_ids = fields.Many2many('school.subject',string="Cursos")

    # Calculando edad
    @api.depends('birth_date')
    def _compute_age(self):
        for student in self:
            if student.birth_date:
                today = date.today()
                student.age = today.year - student.birth_date.year - ((today.month, today.day) < (student.birth_date.month, student.birth_date.day))
        