# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp.osv import fields, osv

class consultas(osv.osv):
	# declaramos el nombre empezando con un prefijo
	_name = 'sis.consultas'
	# Por donde se va a buscar
	_rec_name='nombre'
	_columns = {
	   'nombre' : fields.char('Nombre', size=80, required=True, help='Aqui pones el nombre'),
	   'partner_id': fields.many2one('res.partner', 'Paciente', ondelete='restrict'),
	   'especialidades': fields.many2one('sis.especialidades', 'Especialidad', ondelete='restrict'),	   
	}

consultas();
