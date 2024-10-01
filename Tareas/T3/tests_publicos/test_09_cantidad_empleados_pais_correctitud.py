import os
import sys
import unittest
from collections import namedtuple
from collections.abc import Iterable

from tests_publicos.timeout_function import timeout
from utilidades import N_SECOND

from consultas import cantidad_empleados_pais


class TestCantidadEmpleadosPaisCorrectitud(unittest.TestCase):

    def shortDescription(self):
        doc = self._testMethodDoc
        return doc or None

    @timeout(N_SECOND)
    def test_0(self):
        """
        Verifica funcionamiento correcto cuando no existen locales del país determinado.
        """
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie link Tunnel Apt. 363",
                pais="Uzbekistan",
                ciudad="Hillhaven",
                cantidad_trabajadores=3,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks jardines",
                pais="Slovenia",
                ciudad="North Trevor",
                cantidad_trabajadores=9,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Chile",
                ciudad="Santiago",
                cantidad_trabajadores=6,
            ),
            Local(
                id_local=4,
                direccion="Calle Fake 12226",
                pais="Chile",
                ciudad="Valdivia",
                cantidad_trabajadores=4,
            ),
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
                pais="Ecuador",
                ciudad="Santiago",
                cantidad_trabajadores=2,
            ),
        ]

        generador_entregado_locales = (asociacion for asociacion in lista_entregada)

        int_estudiante = cantidad_empleados_pais(
            generador_entregado_locales, "Argentina"
        )

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 0

        self.assertEqual(int_estudiante, int_esperado)

    @timeout(N_SECOND)
    def test_1(self):
        """
        Verifica funcionamiento correcto cuando existe solamente un local del país determinado y solo un empleado.
        """
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie link Tunnel Apt. 363",
                pais="Uzbekistan",
                ciudad="Hillhaven",
                cantidad_trabajadores=3,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks jardines",
                pais="Slovenia",
                ciudad="North Trevor",
                cantidad_trabajadores=1,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Chile",
                ciudad="Santiago",
                cantidad_trabajadores=6,
            ),
            Local(
                id_local=4,
                direccion="Calle Fake 12226",
                pais="Sloth",
                ciudad="Valdivia",
                cantidad_trabajadores=1,
            ),
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
                pais="Ecuador",
                ciudad="Santiago",
                cantidad_trabajadores=2,
            ),
        ]

        generador_entregado_locales = (asociacion for asociacion in lista_entregada)

        int_estudiante = cantidad_empleados_pais(
            generador_entregado_locales, "Slovenia"
        )

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 1

        self.assertEqual(int_estudiante, int_esperado)

    @timeout(N_SECOND)
    def test_2(self):
        """
        Verifica funcionamiento correcto cuando existe solamente un local del país determinado y dos o más empleados.
        """
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie link Tunnel Apt. 363",
                pais="Uzbekistan",
                ciudad="Hillhaven",
                cantidad_trabajadores=3,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks jardines",
                pais="Slovenia",
                ciudad="North Trevor",
                cantidad_trabajadores=1,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Chile",
                ciudad="Santiago",
                cantidad_trabajadores=6,
            ),
            Local(
                id_local=4,
                direccion="Calle CONCAT Fake CONCAT 12226",
                pais="Chile",
                ciudad="Valdivia",
                cantidad_trabajadores=11,
            ),
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
                pais="Croatia",
                ciudad="Santiago",
                cantidad_trabajadores=2546,
            ),
            Local(
                id_local=6,
                direccion="Cal INSERT el 213",
                pais="Croacia",
                ciudad="Santiago",
                cantidad_trabajadores=23213,
            ),
        ]

        generador_entregado_locales = (asociacion for asociacion in lista_entregada)

        int_estudiante = cantidad_empleados_pais(generador_entregado_locales, "Croacia")

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 23213

        self.assertEqual(int_estudiante, int_esperado)

    @timeout(N_SECOND)
    def test_3(self):
        """
        Verifica funcionamiento correcto cuando existe solamente un local del país determinado y dos o más empleados.
        """
        Local = namedtuple(
            "Local",
            ["id_local", "direccion", "pais", "ciudad", "cantidad_trabajadores"],
        )

        lista_entregada = [
            Local(
                id_local=1,
                direccion="85024 Valerie link Tunnel Apt. 363",
                pais="Uzbekistan",
                ciudad="Hillhaven",
                cantidad_trabajadores=3,
            ),
            Local(
                id_local=2,
                direccion="3896 Garza Brooks jardines",
                pais="Slovenia",
                ciudad="North Trevor",
                cantidad_trabajadores=1,
            ),
            Local(
                id_local=3,
                direccion="Calle Falsa 101",
                pais="Chile",
                ciudad="Santiago",
                cantidad_trabajadores=64,
            ),
            Local(
                id_local=4,
                direccion="Calle Fake 12226",
                pais="Chile",
                ciudad="Valdivia",
                cantidad_trabajadores=131,
            ),
            Local(
                id_local=5,
                direccion="Calle Falsa 127",
                pais="DROP TABLE",
                ciudad="El futuro es hoy",
                cantidad_trabajadores=2546,
            ),
            Local(
                id_local=6,
                direccion="Cal el 213",
                pais="Croacia",
                ciudad="FAs0111100000111111111111111110",
                cantidad_trabajadores=23213,
            ),
            Local(
                id_local=7,
                direccion="Calle Falsa 123427",
                pais="Chile",
                ciudad="Steve",
                cantidad_trabajadores=2,
            ),
        ]

        generador_entregado_locales = (asociacion for asociacion in lista_entregada)

        int_estudiante = cantidad_empleados_pais(generador_entregado_locales, "Chile")

        self.assertIsInstance(int_estudiante, (int))

        int_esperado = 197

        self.assertEqual(int_estudiante, int_esperado)
