# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp.osv import fields, osv

class especialidades(osv.osv):
	# declaramos el nombre empezando con un prefijo
	_name = 'sis.especialidades'
	# Por donde se va a buscar
	_rec_name='nombre'
	_columns = {
	   'nombre' : fields.char('Nombre', size=80, required=True, help='Aqui pones el nombre'),
	}

especialidades();
