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

    def test_media_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_media([1, 2, "a", 3])

    def test_desviacion_lista_vacia(self):
        with self.assertRaises(NoSePuedeCalcular):
            calcular_desviacion_estandar([])

    def test_desviacion_un_elemento(self):
        self.assertEqual(calcular_desviacion_estandar([5]), 0.0)

    def test_desviacion_dos_elementos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([5, 15]), 5.0)

    def test_desviacion_varios_elementos_positivos(self):
        self.assertAlmostEqual(calcular_desviacion_estandar([1, 2, 3, 4, 5]), 1.414213562)

    def test_desviacion_varios_elementos_ceros(self):
        self.assertEqual(calcular_desviacion_estandar([0, 0, 0, 0]), 0.0)