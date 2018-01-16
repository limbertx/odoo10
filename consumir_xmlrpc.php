<?php
// These examples use the Ripcord library, which provides a simple XML-RPC API.
// Ripcord requires that XML-RPC support be enabled in your PHP installation.
// Since calls are performed over HTTPS, 
// it also requires that the OpenSSL extension be enabled
###############################################################################

# esto se cambio para el desarrollo

###########################################################################
/*

    composer require odom/ripcord=dev-master
    https://github.com/odom/ripcord

*/

require_once(base_path() . '\vendor\odom\ripcord\ripcord.php');

class xmlrpcclient{
    public $url = "http://186.121.252.150:8069";
    public $db = "dbprueba";

    #public $url = "http://localhost:8069";
    #public $db = "dbempresa1";
    
    public $username = "admin";
    public $password = "admin";
    
    public function __construct(){
    
    }

    public function autenticacion(){
        // metodo para obtener informacion del servidor
        $common = ripcord::client($this->url . "/xmlrpc/2/common");
        print_r($common->version());
        // metodo para autenticar y devuelve un identificador de usuario uid
        $uid = $common->authenticate($this->db, $this->username, $this->password, array());
        echo "uid : " . $uid;
        return $uid;
    }
    # Funciona
    public function guardarTransaccion(){
            $uid = $this->autenticacion();
            $models = ripcord::client($this->url . "/xmlrpc/2/object");
            # devuelve el id de la transaccion
            $res = $models->execute_kw(
                                $this->db, 
                                $uid, 
                                $this->password,
                                'report_custom.transaccionsorteo', # modelo
                                'createtransaccion',
                                array(
                                        "2000-01-01", # fecha de cierre
                                        "1000", # venta efectiva
                                        "0.2", # comision
                                        "1", # id del juego 
                                        "SUPER 10", # nombre del juego
                                        "1", # id del sorteo
                                        "SORTEO NRO. 66", # nombre del sorteo
                                        "JUAN", # nombre de director departamental
                                        "2017-01-01", # fecha de sorteo
                                        "MONTO DE 1000 BS", # glosa del detalle
                                        "PAGO DE SORTEO 78",  # concepto
                                        "BOLIVIA", # pais
                                        "SANTA CRUZ" # departamento
                                )
                    );
            echo "<br/>";
            echo "id de transaccion : " . $res . "<br/>";
            print_r($res);
    }
}

$obj = new xmlrpcclient();
$obj->guardarTransaccion();
