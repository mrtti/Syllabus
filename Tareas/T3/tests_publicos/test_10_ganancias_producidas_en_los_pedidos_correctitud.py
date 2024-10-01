import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from utilidades import N_SECOND

from consultas import ganancias_producidas_en_los_pedidos



class TestGananciasProducidasEnLosPedidosCorrectitud(unittest.TestCase):

    def shortDescription(self):

        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que el test funcione si es que que no hay pedidos en el generador
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
                nombre="Pollo BBQ",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
            Pizza(
                nombre="Pepperoni", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
        ]

        generador_entregado_pizzas = (pizza for pizza in lista_entregada)

        lista_entregada = []

        generador_entregado_contenido_pedidos = (pedido for pedido in lista_entregada)

        resultado_estudiante = ganancias_producidas_en_los_pedidos(
            generador_entregado_contenido_pedidos, generador_entregado_pizzas
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = []

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que el test funcione si es que todos los pedidos tienen un solo producto
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=811382,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=11385,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12345,
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.23
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.0
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = ganancias_producidas_en_los_pedidos(
            generador_entregado_contenido_pedidos, generador_entregado_pizzas
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [(1, 811382), (2, 1249528), (3, 34155), (4, 34566), (5, 61725)]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que el test funcione si es que todos los pedidos tienen más de un producto
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=811382,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=11385,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Margarita", ingredientes="tomate;queso;albahaca", precio=5000
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(id_pedido=1, nombre="Margarita", cantidad=2, descuento=0.0),
            ContenidoPedido(
                id_pedido=5, nombre="Pepperoni Clásica_M", cantidad=6, descuento=0.23
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.23
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = ganancias_producidas_en_los_pedidos(
            generador_entregado_contenido_pedidos, generador_entregado_pizzas
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [(1, 821382), (3, 58474), (5, 3796113)]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Test que verifique que funcione al haber 5 pedidos de múltiples productos.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=811382,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=11385,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Margarita_S", ingredientes="tomate;queso;albahaca", precio=5000
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Margarita_S", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.15
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Hawaiiana_M", cantidad=4, descuento=0.15
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.23
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pepperoni Clásica_M", cantidad=6, descuento=0.23
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Margarita_S", cantidad=2, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Vegetariana_M", cantidad=3, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = ganancias_producidas_en_los_pedidos(
            generador_entregado_contenido_pedidos, generador_entregado_pizzas
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            (1, 821382),
            (3, 71005),
            (5, 3796113),
            (6, 649106),
            (7, 65474),
            (8, 61725),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Test que verifique que funcione al haber 8 pedidos de múltiples productos.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=811382,
            ),
            Pizza(
                nombre="Vegetariana_M",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=11385,
            ),
            Pizza(
                nombre="Hawaiiana_M",
                ingredientes="piña;jamón;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Camarones sobre ajo_S",
                ingredientes="camarones;ajo;queso;salsa de tomate",
                precio=12345,
            ),
            Pizza(
                nombre="Margarita_S", ingredientes="tomate;queso;albahaca", precio=5000
            ),
        ]

        generador_entregado_pizzas = (asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=1, nombre="Margarita_S", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.15
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Hawaiiana_M", cantidad=4, descuento=0.15
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.23
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Pepperoni Clásica_M", cantidad=6, descuento=0.23
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Margarita_S", cantidad=2, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Vegetariana_M", cantidad=3, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Pepperoni Clásica_M", cantidad=6, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Margarita_S", cantidad=2, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Vegetariana_M", cantidad=3, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Pepperoni Clásica_M", cantidad=6, descuento=0.3
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        resultado_estudiante = ganancias_producidas_en_los_pedidos(
            generador_entregado_contenido_pedidos, generador_entregado_pizzas
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            (1, 821382),
            (3, 71005),
            (5, 3796113),
            (6, 649106),
            (7, 65474),
            (8, 4930017),
            (9, 821382),
            (10, 3509486),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)
