import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_06 import *
from utilidades import N_SECOND

from consultas import cargar_pizzas, cliente_indeciso



class TestClienteIndecisoCargaDatos(unittest.TestCase):

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

        resultado_estudiante = cliente_indeciso(
            generador_pizzas, "salsa de ajo", 30)

        resultado_esperado = CLIENTE_INDECISO_S_1

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

        resultado_estudiante = cliente_indeciso(
            generador_pizzas, "choclo", 500)

        resultado_esperado = CLIENTE_INDECISO_S_2

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

        resultado_estudiante = cliente_indeciso(
            generador_pizzas, "tocino", 100)

        resultado_esperado = CLIENTE_INDECISO_M_1

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

        resultado_estudiante = cliente_indeciso(
            generador_pizzas, "aceitunas negras", 100
        )

        resultado_esperado = CLIENTE_INDECISO_M_2

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

        resultado_estudiante = cliente_indeciso(generador_pizzas, "ojo", 250)

        resultado_esperado = CLIENTE_INDECISO_M_3

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

        resultado_estudiante = cliente_indeciso(
            generador_pizzas, "Sangre Coagulada", 60
        )

        resultado_esperado = CLIENTE_INDECISO_L_1

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

        resultado_estudiante = cliente_indeciso(
            generador_pizzas, "Cerebro con Queso", 40
        )

        resultado_esperado = CLIENTE_INDECISO_L_2

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

        resultado_estudiante = cliente_indeciso(generador_pizzas, "pera", 3574)

        resultado_esperado = CLIENTE_INDECISO_L_3

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

        resultado_estudiante = cliente_indeciso(
            generador_pizzas, "El Ingrediente", 4940
        )

        resultado_esperado = CLIENTE_INDECISO_L_4

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

        resultado_estudiante = cliente_indeciso(
            generador_pizzas, "Escamas de Dragón", 432
        )

        resultado_esperado = CLIENTE_INDECISO_XL_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)
