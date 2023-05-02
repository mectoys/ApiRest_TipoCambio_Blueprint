from scr.database.connectDB import get_connection
from scr.models.entities.Exchange import Exchange


class ExchangeModel:
    # Video 1
    @classmethod
    def list_exchange(self):
        try:
            connection = get_connection()
            exchanges = []

            with connection.cursor() as cursor:
                sql = "SELECT MONEDA, COMPRA, VENTA, FECHA FROM ExchangeRate"
                cursor.execute(sql)
                datos = cursor.fetchall()
                for fila in datos:
                    exchange = Exchange(fila[0], fila[1], fila[2], fila[3])
                    exchanges.append(exchange.convert_to_JSON())
                connection.close()

                return exchanges
        except Exception as ex:
            raise Exception(ex)

    # video 2
    # Método GET: Verificar si existe dato de T.C.
    @classmethod
    def verificar_siexiste(self, fecha):
        connection = get_connection()
        try:
            with connection.cursor() as cursor:
                sql = "SELECT count(ID) as Conteo FROM ExchangeRate WHERE FECHA=CAST('{0}' AS date)".format(fecha)
                print(sql)
                cursor.execute(sql)
                datos = cursor.fetchall()
                if datos != None:
                    exchange = [{'conteo': datos[0]}]
                    print(exchange)
                connection.close()
                return exchange
        except Exception as ex:
            raise Exception(ex)

    # Método GET: Listar último dato T.C.
    @classmethod
    def obtener_lastexchange(self):
        try:
            connection = get_connection()
            exchanges = []

            with connection.cursor() as cursor:
                sql = "SELECT EX.MONEDA, EX.COMPRA, EX.VENTA,EX.FECHA FROM ExchangeRate EX where EX.FECHA \
                               in (SELECT  MAX(EX.FECHA) FROM ExchangeRate EX )"
                cursor.execute(sql)
                datos = cursor.fetchall()
                for fila in datos:
                    exchange = Exchange(fila[0], fila[1], fila[2], fila[3])
                    exchanges.append(exchange.convert_to_JSON())
                connection.close()
                return exchanges
        except Exception as ex:
            raise Exception(ex)

    # Método POST : Agregar T. Cambio.
    @classmethod
    def add_exchange(self, exchange):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql = "INSERT INTO ExchangeRate(MONEDA, COMPRA, VENTA, FECHA) VALUES('{0}',{1},{2},'{3}')".format(
                    exchange.compra, exchange.compra, exchange.venta, exchange.fecha)
                cursor.execute(sql)
                affected_rows = cursor.rowcount
            connection.commit()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
