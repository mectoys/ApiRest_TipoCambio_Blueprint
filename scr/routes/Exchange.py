from scr.models.ExchangeModel import ExchangeModel
from scr.models.entities.Exchange import Exchange
from flask import Blueprint, jsonify, request

main = Blueprint('exchange_blueprint', __name__)


# Video 1
@main.route('/')
def list_exchange():
    try:
        exchange = ExchangeModel.list_exchange()
        return jsonify(exchange)
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500


# video 2
# Ruta GET: Verificar si existe dato de T.C.
@main.route('/<fecha>')
def verificar_siexiste(fecha):
    try:
        exchange_date = ExchangeModel.verificar_siexiste(fecha)
        print(exchange_date)
        if exchange_date != None:
            return jsonify(exchange_date)
        else:
            return jsonify({}), 404

    except Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500


# Ruta GET: Listar último dato T.C.
@main.route('/lastexchange')
def obtener_lastexchange():
    try:
        exchange = ExchangeModel.obtener_lastexchange()
        print(exchange)
        if exchange != None:
            return jsonify(exchange)
        else:
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500


# Ruta POST : Agregar T. Cambio.

@main.route('/addex', methods=['POST'])
def add_exchange():
    try:
        moneda = request.json['MONEDA']
        compra = request.json['COMPRA']
        venta = request.json['VENTA']
        fecha = request.json['FECHA']

        exchange = Exchange(moneda, compra, venta, fecha)
        affected_rows = ExchangeModel.add_exchange(exchange)

        if affected_rows == 1:
            return jsonify(exchange.fecha)
        else:
            return jsonify({'mensaje': "Error Insert"}), 500

    except  Exception as ex:
        return jsonify({'mensaje': str(ex)}), 500
