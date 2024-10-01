import os
import sys
import unittest
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from utilidades import Pizzas, Locales, ContenidoPedidos, Pedidos
from utilidades import N_SECOND

from consultas import (
    cargar_pizzas,
    cargar_locales,
    cargar_pedidos,
    cargar_contenido_pedidos,
)



class TestCargarDatos(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_l_pizzas(self):
        """
        Verifica que los datos carguen bien con un dataset L de Pizzas.
        """
        path = os.path.join("data", "l", "pizzas.csv")
        generador = cargar_pizzas(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 14973)

        # Revisar posiciones aleatorias
        pizzas_cargadas = [
            generador[0],
            generador[11],
            generador[4444],
            generador[-1],
        ]

        pizzas_esperadas = [
            Pizzas(
                nombre="Alegre Encantador Sensacional con Magia_S",
                ingredientes="Moco de Momia;Salsa Blanca;Corazón Desgarrado;choclo;Larvas Crujientes;salsa de queso",
                precio=8204,
            ),
            Pizzas(
                nombre="Sabroso Glorioso Tentador con Tradición_L",
                ingredientes="pepperoni;palta;Dedos Verdes;salsa de pimienta",
                precio=19125,
            ),
            Pizzas(
                nombre="Fascinante Cálido Sensacional con Cuidado_M",
                ingredientes="salchicha;piña;Sangre Coagulada;salsa de queso",
                precio=12439,
            ),
            Pizzas(
                nombre="Irresistible Picante Cremoso con Estilo_L",
                ingredientes="Baba de Zombie;Dedos de Cadáver;salsa de queso",
                precio=16272,
            ),
        ]

        self.assertCountEqual(pizzas_cargadas, pizzas_esperadas)

    @timeout(N_SECOND)
    def test_xl_pizzas(self):
        """
        Verifica que los datos carguen bien con un dataset XL de Pizzas.
        """
        path = os.path.join("data", "xl", "pizzas.csv")
        generador = cargar_pizzas(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 150000)

        # Revisar posiciones aleatorias
        pizzas_cargadas = [
            generador[0],
            generador[131],
            generador[445],
            generador[-1],
        ]

        pizzas_esperadas = [
            Pizzas(
                nombre="Envolvente Glorioso Delicioso con Cautela_S",
                ingredientes="cebolla;Dedos Verdes;salsa de pimentón",
                precio=9703,
            ),
            Pizzas(
                nombre="Magnífico Perfecto Apetitoso con Pureza_L",
                ingredientes="Cerebro con Queso;Lengua de Vampiro;Tripas Enrolladas;Larvas Crujientes;pimiento;salsa de mostaza",
                precio=17659,
            ),
            Pizzas(
                nombre="Tierno Brillante Estupendo con Perfección_M",
                ingredientes="camarones;queso azul;Piel Marchita;palta;salchicha;salsa blanca",
                precio=10753,
            ),
            Pizzas(
                nombre="Cremoso Glorioso Alegre con Fervor_L",
                ingredientes="Sangre Coagulada;Moco de Momia;jamón;Sesos Picados;Palta;salsa de pimentón",
                precio=15759,
            ),
        ]

        self.assertCountEqual(pizzas_cargadas, pizzas_esperadas)

    @timeout(N_SECOND)
    def test_l_locales(self):
        """
        Verifica que los datos carguen bien con un dataset L de Locales.
        """
        path = os.path.join("data", "l", "locales.csv")
        generador = cargar_locales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 40000)

        # Revisar posiciones aleatorias
        locales_cargados = [
            generador[0],
            generador[140],
            generador[42],
            generador[-1],
        ]

        locales_esperados = [
            Locales(
                id_local=0,
                direccion="3135 Gutierrez Flats 3135",
                pais="Tuvalu",
                ciudad="West Christopher",
                cantidad_trabajadores=17,
            ),
            Locales(
                id_local=140,
                direccion="27786 Joseph Road Apt. 034 27786",
                pais="Norway",
                ciudad="Hernandezview",
                cantidad_trabajadores=15,
            ),
            Locales(
                id_local=42,
                direccion="04513 Scott Parks Suite 143 04513",
                pais="Liberia",
                ciudad="Port Kelly",
                cantidad_trabajadores=10,
            ),
            Locales(
                id_local=39999,
                direccion="USCGC Morris USCGC",
                pais="Iraq",
                ciudad="Holmesstad",
                cantidad_trabajadores=12,
            ),
        ]

        self.assertCountEqual(locales_cargados, locales_esperados)

    @timeout(N_SECOND)
    def test_xl_locales(self):
        """
        Verifica que los datos carguen bien con un dataset XL de Locales.
        """
        path = os.path.join("data", "xl", "locales.csv")
        generador = cargar_locales(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 400000)

        # Revisar posiciones aleatorias
        locales_cargados = [
            generador[0],
            generador[1400],
            generador[4442],
            generador[-1],
        ]

        locales_esperados = [
            Locales(
                id_local=0,
                direccion="8691 Brian Road Suite 259 8691",
                pais="Falkland Islands (Malvinas)",
                ciudad="South Jessehaven",
                cantidad_trabajadores=18,
            ),
            Locales(
                id_local=1400,
                direccion="858 Gonzalez Parkways Apt. 406 858",
                pais="Andorra",
                ciudad="Haynesmouth",
                cantidad_trabajadores=4,
            ),
            Locales(
                id_local=4442,
                direccion="60032 Jason Loaf Apt. 062 60032",
                pais="Seychelles",
                ciudad="Fletcherborough",
                cantidad_trabajadores=12,
            ),
            Locales(
                id_local=399999,
                direccion="775 Barbara Lock 775",
                pais="Taiwan",
                ciudad="South Kellyland",
                cantidad_trabajadores=19,
            ),
        ]

        self.assertCountEqual(locales_cargados, locales_esperados)

    @timeout(N_SECOND)
    def test_l_contenido_pedidos(self):
        """
        Verifica que los datos carguen bien con un dataset L de ContenidoPedidos.
        """
        path = os.path.join("data", "l", "contenido_pedidos.csv")
        generador = cargar_contenido_pedidos(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 174967)

        # Revisar posiciones aleatorias
        contenido_cargado = [
            generador[0],
            generador[104],
            generador[25],
            generador[-1],
        ]

        contenido_esperado = [
            ContenidoPedidos(
                id_pedido=0,
                nombre="Cremoso Fascinante Delicioso con Arte_M",
                cantidad=5,
                descuento=0.0,
            ),
            ContenidoPedidos(
                id_pedido=41,
                nombre="Picante Tentador Perfecto con Arte_M",
                cantidad=2,
                descuento=0.0,
            ),
            ContenidoPedidos(
                id_pedido=11,
                nombre="Tentador Sensacional Envolvente con Cariño_M",
                cantidad=3,
                descuento=0.0,
            ),
            ContenidoPedidos(
                id_pedido=69999,
                nombre="Esponjoso Jugoso Fino con Arte_L",
                cantidad=4,
                descuento=0.0,
            ),
        ]

        self.assertCountEqual(contenido_cargado, contenido_esperado)

    @timeout(N_SECOND)
    def test_xl_contenido_pedidos(self):
        """
        Verifica que los datos carguen bien con un dataset XL de ContenidoPedidos.
        """
        path = os.path.join("data", "xl", "contenido_pedidos.csv")
        generador = cargar_contenido_pedidos(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 1749343)

        # Revisar posiciones aleatorias
        contenido_cargado = [
            generador[0],
            generador[15442],
            generador[33],
            generador[-1],
        ]

        contenido_esperado = [
            ContenidoPedidos(
                id_pedido=0,
                nombre="Tierno Magnífico Radiante con Alegría_L",
                cantidad=1,
                descuento=0.0,
            ),
            ContenidoPedidos(
                id_pedido=6210,
                nombre="Increíble Aromático Asombroso con Nobleza_M",
                cantidad=3,
                descuento=0.0,
            ),
            ContenidoPedidos(
                id_pedido=17,
                nombre="Glorioso Jugoso Vibrante con Maestría_S",
                cantidad=4,
                descuento=0.0,
            ),
            ContenidoPedidos(
                id_pedido=699999,
                nombre="Envolvente Crujiente Apetitoso con Arte_S",
                cantidad=4,
                descuento=0.0,
            ),
        ]

        self.assertCountEqual(contenido_cargado, contenido_esperado)

    @timeout(N_SECOND)
    def test_l_pedidos(self):
        """
        Verifica que los datos carguen bien con un dataset L de Pedidos.
        """
        path = os.path.join("data", "l", "pedidos.csv")
        generador = cargar_pedidos(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 70000)

        # Revisar posiciones aleatorias
        pedidos_cargados = [
            generador[0],
            generador[242],
            generador[54],
            generador[-1],
        ]

        pedidos_esperados = [
            Pedidos(
                id_pedido=0,
                id_local=39917,
                id_cliente=36942,
                fecha="2024-02-24",
                hora="19:07:29",
            ),
            Pedidos(
                id_pedido=242,
                id_local=14554,
                id_cliente=41201,
                fecha="2024-08-18",
                hora="04:46:52",
            ),
            Pedidos(
                id_pedido=54,
                id_local=11441,
                id_cliente=23964,
                fecha="2024-01-25",
                hora="04:19:27",
            ),
            Pedidos(
                id_pedido=69999,
                id_local=17852,
                id_cliente=33551,
                fecha="2024-05-03",
                hora="01:47:12",
            ),
        ]

        self.assertCountEqual(pedidos_cargados, pedidos_esperados)

    @timeout(N_SECOND)
    def test_xl_pedidos(self):
        """
        Verifica que los datos carguen bien con un dataset XL de Pedidos.
        """
        path = os.path.join("data", "xl", "pedidos.csv")
        generador = cargar_pedidos(path)

        # Revisar tipo de dato
        self.assertIsInstance(generador, Iterable)

        # Revisar largo
        generador = list(generador)
        self.assertEqual(len(generador), 700000)

        # Revisar posiciones aleatorias
        pedidos_cargados = [
            generador[0],
            generador[22551],
            generador[54544],
            generador[-1],
        ]

        pedidos_esperados = [
            Pedidos(
                id_pedido=0,
                id_local=2052,
                id_cliente=434366,
                fecha="2024-04-24",
                hora="04:33:57",
            ),
            Pedidos(
                id_pedido=22551,
                id_local=205747,
                id_cliente=19294,
                fecha="2024-07-13",
                hora="06:15:16",
            ),
            Pedidos(
                id_pedido=54544,
                id_local=71198,
                id_cliente=320124,
                fecha="2024-01-23",
                hora="02:24:17",
            ),
            Pedidos(
                id_pedido=699999,
                id_local=11785,
                id_cliente=283147,
                fecha="2024-05-22",
                hora="09:09:21",
            ),
        ]

        self.assertCountEqual(pedidos_cargados, pedidos_esperados)
