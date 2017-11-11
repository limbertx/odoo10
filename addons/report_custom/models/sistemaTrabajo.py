# -*- coding: utf-8 -*-

from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)
"""
	Clase encargada de sistemas de trabajo del sistema web comercial
"""
class SistemaTrabajo(models.Model):
    _name = 'report_custom.sistematrabajo'
    _description = "Sistema de trabajo"
    _rec_name = 'descripcion'

    sistema_trabajo = fields.Char(string="Sistema trabajo (web-comercial)", required= True)
    descripcion = fields.Char(string = "Descripcion del sistema de trabajo", required= True)
    account_id = fields.Many2one('account.account', string="Cuenta Contable", required = False)
    account_against_id = fields.Many2one('account.account', string="Contra Cuenta", required = False)
    
    @api.model
    def update_sistema_trabajo(self, sistema_trabajo, descripcion):
    	env_sistem = self.env["report_custom.sistematrabajo"]

    	_logger.info(':CONT_ODOO: sistema_trabajo' + sistema_trabajo)
    	# necesito actualizar
    	res_sistema = env_sistem.search([("sistema_trabajo", "=", sistema_trabajo)])
    	_logger.info(':CONT_ODOO: pase sistema encontrado : ' + str(len(res_sistema)))


    	if(len(res_sistema)>0):
    		res_sistema.write({
    			"sistema_trabajo": sistema_trabajo,
    			"descripcion": descripcion,
                "account_id": False,
                "account_against_id": False,
    			})
    	else:
    		res_sistema = env_sistem.create({
    			"sistema_trabajo": sistema_trabajo,
    			"descripcion": descripcion,
                "account_id": False,
                "account_against_id": False,
    			})

    	return (str(res_sistema.id))