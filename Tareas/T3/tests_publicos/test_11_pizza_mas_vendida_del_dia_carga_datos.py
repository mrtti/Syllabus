import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_11 import *
from utilidades import N_SECOND

from consultas import cargar_contenido_pedidos, cargar_pedidos, pizza_mas_vendida_del_dia



class TestPizzaMasVendidaDelDiaCargaDatos(unittest.TestCase):

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

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-03-20"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_S_1

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

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-03-21"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_S_2

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

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-04-20"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_M_1

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

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-04-21"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_M_2

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

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-04-22"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_M_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-05-20"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_L_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-05-21"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_L_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-05-22"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_L_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        generador_contenido_pedidos = cargar_contenido_pedidos(path)

        path = os.path.join("data", carpeta, "pedidos.csv")
        generador_pedidos = cargar_pedidos(path)

        resultado_estudiante = pizza_mas_vendida_del_dia(
            generador_contenido_pedidos, generador_pedidos, "2024-05-23"
        )

        resultado_esperado = PIZZA_MAS_VENDIDA_DEL_DIA_L_4

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)
