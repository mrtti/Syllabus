import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_15 import *
from utilidades import N_SECOND

from consultas import cargar_contenido_pedidos, cargar_pedidos, pizza_favorita_cliente



class TestPizzaFavoritaClienteCargaDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_favorita_cliente(
            generador_pedidos, generador_contenido_pedidos, 13
        )

        resultado_esperado = PIZZA_FAVORITA_CLIENTE_S_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_favorita_cliente(
            generador_pedidos, generador_contenido_pedidos, 14
        )

        resultado_esperado = PIZZA_FAVORITA_CLIENTE_S_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_favorita_cliente(
            generador_pedidos, generador_contenido_pedidos, 135
        )

        resultado_esperado = PIZZA_FAVORITA_CLIENTE_M_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_favorita_cliente(
            generador_pedidos, generador_contenido_pedidos, 120
        )

        resultado_esperado = PIZZA_FAVORITA_CLIENTE_M_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_favorita_cliente(
            generador_pedidos, generador_contenido_pedidos, 111
        )

        resultado_esperado = PIZZA_FAVORITA_CLIENTE_M_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_favorita_cliente(
            generador_pedidos, generador_contenido_pedidos, 1335
        )

        resultado_esperado = PIZZA_FAVORITA_CLIENTE_L_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_favorita_cliente(
            generador_pedidos, generador_contenido_pedidos, 1200
        )

        resultado_esperado = PIZZA_FAVORITA_CLIENTE_L_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_favorita_cliente(
            generador_pedidos, generador_contenido_pedidos, 1111
        )

        resultado_esperado = PIZZA_FAVORITA_CLIENTE_L_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = pizza_favorita_cliente(
            generador_pedidos, generador_contenido_pedidos, 1337
        )

        resultado_esperado = PIZZA_FAVORITA_CLIENTE_L_4

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)
