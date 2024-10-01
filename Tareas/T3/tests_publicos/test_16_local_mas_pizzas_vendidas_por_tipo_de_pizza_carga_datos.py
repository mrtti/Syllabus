import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_16 import *
from utilidades import N_SECOND

from consultas import cargar_contenido_pedidos, cargar_pedidos, cargar_locales, \
    local_mas_pizzas_vendidas_por_tipo_de_pizza



class TestLocalMasPizzasVendidasPorTipoDePizzaCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "locales.csv")
        generador_locales = cargar_locales(path)

        resultado_estudiante = local_mas_pizzas_vendidas_por_tipo_de_pizza(
            generador_contenido_pedidos,
            generador_pedidos,
            generador_locales,
            "Pepperoni Clásica",
        )

        resultado_esperado = LOCAL_MAS_PIZZAS_VENDIDAS_POR_TIPO_DE_PIZZA_S_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "locales.csv")
        generador_locales = cargar_locales(path)

        resultado_estudiante = local_mas_pizzas_vendidas_por_tipo_de_pizza(
            generador_contenido_pedidos,
            generador_pedidos,
            generador_locales,
            "Tocino BBQ",
        )

        resultado_esperado = LOCAL_MAS_PIZZAS_VENDIDAS_POR_TIPO_DE_PIZZA_S_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "locales.csv")
        generador_locales = cargar_locales(path)

        resultado_estudiante = local_mas_pizzas_vendidas_por_tipo_de_pizza(
            generador_contenido_pedidos,
            generador_pedidos,
            generador_locales,
            "Encantador Fresquito Tierno con Sazón",
        )

        resultado_esperado = LOCAL_MAS_PIZZAS_VENDIDAS_POR_TIPO_DE_PIZZA_M_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "locales.csv")
        generador_locales = cargar_locales(path)

        resultado_estudiante = local_mas_pizzas_vendidas_por_tipo_de_pizza(
            generador_contenido_pedidos,
            generador_pedidos,
            generador_locales,
            "Radiante Asombroso Cálido con Genialidad",
        )

        resultado_esperado = LOCAL_MAS_PIZZAS_VENDIDAS_POR_TIPO_DE_PIZZA_M_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "locales.csv")
        generador_locales = cargar_locales(path)

        resultado_estudiante = local_mas_pizzas_vendidas_por_tipo_de_pizza(
            generador_contenido_pedidos,
            generador_pedidos,
            generador_locales,
            "Encantador Sabroso Tradicional con Esmero",
        )

        resultado_esperado = LOCAL_MAS_PIZZAS_VENDIDAS_POR_TIPO_DE_PIZZA_M_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)
