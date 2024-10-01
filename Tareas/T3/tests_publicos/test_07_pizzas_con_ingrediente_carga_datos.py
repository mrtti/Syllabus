import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_07 import *
from utilidades import N_SECOND

from consultas import cargar_pizzas, pizzas_con_ingrediente



class TestPizzaConIngredianteCargaDatos(unittest.TestCase):

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
        g_a = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_a, "tocino")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_S_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data", carpeta, "pizzas.csv")
        g_a = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_a, "pepperoni")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_S_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "pizzas.csv")
        g_a = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_a, "aceitunas negras")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_M_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "pizzas.csv")
        g_a = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_a, "Salsa de Queso")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_M_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "pizzas.csv")
        g_a = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_a, "Palta")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_M_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pizzas.csv")
        g_a = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_a, "champiñones")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_L_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pizzas.csv")
        g_a = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_a, "salsa de queso")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_L_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pizzas.csv")
        g_a = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_a, "Cerebro con Queso")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_L_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pizzas.csv")
        g_a = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_a, "Larvas Crujientes")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_L_4

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_9(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño XL.
        """
        carpeta = "xl"

        path = os.path.join("data", carpeta, "pizzas.csv")
        g_a = cargar_pizzas(path)

        resultado_estudiante = pizzas_con_ingrediente(g_a, "Cerebro con Queso")

        resultado_esperado = PIZZAS_CON_INGREDIENTE_XL_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)
