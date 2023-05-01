from scr.utils.Dateformat import DateFormat


class Exchange:

    def __init__(self, moneda=None, compra=None, venta=None, fecha=None):
        self.moneda = moneda
        self.compra = compra
        self.venta = venta
        self.fecha = fecha

    def convert_to_JSON(self):
        return {
            'moneda': self.moneda,
            'compra': self.compra,
            'venta': self.venta,
            'fecha': DateFormat.convert_date(self.fecha)
        }
