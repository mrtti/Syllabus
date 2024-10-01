import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from utilidades import N_SECOND

from consultas import pizzas_pagables_de_un_tamano



class TestPizzasPagablesDeUnTamanoCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica funcionamiento correcto cuando todas las pizzas cuestan más que la cantidad de dinero determinada.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Marga_XL", ingredientes="tomate;queso;albahaca", precio=28000
            ),
            Pizza(nombre="Napolif_S", ingredientes="tomate;jamón;salame", precio=7100),
            Pizza(
                nombre="Hawaiana_XL",
                ingredientes="tomate;queso;jamón;piña",
                precio=29290,
            ),
            Pizza(
                nombre="Pepperoni_L", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ_L",
                ingredientes="tomate;queso;pollo;cebolla;bbq;pepinillos",
                precio=7200,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_pagables_de_un_tamano(
            generador_entregado, 7099, "S"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = []

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica funcionamiento correcto cuando existen pizzas que cuestan igual que la cantidad de dinero determinada.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Marga_XL", ingredientes="tomate;queso;albahaca", precio=28000
            ),
            Pizza(nombre="Napolif_S", ingredientes="tomate;jamón;salame", precio=7100),
            Pizza(
                nombre="Hawaiana_XL",
                ingredientes="tomate;queso;jamón;piña",
                precio=29290,
            ),
            Pizza(
                nombre="Pepperoni_L", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ_L",
                ingredientes="tomate;queso;pollo;cebolla;bbq;pepinillos",
                precio=7200,
            ),
            Pizza(nombre="Marga_S", ingredientes="tomate;queso;albahaca", precio=7100),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_pagables_de_un_tamano(
            generador_entregado, 7100, "S"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(nombre="Marga_S", ingredientes="tomate;queso;albahaca", precio=7100),
            Pizza(nombre="Napolif_S", ingredientes="tomate;jamón;salame", precio=7100),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica funcionamiento correcto cuando, aun habiendo pizzas que cuestan menos que la cantidad de dinero determinada, no son del tamaño determinado.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Marga_XL", ingredientes="tomate;queso;albahaca", precio=28000
            ),
            Pizza(nombre="Napolif_S", ingredientes="tomate;jamón;salame", precio=7100),
            Pizza(
                nombre="Hawaiana_XL",
                ingredientes="tomate;queso;jamón;piña",
                precio=29290,
            ),
            Pizza(
                nombre="Pepperoni_L", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="MEGA MEGA NOT GUNDAM PIZZA_XL",
                ingredientes="tomate;queso;pepperoni;jamon;pepinillo;palta;pina;frambuesa",
                precio=100000,
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo TANAKA BBQ_L",
                ingredientes="tomate;queso;pollo;cebolla;bbq;pepinillos",
                precio=7200,
            ),
            Pizza(nombre="Marga_S", ingredientes="tomate;queso;albahaca", precio=7100),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_pagables_de_un_tamano(
            generador_entregado, 25000, "XL"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = []

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica funcionamiento correcto cuando existe solamente una pizza que cumple con el requisito del tamaño y del precio.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Marga_XL", ingredientes="tomate;queso;albahaca", precio=28000
            ),
            Pizza(nombre="Napolif_S", ingredientes="tomate;jamón;salame", precio=7100),
            Pizza(
                nombre="Hawaiana_XL",
                ingredientes="tomate;queso;jamón;piña",
                precio=29290,
            ),
            Pizza(
                nombre="Pepperoni_L", ingredientes="tomate;queso;pepperoni", precio=7800
            ),
            Pizza(
                nombre="MEGA_PIZZA_XL",
                ingredientes="tomate;queso;pepperoni;jamon;pepinillo;palta;pina;frambuesa",
                precio=100000,
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq;pepinillos",
                precio=7200,
            ),
            Pizza(nombre="Marga_S", ingredientes="tomate;queso;albahaca", precio=7100),
            Pizza(
                nombre="Pepperoni CLASIC_L",
                ingredientes="tomate;queso;pepperoni",
                precio=7900,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_pagables_de_un_tamano(
            generador_entregado, 7850, "L"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Pepperoni_L",
                ingredientes="tomate;queso;pepperoni",
                precio=7800,
            )
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_4(self):
        """
        Verifica funcionamiento correcto cuando existen dos o más pizzas que cumplen con el requisito del tamaño y del precio.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="Marga_XL", ingredientes="tomate;queso;albahaca", precio=28000
            ),
            Pizza(
                nombre="Von Napolif II_S",
                ingredientes="tomate;jamón;salame",
                precio=7100,
            ),
            Pizza(
                nombre="Hawaiana_XL",
                ingredientes="tomate;queso;jamón;piña",
                precio=29290,
            ),
            Pizza(
                nombre="Pepperoni_L", ingredientes="tomate;queso;pepperoni", precio=7800
            ),
            Pizza(
                nombre="MEGA_PIZZA_XL",
                ingredientes="tomate;queso;pepperoni;jamon;pepinillo;palta;pina;frambuesa",
                precio=100000,
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq;pepinillos",
                precio=7200,
            ),
            Pizza(nombre="Marga_S", ingredientes="tomate;queso;albahaca", precio=7100),
            Pizza(
                nombre="Pepperoni CLASIC_L",
                ingredientes="tomate;queso;pepperoni",
                precio=7900,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = pizzas_pagables_de_un_tamano(
            generador_entregado, 15000, "S"
        )

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pedido for pedido in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq;pepinillos",
                precio=7200,
            ),
            Pizza(nombre="Marga_S", ingredientes="tomate;queso;albahaca", precio=7100),
            Pizza(
                nombre="Von Napolif II_S",
                ingredientes="tomate;jamón;salame",
                precio=7100,
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)
