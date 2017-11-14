# -*- coding: utf-8 -*-

from odoo import api, fields, models
import json
import logging
from Constantes.ResponseJson import ResponseJson
from Constantes.Constantes import Constantes

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
    def update_sistema_trabajo(self, sistema_trabajos_json):
        """
        Metodo que actualiza y/o adiciona un sistema de trabajo en la contabilidad

        Parametros:

        sistema_trabajos_json --- Es una cadena en formato json 
                                  donde vienen los sistemas de trabajo
        """
        json_acceptable_string = sistema_trabajos_json.replace("'", "\"")
        detail_json = json.loads(json_acceptable_string)

        uid = -1
        for key, value in detail_json.items():
            uid = self._insert_sistema(key, value)
            _logger.info(':CONT_ODOO: key : ' + key + "> <value : " + value)
        
        respuesta = None;

        if(uid <= 0):
            message = "No se pudo guardar sistema de trabajo (verifique en sist. contable SISTEMA DE TRABAJO)"
            respuesta = ResponseJson(Constantes.ERROR_FAIL, message, "ERROR", {})
        else:
            message = "Sistema de trabajo guardado correctamente"
            respuesta = ResponseJson(Constantes.ERROR_OK, message, "OK", {"last_id_sistema_trabajo" : str(uid)})

        return json.dumps(respuesta.__dict__)

    def _insert_sistema(self, sistema_trabajo, descripcion):
        """
        Metodo que inserta y/o actualiza una sistema de trabajo en la base de datos

        Parametros

        sistema_trabajo --- Es el codigo del sistema de trabajo que llega del sist. web comercial
        descripcion --- Es la descripcion del sistema de trabajo enviado por el sistema web comercial        

        """
        env_sistem = self.env["report_custom.sistematrabajo"]

        res_sistema = env_sistem.search([("sistema_trabajo", "=", sistema_trabajo)])    	


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

        if(len(res_sistema) <= 0 ):
            return -1
        else:
            return res_sistema.id