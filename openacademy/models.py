# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError

class Courses(models.Model):
    _name = 'openacademy.course'

    name = fields.Char()
    user_id = fields.Many2one('res.users', string="Responsible")


class Sessions(models.Model):
    _name = 'openacademy.session'

    course_id = fields.Many2one('openacademy.course', string="Course")
    user_id = fields.Many2one('res.users', string="Instructor")
    start_date = fields.Date()
    seats = fields.Integer('Room Capacity')
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    
    def _get_available_spots(self):
        current = len(self.attendee_ids)
        return self.seats - current
    
    # Constrains validations are triggered 
    # all the time after the model changes
    @api.constrains('attendee_ids')
    def validate_attendees_constrains(self):
        current = len(self.attendee_ids)
        if self._get_available_spots() < 0:
            raise ValidationError("CONSTRAIN")
            
    
    # Onchange validations are only triggered when 
    # changing the model via the user interface
    @api.onchange('attendee_ids')
    def validate_attendees_onchange(self):
        if self._get_available_spots() < 0:
            raise ValidationError("ONCHANGE")
    
    
