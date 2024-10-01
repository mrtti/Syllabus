import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_09 import *
from utilidades import N_SECOND

from consultas import cargar_locales, cantidad_empleados_pais



class TestCantidadEmpleadosPaisCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data", carpeta, "locales.csv")

        generador_locales = cargar_locales(path)

        resultado_estudiante = cantidad_empleados_pais(generador_locales, "Slovenia")

        resultado_esperado = CANTIDAD_EMPLEADOS_PAIS_S_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data", carpeta, "locales.csv")

        generador_locales = cargar_locales(path)

        resultado_estudiante = cantidad_empleados_pais(generador_locales, "Argentina")

        resultado_esperado = CANTIDAD_EMPLEADOS_PAIS_S_2

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "locales.csv")

        generador_locales = cargar_locales(path)

        resultado_estudiante = cantidad_empleados_pais(generador_locales, "Singapore")

        resultado_esperado = CANTIDAD_EMPLEADOS_PAIS_M_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "locales.csv")

        generador_locales = cargar_locales(path)

        resultado_estudiante = cantidad_empleados_pais(
            generador_locales, "Dominican Republic"
        )

        resultado_esperado = CANTIDAD_EMPLEADOS_PAIS_M_2

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "locales.csv")

        generador_locales = cargar_locales(path)

        resultado_estudiante = cantidad_empleados_pais(generador_locales, "Qatar")

        resultado_esperado = CANTIDAD_EMPLEADOS_PAIS_M_3

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "locales.csv")

        generador_locales = cargar_locales(path)

        resultado_estudiante = cantidad_empleados_pais(generador_locales, "Luxembourg")

        resultado_esperado = CANTIDAD_EMPLEADOS_PAIS_L_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "locales.csv")

        generador_locales = cargar_locales(path)

        resultado_estudiante = cantidad_empleados_pais(generador_locales, "Isle of Man")

        resultado_esperado = CANTIDAD_EMPLEADOS_PAIS_L_2

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "locales.csv")

        generador_locales = cargar_locales(path)

        resultado_estudiante = cantidad_empleados_pais(generador_locales, "Hong Kong")

        resultado_esperado = CANTIDAD_EMPLEADOS_PAIS_L_3

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "locales.csv")

        generador_locales = cargar_locales(path)

        resultado_estudiante = cantidad_empleados_pais(generador_locales, "Monaco")

        resultado_esperado = CANTIDAD_EMPLEADOS_PAIS_L_4

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_9(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño XL.
        """
        carpeta = "xl"

        path = os.path.join("data", carpeta, "locales.csv")

        generador_locales = cargar_locales(path)

        resultado_estudiante = cantidad_empleados_pais(generador_locales, "Iran")

        resultado_esperado = CANTIDAD_EMPLEADOS_PAIS_XL_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)
