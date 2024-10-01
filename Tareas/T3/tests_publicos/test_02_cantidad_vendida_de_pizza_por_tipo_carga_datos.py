import os
import sys
import unittest

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_02 import *
from utilidades import N_SECOND

from consultas import cargar_contenido_pedidos, cantidad_vendida_de_pizza_por_tipo


class TestCantidadVendidaDePizzaPorTipoCargaDatos(unittest.TestCase):

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

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Hawaiiana"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_S_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")

        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Pepperoni Clásica"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_S_2

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Asombroso Salado Sabroso con Cariño"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_M_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Fino Salado Increíble con Cautela"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_M_2

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Perfecto Sabroso Perfecto con Estilo"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_M_3

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Jugoso Suave Sublime con Arte"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_L_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Dorado Delicioso Suave con Cariño"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_L_2

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Tentador Vibrante Picante con Tradición"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_L_3

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Vibrante Sabroso Cremoso con Toque Divino"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_L_4

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_9(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño XL.
        """
        carpeta = "xl"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        resultado_estudiante = cantidad_vendida_de_pizza_por_tipo(
            generador_contenido_pedidos, "Asombroso Apetitoso Vibrante con Maestría"
        )

        resultado_esperado = CANTIDAD_VENDIDA_DE_PIZZA_POR_TIPO_XL_1

        self.assertIsInstance(resultado_estudiante, (int))

        self.assertEqual((resultado_estudiante), resultado_esperado)
