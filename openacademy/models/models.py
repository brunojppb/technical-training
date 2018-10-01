# -*- coding: utf-8 -*-
from odoo import api, models, fields

class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'
    #attributes
    name = fields.Char(string="Course name") # No definition for varchar limit?
    description = fields.Text(string="Course description")
    maester_id = fields.Many2one('res.partner')
    
    #relations


class CourseSession(models.Model):
    _name = 'openacademy.course_session'
    _description = 'Course Session'
    
    # attributes
    name = fields.Char(compute='_compute_name')
    start_date = fields.Datetime(string="Session start date")
    end_date = fields.Datetime(string="Session end date")
    is_preparation = fields.Boolean(default=False, string="Is a preparation session?")
    is_archived = fields.Boolean(default=False, string="Is archived")

    # Relations
    course_id = fields.Many2one('openacademy.course', required=True, ondelete='cascade')
    attendees = fields.Many2many(comodel_name='openacademy.attendee',
                                 relation='course_session_attendee',
                                 column1='course_session_id', 
                                 column2='attendee_id', 
                                 string='Attendees')
    
    def _compute_name(self):
        for record in self:
            record.name = "{0} - Start date: {1} - End date: {2}".format(record.course_id.name, 
                                                                         record.start_date.strftime('%d, %b %Y'), 
                                                                         record.end_date.strftime('%d, %b %Y'))
        
        

    
class Attendee(models.Model):
    _name = 'openacademy.attendee'
    _description = 'Attendee'
    name = fields.Char('Attendee name')
    