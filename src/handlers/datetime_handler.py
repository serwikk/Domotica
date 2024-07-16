import datetime

class DatetimeHandler:

    def __init__(self, fecha_completa = datetime.datetime.now()) -> None:
        self.fecha_completa = fecha_completa
        self.anyo = self.fecha_completa.year
        self.mes = self.fecha_completa.month
        self.dia = self.fecha_completa.day
        self.hora = self.fecha_completa.hour
        self.minuto = self.fecha_completa.minute
        self.segundo = self.fecha_completa.second
        self.microsegundos = self.fecha_completa.microsecond


    def obtener_mes_string(self) -> str:

        meses_dictionario = {
            1: 'enero',
            2: 'febrero',
            3: 'marzo',
            4: 'abril',
            5: 'mayo',
            6: 'junio',
            7: 'julio',
            8: 'agosto',
            9: 'septiembre',
            10: 'octubre',
            11: 'noviembre',
            12: 'diciembre'
        }

        return meses_dictionario[self.mes]