import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_08 import *
from utilidades import N_SECOND

from consultas import cargar_pizzas, pizzas_pagables_de_un_tamano



class TestPizzasPagablesDeUnTamanoCargaDatos(unittest.TestCase):

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

        resultado_estudiante = pizzas_pagables_de_un_tamano(
            generador_pizzas, 18000, "S"
        )

        resultado_esperado = PIZZAS_PAGABLES_DE_UN_TAMANO_S_1

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

        resultado_estudiante = pizzas_pagables_de_un_tamano(
            generador_pizzas, 26000, "L"
        )

        resultado_esperado = PIZZAS_PAGABLES_DE_UN_TAMANO_S_2

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

        resultado_estudiante = pizzas_pagables_de_un_tamano(
            generador_pizzas, 14000, "M"
        )

        resultado_esperado = PIZZAS_PAGABLES_DE_UN_TAMANO_M_1

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

        resultado_estudiante = pizzas_pagables_de_un_tamano(
            generador_pizzas, 17000, "L"
        )

        resultado_esperado = PIZZAS_PAGABLES_DE_UN_TAMANO_M_2

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

        resultado_estudiante = pizzas_pagables_de_un_tamano(
            generador_pizzas, 11000, "S"
        )

        resultado_esperado = PIZZAS_PAGABLES_DE_UN_TAMANO_M_3

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

        resultado_estudiante = pizzas_pagables_de_un_tamano(
            generador_pizzas, 100000, "L"
        )

        resultado_esperado = PIZZAS_PAGABLES_DE_UN_TAMANO_L_1

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

        resultado_estudiante = pizzas_pagables_de_un_tamano(
            generador_pizzas, 120000, "XL"
        )

        resultado_esperado = PIZZAS_PAGABLES_DE_UN_TAMANO_L_2

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

        resultado_estudiante = pizzas_pagables_de_un_tamano(
            generador_pizzas, 8000, "M")

        resultado_esperado = PIZZAS_PAGABLES_DE_UN_TAMANO_L_3

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

        resultado_estudiante = pizzas_pagables_de_un_tamano(
            generador_pizzas, 9000, "S")

        resultado_esperado = PIZZAS_PAGABLES_DE_UN_TAMANO_L_4

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

        resultado_estudiante = pizzas_pagables_de_un_tamano(
            generador_pizzas, 15000, "S"
        )

        resultado_esperado = PIZZAS_PAGABLES_DE_UN_TAMANO_XL_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)
