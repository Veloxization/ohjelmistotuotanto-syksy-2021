from kivipaperisakset import KPSPelaajaVsPelaaja, KPSTekoaly, KPSTekoalyParannettu
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu

class Peli:
    @staticmethod
    def luo_kaksinpeli():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def luo_yksinpeli():
        return KPSTekoaly(Tekoaly())

    @staticmethod
    def luo_haastava_yksinpeli():
        return KPSTekoalyParannettu(TekoalyParannettu(10))