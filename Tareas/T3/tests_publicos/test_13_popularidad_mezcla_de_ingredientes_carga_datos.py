import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_13 import *
from utilidades import N_SECOND

from consultas import cargar_contenido_pedidos, cargar_pizzas, popularidad_mezcla_de_ingredientes



class TestPopularidadMezclaDeIngredientesCargaDatos(unittest.TestCase):

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

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = popularidad_mezcla_de_ingredientes(
            generador_pizzas, generador_contenido_pedidos, {"queso"}
        )

        resultado_esperado = POPULARIDAD_MEZCLA_DE_INGREDIENTES_S_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data", carpeta, "pizzas.csv")
        generador_pizzas = cargar_pizzas(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = popularidad_mezcla_de_ingredientes(
            generador_pizzas,
            generador_contenido_pedidos,
            {"tocino", "pepperoni", "aceitunas negras"},
        )

        resultado_esperado = POPULARIDAD_MEZCLA_DE_INGREDIENTES_S_2

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "pizzas.csv")
        generador_pizzas = cargar_pizzas(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = popularidad_mezcla_de_ingredientes(
            generador_pizzas,
            generador_contenido_pedidos,
            {"tocino", "pepperoni", "camarones", "anchoas"},
        )

        resultado_esperado = POPULARIDAD_MEZCLA_DE_INGREDIENTES_M_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "pizzas.csv")
        generador_pizzas = cargar_pizzas(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = popularidad_mezcla_de_ingredientes(
            generador_pizzas, generador_contenido_pedidos, {"queso azul"}
        )

        resultado_esperado = POPULARIDAD_MEZCLA_DE_INGREDIENTES_M_2

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "pizzas.csv")
        generador_pizzas = cargar_pizzas(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = popularidad_mezcla_de_ingredientes(
            generador_pizzas, generador_contenido_pedidos, {
                "tocino", "champiñones"}
        )

        resultado_esperado = POPULARIDAD_MEZCLA_DE_INGREDIENTES_M_3

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pizzas.csv")
        generador_pizzas = cargar_pizzas(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = popularidad_mezcla_de_ingredientes(
            generador_pizzas,
            generador_contenido_pedidos,
            {"pimiento", "huevo", "champiñones"},
        )

        resultado_esperado = POPULARIDAD_MEZCLA_DE_INGREDIENTES_L_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pizzas.csv")
        generador_pizzas = cargar_pizzas(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = popularidad_mezcla_de_ingredientes(
            generador_pizzas, generador_contenido_pedidos, {"carne molida"}
        )

        resultado_esperado = POPULARIDAD_MEZCLA_DE_INGREDIENTES_L_2

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pizzas.csv")
        generador_pizzas = cargar_pizzas(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = popularidad_mezcla_de_ingredientes(
            generador_pizzas, generador_contenido_pedidos, {
                "anchoas", "salsa blanca"}
        )

        resultado_esperado = POPULARIDAD_MEZCLA_DE_INGREDIENTES_L_3

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pizzas.csv")
        generador_pizzas = cargar_pizzas(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = popularidad_mezcla_de_ingredientes(
            generador_pizzas,
            generador_contenido_pedidos,
            {"Pulmones Fritos", "salsa de pimentón"},
        )

        resultado_esperado = POPULARIDAD_MEZCLA_DE_INGREDIENTES_L_4

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)
