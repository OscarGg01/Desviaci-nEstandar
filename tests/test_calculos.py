import unittest
from src.logica.calculos import calcular_media, calcular_desviacion_estandar, NoSePuedeCalcular

class TestCalculos(unittest.TestCase):

    def test_media_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_media([])
