import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from utilidades import N_SECOND

from consultas import gasto_cliente_por_mes



class TestGastoClientePorMesCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica que el test funcione si es que el gasto para el cliente es 0 todos los meses
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8182,
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

        generador_entregado_pizzas = (
            asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=1, fecha="2021-04-01", hora="12:30"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=1, fecha="2021-03-01", hora="17:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=1, fecha="2021-02-01", hora="18:30"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=1, fecha="2021-06-01", hora="13:00"
            ),
            Pedido(
                id_pedido=7, id_local=1, id_cliente=2, fecha="2021-06-01", hora="13:00"
            ),
            Pedido(
                id_pedido=8, id_local=1, id_cliente=2, fecha="2021-06-01", hora="13:00"
            ),
            Pedido(
                id_pedido=9, id_local=1, id_cliente=3, fecha="2021-06-01", hora="13:00"
            ),
        ]

        generador_entregado_pedidos = (
            asociacion for asociacion in lista_entregada)

        resultado_estudiante = gasto_cliente_por_mes(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_pizzas,
            1,
            2022,
        )

        resultado_esperado = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica que el test funcione si es que el cliente por el que se pregunta no ha hecho pedidos
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8182,
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

        generador_entregado_pizzas = (
            asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=11, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=12, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=1, fecha="2021-04-01", hora="12:30"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=1, fecha="2021-03-01", hora="17:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=1, fecha="2021-02-01", hora="18:30"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=1, fecha="2021-06-01", hora="13:00"
            ),
            Pedido(
                id_pedido=7, id_local=2, id_cliente=1, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=8, id_local=2, id_cliente=1, fecha="2021-04-01", hora="12:30"
            ),
            Pedido(
                id_pedido=9, id_local=2, id_cliente=1, fecha="2021-03-01", hora="17:00"
            ),
            Pedido(
                id_pedido=10, id_local=2, id_cliente=1, fecha="2021-02-01", hora="18:30"
            ),
            Pedido(
                id_pedido=11, id_local=2, id_cliente=1, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=12, id_local=2, id_cliente=2, fecha="2021-12-01", hora="13:00"
            ),
        ]

        generador_entregado_pedidos = (
            asociacion for asociacion in lista_entregada)

        resultado_estudiante = gasto_cliente_por_mes(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_pizzas,
            3,
            2021,
        )

        resultado_esperado = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        self.assertIsInstance(resultado_estudiante, (Iterable))

        self.assertEqual(list(resultado_estudiante), resultado_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica que el test funcione si es que el cliente ha hecho múltiples pedidos en meses aunque no en todos.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8182,
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

        generador_entregado_pizzas = (
            asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=11, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=12, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:30"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=1, fecha="2021-03-01", hora="17:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=1, fecha="2021-03-01", hora="18:30"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=1, fecha="2021-05-01", hora="12:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=1, fecha="2021-05-01", hora="13:00"
            ),
            Pedido(
                id_pedido=7, id_local=2, id_cliente=1, fecha="2021-06-01", hora="12:00"
            ),
            Pedido(
                id_pedido=8, id_local=2, id_cliente=1, fecha="2021-07-01", hora="12:30"
            ),
            Pedido(
                id_pedido=9, id_local=2, id_cliente=1, fecha="2021-08-01", hora="17:00"
            ),
            Pedido(
                id_pedido=10, id_local=2, id_cliente=1, fecha="2021-09-01", hora="18:30"
            ),
            Pedido(
                id_pedido=11, id_local=2, id_cliente=1, fecha="2021-10-01", hora="12:00"
            ),
            Pedido(
                id_pedido=12, id_local=2, id_cliente=2, fecha="2021-11-01", hora="13:00"
            ),
        ]

        generador_entregado_pedidos = (
            asociacion for asociacion in lista_entregada)

        resultado_estudiante = gasto_cliente_por_mes(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_pizzas,
            1,
            2021,
        )

        resultado_esperado = [
            16364,
            0,
            48228,
            0,
            68271,
            34566,
            9818,
            61725,
            13662,
            6546,
            0,
            0,
        ]

        self.assertIsInstance(resultado_estudiante, (list))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica que el test funcione si es que el cliente ha hecho múltiples pedidos en todos los meses.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8182,
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

        generador_entregado_pizzas = (
            asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Hawaiiana_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=11, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=12, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=13, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=14, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=15, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2021-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=1, fecha="2021-02-01", hora="12:30"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=1, fecha="2021-03-01", hora="17:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=1, fecha="2021-04-01", hora="18:30"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=1, fecha="2021-05-01", hora="12:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=1, fecha="2021-06-01", hora="13:00"
            ),
            Pedido(
                id_pedido=7, id_local=2, id_cliente=1, fecha="2021-07-01", hora="12:00"
            ),
            Pedido(
                id_pedido=8, id_local=2, id_cliente=1, fecha="2021-08-01", hora="12:30"
            ),
            Pedido(
                id_pedido=9, id_local=2, id_cliente=1, fecha="2021-09-01", hora="17:00"
            ),
            Pedido(
                id_pedido=10, id_local=2, id_cliente=1, fecha="2021-10-01", hora="18:30"
            ),
            Pedido(
                id_pedido=11, id_local=2, id_cliente=1, fecha="2021-11-01", hora="12:00"
            ),
            Pedido(
                id_pedido=12, id_local=2, id_cliente=2, fecha="2021-12-01", hora="13:00"
            ),
            Pedido(
                id_pedido=13, id_local=2, id_cliente=1, fecha="2021-12-01", hora="13:00"
            ),
            Pedido(
                id_pedido=14, id_local=2, id_cliente=2, fecha="2021-10-01", hora="13:00"
            ),
            Pedido(
                id_pedido=15, id_local=2, id_cliente=2, fecha="2021-11-01", hora="13:00"
            ),
        ]

        generador_entregado_pedidos = (
            asociacion for asociacion in lista_entregada)

        resultado_estudiante = gasto_cliente_por_mes(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_pizzas,
            1,
            2021,
        )

        resultado_esperado = [
            6546,
            24632,
            13662,
            34566,
            61725,
            6546,
            34566,
            9818,
            61725,
            13662,
            6546,
            6546,
        ]

        self.assertIsInstance(resultado_estudiante, (list))

        self.assertEqual(resultado_estudiante, resultado_esperado)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica que el test funcione si es que el cliente ha hecho múltiples pedidos en todos los meses.
        """
        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Pepperoni Clásica_M",
                ingredientes="pepperoni;queso;salsa de tomate",
                precio=8182,
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

        generador_entregado_pizzas = (
            asociacion for asociacion in lista_entregada)

        ContenidoPedido = namedtuple(
            "ContenidoPedido", ["id_pedido", "nombre", "cantidad", "descuento"]
        )

        lista_entregada = [
            ContenidoPedido(
                id_pedido=1, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Hawaiiana_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=2, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=4, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=5, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=3, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=6, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=7, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=8, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=9, nombre="Camarones sobre ajo_S", cantidad=5, descuento=0.0
            ),
            ContenidoPedido(
                id_pedido=10, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
            ContenidoPedido(
                id_pedido=11, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=12, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=13, nombre="Pepperoni Clásica_M", cantidad=1, descuento=0.2
            ),
            ContenidoPedido(
                id_pedido=14, nombre="Hawaiiana_M", cantidad=4, descuento=0.3
            ),
            ContenidoPedido(
                id_pedido=15, nombre="Pepperoni Clásica_M", cantidad=2, descuento=0.4
            ),
            ContenidoPedido(
                id_pedido=16, nombre="Vegetariana_M", cantidad=3, descuento=0.6
            ),
        ]

        generador_entregado_contenido_pedidos = (
            asociacion for asociacion in lista_entregada
        )

        Pedido = namedtuple(
            "Pedido", ["id_pedido", "id_local", "id_cliente", "fecha", "hora"]
        )

        lista_entregada = [
            Pedido(
                id_pedido=1, id_local=1, id_cliente=1, fecha="2022-01-01", hora="12:00"
            ),
            Pedido(
                id_pedido=2, id_local=1, id_cliente=1, fecha="2021-02-01", hora="12:30"
            ),
            Pedido(
                id_pedido=3, id_local=1, id_cliente=1, fecha="2021-03-06", hora="17:00"
            ),
            Pedido(
                id_pedido=4, id_local=1, id_cliente=1, fecha="2021-04-01", hora="18:30"
            ),
            Pedido(
                id_pedido=5, id_local=1, id_cliente=1, fecha="2021-05-01", hora="12:00"
            ),
            Pedido(
                id_pedido=6, id_local=1, id_cliente=1, fecha="2021-06-01", hora="13:00"
            ),
            Pedido(
                id_pedido=7, id_local=2, id_cliente=1, fecha="2021-07-01", hora="12:00"
            ),
            Pedido(
                id_pedido=8, id_local=2, id_cliente=1, fecha="2021-08-01", hora="12:30"
            ),
            Pedido(
                id_pedido=9, id_local=2, id_cliente=1, fecha="2021-09-01", hora="17:00"
            ),
            Pedido(
                id_pedido=10, id_local=2, id_cliente=1, fecha="2021-10-01", hora="18:30"
            ),
            Pedido(
                id_pedido=11, id_local=2, id_cliente=1, fecha="2021-11-01", hora="12:00"
            ),
            Pedido(
                id_pedido=12, id_local=2, id_cliente=2, fecha="2021-12-01", hora="13:00"
            ),
            Pedido(
                id_pedido=13, id_local=2, id_cliente=1, fecha="2021-12-01", hora="13:00"
            ),
            Pedido(
                id_pedido=14, id_local=2, id_cliente=2, fecha="2021-10-01", hora="13:00"
            ),
            Pedido(
                id_pedido=15, id_local=2, id_cliente=2, fecha="2021-11-01", hora="13:00"
            ),
            Pedido(
                id_pedido=16, id_local=2, id_cliente=1, fecha="2021-04-01", hora="13:00"
            ),
        ]

        generador_entregado_pedidos = (
            asociacion for asociacion in lista_entregada)

        resultado_estudiante = gasto_cliente_por_mes(
            generador_entregado_contenido_pedidos,
            generador_entregado_pedidos,
            generador_entregado_pizzas,
            1,
            2021,
        )

        resultado_esperado = [
            0,
            24632,
            13662,
            48228,
            61725,
            6546,
            34566,
            9818,
            61725,
            13662,
            6546,
            6546,
        ]

        self.assertIsInstance(resultado_estudiante, (list))

        self.assertEqual(resultado_estudiante, resultado_esperado)
