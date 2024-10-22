import unittest
from src.logica.calculos import calcular_media, calcular_desviacion_estandar, NoSePuedeCalcular

class TestCalculos(unittest.TestCase):

    def test_media_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_media([])

    def test_media_un_elemento(self):
        self.assertEqual(calcular_media([5]), 5)

    def test_media_dos_elementos(self):
        self.assertEqual(calcular_media([5, 15]), 10)

    def test_media_varios_elementos_positivos(self):
        self.assertEqual(calcular_media([1, 2, 3, 4, 5]), 3)

    def test_media_varios_elementos_ceros(self):
        self.assertEqual(calcular_media([0, 0, 0, 0]), 0)

    def test_media_elementos_positivos_y_negativos(self):
        self.assertEqual(calcular_media([-3, -1, 1, 3]), 0)