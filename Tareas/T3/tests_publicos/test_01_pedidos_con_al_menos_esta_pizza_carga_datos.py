import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from tests_publicos.solution.test_01 import *
from utilidades import N_SECOND

from consultas import cargar_contenido_pedidos, pedidos_con_al_menos_esta_pizza



class TestPedidoConAlMenosEstaPizzaCargaDeDatos(unittest.TestCase):

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

        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(g_pe, "Hawaiiana")

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_S_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño S.
        """
        carpeta = "s"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")

        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Pepperoni Clásica"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_S_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Asombroso Salado Sabroso con Cariño"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_M_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Fino Salado Increíble con Cautela"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_M_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño M.
        """
        carpeta = "m"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Perfecto Sabroso Perfecto con Estilo"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_M_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_5(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Jugoso Suave Sublime con Arte"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_L_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_6(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Dorado Delicioso Suave con Cariño"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_L_2

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_7(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Tentador Vibrante Picante con Tradición"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_L_3

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_8(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño L.
        """
        carpeta = "l"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Vibrante Sabroso Cremoso con Toque Divino"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_L_4

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_9(self):
        """
        Verifica que se retorne lo pedido con instancias de tamaño XL.
        """
        carpeta = "xl"

        path = os.path.join("data", carpeta, "contenido_pedidos.csv")
        g_pe = cargar_contenido_pedidos(path)

        resultado_estudiante = pedidos_con_al_menos_esta_pizza(
            g_pe, "Tierno Magnífico Radiante con Alegría"
        )

        resultado_esperado = PEDIDOS_CON_AL_MENOS_ESTA_PIZZA_XL_1

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertCountEqual(list(resultado_estudiante), resultado_esperado)
