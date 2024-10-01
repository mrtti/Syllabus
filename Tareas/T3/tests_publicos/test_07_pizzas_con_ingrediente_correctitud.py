import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_07 import *
from utilidades import N_SECOND

from consultas import pizzas_con_ingrediente



class TestPizzasConIngredienteCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que el test funcione si es que el ingrediente no existe en ninguna pizza.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Margarita", ingredientes="tomate;queso;albahaca", precio=5000
            ),
            Pizza(nombre="Napolitana", ingredientes="tomate;queso;jamón", precio=6000),
            Pizza(
                nombre="Hawaiana", ingredientes="tomate;queso;jamón;piña", precio=7000
            ),
            Pizza(
                nombre="Pepperoni", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_con_ingrediente(generador_entregado, "orégano")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = []

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que el test funcione si es que el ingrediente existe en todas las pizzas.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Margarita", ingredientes="tomate;queso;albahaca", precio=5000
            ),
            Pizza(nombre="Napolitana", ingredientes="tomate;queso;jamón", precio=6000),
            Pizza(
                nombre="Hawaiana", ingredientes="tomate;queso;jamón;piña", precio=7000
            ),
            Pizza(
                nombre="Pepperoni", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_con_ingrediente(generador_entregado, "tomate")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Margarita", ingredientes="tomate;queso;albahaca", precio=5000
            ),
            Pizza(nombre="Napolitana", ingredientes="tomate;queso;jamón", precio=6000),
            Pizza(
                nombre="Hawaiana", ingredientes="tomate;queso;jamón;piña", precio=7000
            ),
            Pizza(
                nombre="Pepperoni", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que el test funcione si es que el ingrediente existe en tres pizzas.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Margarita", ingredientes="tomate;queso;albahaca", precio=5000
            ),
            Pizza(nombre="Napolitana", ingredientes="tomate;queso;jamón", precio=6000),
            Pizza(
                nombre="Hawaiana", ingredientes="tomate;queso;jamón;piña", precio=7000
            ),
            Pizza(
                nombre="Pepperoni", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Locura",
                ingredientes="tomate;queso;manjar;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Vegetariana",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
            Pizza(
                nombre="supra-pepperoni",
                ingredientes="tomate;queso;pepperoni;pepperoni-doble",
                precio=9000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_con_ingrediente(generador_entregado, "pepperoni")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Pepperoni", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Locura",
                ingredientes="tomate;queso;manjar;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="supra-pepperoni",
                ingredientes="tomate;queso;pepperoni;pepperoni-doble",
                precio=9000,
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que el test funcione si es que el ingrediente existe en una pizza.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Margarita", ingredientes="tomate;queso;albahaca", precio=5000
            ),
            Pizza(nombre="Napolitana", ingredientes="tomate;queso;jamón", precio=6000),
            Pizza(
                nombre="Hawaiana", ingredientes="tomate;queso;jamón;piña", precio=7000
            ),
            Pizza(
                nombre="Pepperoni", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_con_ingrediente(generador_entregado, "albahaca")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Margarita", ingredientes="tomate;queso;albahaca", precio=5000
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que el test funcione si es que el generador entregado está vacío.
        """

        lista_entregada = []

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_con_ingrediente(generador_entregado, "tomate")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = []

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que el test funcione si es que el generador entregado tiene solo una pizza.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Margarita", ingredientes="tomate;queso;albahaca", precio=5000
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_con_ingrediente(generador_entregado, "tomate")

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Margarita", ingredientes="tomate;queso;albahaca", precio=5000
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)
