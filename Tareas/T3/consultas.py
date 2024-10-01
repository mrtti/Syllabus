from typing import Any, Generator, Iterable


# Carga de datos

def cargar_pizzas(path: str) -> Generator:
    pass

def cargar_locales(path: str) -> Generator:
    pass

def cargar_pedidos(path: str) -> Generator:
    pass

def cargar_contenido_pedidos(path: str) -> Generator:
    pass


# Consultas que ocupan 1 generador

def pedidos_con_al_menos_esta_pizza(
        generador_contenido_pedidos: Generator,
        tipo_de_pizza: str
        ) -> Iterable:
    pass

def cantidad_vendida_de_pizza_por_tipo(
        generador_contenido_pedidos: Generator,
        tipo_de_pizza: str
        ) -> int:
    pass

def pedido_con_mayor_descuento_utilizado(
        generador_contenido_pedidos: Generator
        ) -> Iterable:
    pass

def ajustar_precio_segun_ingredientes(
        generador_pizzas: Generator,
        ingrediente: str,
        diferencia_precio: int
        ) -> Iterable:
    pass

def clientes_despues_hora(
        generador_pedidos: Generator,
        hora: str
        ) -> str:
    pass

def cliente_indeciso(
        generador_pizzas: Generator,
        ingrediente_no_deseado: str,
        cantidad_pizzas: int
        ) -> Iterable:
    pass

def pizzas_con_ingrediente(
        generador_pizzas: Generator,
        ingrediente: str
        ) -> Iterable:
    pass


def pizzas_pagables_de_un_tamano(
        generador_pizzas: Generator,
        dinero: int,
        tamano: str
    ) -> Iterable:
    pass

def cantidad_empleados_pais(
        generador_locales: Generator,
        pais: str
        ) -> int:
    pass


# Consultas que ocupan 2 Generadores

def ganancias_producidas_en_los_pedidos(
        generador_contenido_pedidos: Generator,
        generador_pizzas: Generator
        ) -> Iterable:
    pass

def pizza_mas_vendida_del_dia(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        fecha: str
        ) -> set:
    pass


def pizza_del_mes(
        generador_pedidos: Generator,
        generador_contenido_pedidos: Generator,
        mes: str
        ) -> str:
    pass

def popularidad_mezcla_de_ingredientes(
        generador_pizzas: Generator,
        generador_contenido_pedidos: Generator,
        ingredientes: set
        ) -> int:
    pass


def total_ahorrado_pedidos(
        generador_contenido_pedidos: Generator,
        generador_pizzas: Generator
        ) -> str:
    pass

def pizza_favorita_cliente(
        generador_pedidos: Generator,
        generador_contenido_pedidos: Generator,
        id_cliente: int,
        ) -> tuple:
    pass


# Consultas que ocupan 3 o mas Generadores

def local_mas_pizzas_vendidas_por_tipo_de_pizza(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        generador_locales: Generator,
        tipo_de_pizza: str
        ) -> Iterable:
    pass

def ganancia_total_de_un_local(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        generador_pizzas: Generator,
        id_local: int
        ) -> int:
    pass


def promedio_ventas_con_descuento_de_un_pais(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        generador_locales: Generator,
        pais: str
        ) -> float:
    pass


def gasto_cliente_por_mes(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        generador_pizzas: Generator,
        id_cliente: int,
        year: int,
        ) -> list:
    pass

def pizzas_vendidas_mes_pais(
        generador_contenido_pedidos: Generator,
        generador_pedidos: Generator,
        generador_locales: Generator,
        pais: str,
        mes: int,
        year: int,
        ) -> int:
    pass


# Consulta anidada

def consulta_anidada(instrucciones: dict) -> Any:
    pass
