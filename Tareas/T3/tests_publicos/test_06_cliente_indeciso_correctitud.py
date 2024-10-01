import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from utilidades import N_SECOND

from consultas import cliente_indeciso



class ClienteIndecisoCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica funcionamiento correcto cuando todas las pizzas tienen el ingrediente no deseado.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(nombre="Marge_S", ingredientes="tomate;queso;albahaca", precio=8000),
            Pizza(nombre="Napolitan_S", ingredientes="tomate;queso;jamón", precio=7600),
            Pizza(
                nombre="Hawaiana_S", ingredientes="tomate;queso;jamón;piña", precio=7000
            ),
            Pizza(
                nombre="Pepperoni_S", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = cliente_indeciso(generador_entregado, "tomate", 3)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pizza for pizza in resultado_estudiante]

        lista_esperada = []

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica funcionamiento correcto cuando solamente una pizza tiene el ingrediente no deseado.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(nombre="Marge_S", ingredientes="tomate;queso;albahaca", precio=8000),
            Pizza(nombre="Napolitan_S", ingredientes="tomate;queso;jamón", precio=7600),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Pepperoni_S", ingredientes="tomate;queso;pepperoni", precio=8000
            ),
            Pizza(
                nombre="Vegetariana_S",
                ingredientes="tomate;queso;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo NOT BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = cliente_indeciso(generador_entregado, "tomate", 20)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pizza for pizza in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica funcionamiento correcto cuando más de una pizza (pero no todas) tienen el ingrediente no deseado.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(nombre="HOMERO_S", ingredientes="tomate;albahaca", precio=8000),
            Pizza(nombre="Napolitan_S", ingredientes="tomate;queso;jamón", precio=7600),
            Pizza(
                nombre="Hawai SUPER MEGA_S",
                ingredientes="queso;jamón;piña",
                precio=7000,
            ),
            Pizza(
                nombre="CLASS OF Pepperoni_S",
                ingredientes="aceituna;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Ted Vegetariana_S",
                ingredientes="tomate;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(
                nombre="Pollo NOT 9 BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = cliente_indeciso(generador_entregado, "queso", 13)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pizza for pizza in resultado_estudiante]

        lista_esperada = [
            Pizza(nombre="HOMERO_S", ingredientes="tomate;albahaca", precio=8000),
            Pizza(
                nombre="CLASS OF Pepperoni_S",
                ingredientes="aceituna;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Ted Vegetariana_S",
                ingredientes="tomate;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(nombre="HOMERO_S", ingredientes="tomate;albahaca", precio=8000),
            Pizza(
                nombre="CLASS OF Pepperoni_S",
                ingredientes="aceituna;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Ted Vegetariana_S",
                ingredientes="tomate;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(nombre="HOMERO_S", ingredientes="tomate;albahaca", precio=8000),
            Pizza(
                nombre="CLASS OF Pepperoni_S",
                ingredientes="aceituna;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Ted Vegetariana_S",
                ingredientes="tomate;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(nombre="HOMERO_S", ingredientes="tomate;albahaca", precio=8000),
            Pizza(
                nombre="CLASS OF Pepperoni_S",
                ingredientes="aceituna;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Ted Vegetariana_S",
                ingredientes="tomate;champiñones;pimentón;aceitunas",
                precio=9000,
            ),
            Pizza(nombre="HOMERO_S", ingredientes="tomate;albahaca", precio=8000),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica funcionamiento correcto cuando todas las pizzas tienen el ingrediente no deseado.
        """

        Pizza = namedtuple("Pizza", ["nombre", "ingredientes", "precio"])

        lista_entregada = [
            Pizza(
                nombre="HOMERO_S", ingredientes="tomate;albahaca;piedra", precio=8000
            ),
            Pizza(nombre="JUARJUAR_S", ingredientes="tomate;queso;jamón", precio=7600),
            Pizza(
                nombre="Hawai DELTA SUPER MEGA_S",
                ingredientes="queso;jamón;piña;serpiente",
                precio=7000,
            ),
            Pizza(
                nombre="CLASS OF Pepperoni_S",
                ingredientes="aceituna;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Bomber Machine_S",
                ingredientes="tomate;champiñones;pimentón;aceitunas;ojo",
                precio=9000,
            ),
            Pizza(
                nombre="KYRIE NOT 9 BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
        ]

        generador_entregado = (asociacion for asociacion in lista_entregada)

        resultado_estudiante = cliente_indeciso(generador_entregado, "avestruz", 38)

        self.assertIsInstance(resultado_estudiante, (Iterable))

        lista_estudiante = [pizza for pizza in resultado_estudiante]

        lista_esperada = [
            Pizza(
                nombre="HOMERO_S", ingredientes="tomate;albahaca;piedra", precio=8000
            ),
            Pizza(nombre="JUARJUAR_S", ingredientes="tomate;queso;jamón", precio=7600),
            Pizza(
                nombre="Hawai DELTA SUPER MEGA_S",
                ingredientes="queso;jamón;piña;serpiente",
                precio=7000,
            ),
            Pizza(
                nombre="CLASS OF Pepperoni_S",
                ingredientes="aceituna;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Bomber Machine_S",
                ingredientes="tomate;champiñones;pimentón;aceitunas;ojo",
                precio=9000,
            ),
            Pizza(
                nombre="KYRIE NOT 9 BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
            Pizza(
                nombre="HOMERO_S", ingredientes="tomate;albahaca;piedra", precio=8000
            ),
            Pizza(nombre="JUARJUAR_S", ingredientes="tomate;queso;jamón", precio=7600),
            Pizza(
                nombre="Hawai DELTA SUPER MEGA_S",
                ingredientes="queso;jamón;piña;serpiente",
                precio=7000,
            ),
            Pizza(
                nombre="CLASS OF Pepperoni_S",
                ingredientes="aceituna;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Bomber Machine_S",
                ingredientes="tomate;champiñones;pimentón;aceitunas;ojo",
                precio=9000,
            ),
            Pizza(
                nombre="KYRIE NOT 9 BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
            Pizza(
                nombre="HOMERO_S", ingredientes="tomate;albahaca;piedra", precio=8000
            ),
            Pizza(nombre="JUARJUAR_S", ingredientes="tomate;queso;jamón", precio=7600),
            Pizza(
                nombre="Hawai DELTA SUPER MEGA_S",
                ingredientes="queso;jamón;piña;serpiente",
                precio=7000,
            ),
            Pizza(
                nombre="CLASS OF Pepperoni_S",
                ingredientes="aceituna;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Bomber Machine_S",
                ingredientes="tomate;champiñones;pimentón;aceitunas;ojo",
                precio=9000,
            ),
            Pizza(
                nombre="KYRIE NOT 9 BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
            Pizza(
                nombre="HOMERO_S", ingredientes="tomate;albahaca;piedra", precio=8000
            ),
            Pizza(nombre="JUARJUAR_S", ingredientes="tomate;queso;jamón", precio=7600),
            Pizza(
                nombre="Hawai DELTA SUPER MEGA_S",
                ingredientes="queso;jamón;piña;serpiente",
                precio=7000,
            ),
            Pizza(
                nombre="CLASS OF Pepperoni_S",
                ingredientes="aceituna;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Bomber Machine_S",
                ingredientes="tomate;champiñones;pimentón;aceitunas;ojo",
                precio=9000,
            ),
            Pizza(
                nombre="KYRIE NOT 9 BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
            Pizza(
                nombre="HOMERO_S", ingredientes="tomate;albahaca;piedra", precio=8000
            ),
            Pizza(nombre="JUARJUAR_S", ingredientes="tomate;queso;jamón", precio=7600),
            Pizza(
                nombre="Hawai DELTA SUPER MEGA_S",
                ingredientes="queso;jamón;piña;serpiente",
                precio=7000,
            ),
            Pizza(
                nombre="CLASS OF Pepperoni_S",
                ingredientes="aceituna;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Bomber Machine_S",
                ingredientes="tomate;champiñones;pimentón;aceitunas;ojo",
                precio=9000,
            ),
            Pizza(
                nombre="KYRIE NOT 9 BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
            Pizza(
                nombre="HOMERO_S", ingredientes="tomate;albahaca;piedra", precio=8000
            ),
            Pizza(nombre="JUARJUAR_S", ingredientes="tomate;queso;jamón", precio=7600),
            Pizza(
                nombre="Hawai DELTA SUPER MEGA_S",
                ingredientes="queso;jamón;piña;serpiente",
                precio=7000,
            ),
            Pizza(
                nombre="CLASS OF Pepperoni_S",
                ingredientes="aceituna;pepperoni",
                precio=8000,
            ),
            Pizza(
                nombre="Bomber Machine_S",
                ingredientes="tomate;champiñones;pimentón;aceitunas;ojo",
                precio=9000,
            ),
            Pizza(
                nombre="KYRIE NOT 9 BBQ_S",
                ingredientes="tomate;queso;pollo;cebolla;bbq",
                precio=10000,
            ),
            Pizza(
                nombre="HOMERO_S", ingredientes="tomate;albahaca;piedra", precio=8000
            ),
            Pizza(nombre="JUARJUAR_S", ingredientes="tomate;queso;jamón", precio=7600),
        ]

        self.assertCountEqual(lista_estudiante, lista_esperada)
