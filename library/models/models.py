# -*- coding: utf-8 -*-
from odoo import api, models, fields
from datetime import datetime

class Book(models.Model):
    _name = 'library.book'
    _description = 'library book'
    # attributes
    name = fields.Char(string="Book name")
    year = fields.Integer(string="Year of edition")
    isbn = fields.Char(string="ISBN")
    
    #relations
    authors = fields.Many2many(comodel_name='library.author',
                                 relation='book_author',
                                 column1='book_id', 
                                 column2='author_id', 
                                 string='Authors')
    editors = fields.Many2many(comodel_name='library.editor',
                                 relation='book_editor',
                                 column1='book_id', 
                                 column2='editor_id', 
                                 string='Editors')
    

class Author(models.Model):
    _name = 'library.author'
    _description = 'Book Author'
    
    #attributes
    name = fields.Char(string="Author name")

class Editor(models.Model):
    _name = 'library.editor'
    _description = 'Book Editor'

    #attributes
    name = fields.Char(string="Editor name")


class Rent(models.Model):
    _name = 'library.rent'
    _description = 'Book Rental'
    name = fields.Char(compute='_compute_name')
    def _compute_name(self):
        for record in self:
            return_date = record.return_date.strftime('%d, %b %Y') if record.return_date else "not returned yet."
            record.name = "{0} - Rent date: {1}. Return date: {2}".format(record.book_id.name, 
                                                                          record.rent_date.strftime('%d, %b %Y'), 
                                                                          return_date)
    
    #attributes
    rent_date = fields.Datetime(string='rent date', default=datetime.now())
    expiration_date = fields.Datetime(string='expiration date')
    return_date = fields.Datetime(string='return date')
    
    # relations
    book_id = fields.Many2one('library.book', required=True, ondelete='cascade')
    customer_id = fields.Many2one('res.partner', required=True)
    
