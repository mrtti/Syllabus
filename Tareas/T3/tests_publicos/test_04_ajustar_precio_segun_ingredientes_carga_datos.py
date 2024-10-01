import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_04 import *
from utilidades import N_SECOND

from consultas import cargar_pizzas, ajustar_precio_segun_ingredientes



class TestAjustarPrecioSegunIngredientesCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "tocino", 10000
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_S_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "pepperoni", 100
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_S_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "aceitunas negras", 0
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_M_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "Salsa de Queso", 100
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_M_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "Palta", 100
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_M_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "champiñones", 100
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_L_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "salsa de queso", 100
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_L_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "Cerebro con Queso", 100
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_L_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "Larvas Crujientes", 100
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_L_4

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_9(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño XL.
        """
        carpeta = "xl"

        path = os.path.join("data", carpeta, "pizzas.csv")

        generador_pizzas = cargar_pizzas(path)

        resultado_estudiante = ajustar_precio_segun_ingredientes(
            generador_pizzas, "Cerebro con Queso", 100
        )

        resultado_esperado = AJUSTAR_PRECIO_SEGUN_INGREDIENTES_XL_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)
