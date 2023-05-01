from scr.database.connectDB import get_connection
from scr.models.entities.Exchange import Exchange


class ExchangeModel:
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
