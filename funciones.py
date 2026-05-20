"""Funciones para el control de sistemas del local"""
#pylint: disable= w1203
import random


def ingresar_trabajador(hora_actual,hora_inicio_jornada):
    """Simula la llegada de un trabajador"""
    entrada = input("¿INICIAR SISTEMAS? (s/n): ")
    if hora_actual >= hora_inicio_jornada:
        try:
            if entrada.lower() == 's':
                return True
        except AttributeError:
            pass
    return False

def iniciar_jornada(hora_actual, hora_apertura, local_ocupado):
    """Inicia la jornada laboral, abre la puerta y registra el evento"""
    estado_puerta = False
    if hora_apertura <= hora_actual and local_ocupado:
        estado_puerta = True

    return estado_puerta


def aire_luces(hora_actual, hora_inicio_jornada, hora_fin_jornada, local_ocupado):
    """Enciende el aire acondicionado y las luces durante la jornada laboral"""
    estado_aire_luces = False
    if hora_inicio_jornada <= hora_actual <= hora_fin_jornada and local_ocupado:
        estado_aire_luces = True

    return estado_aire_luces

def validar_cierre(local_ocupado):
    """Valida si esta vacio para cerrar el local"""
    validacion = input("¿VALIDAR CIERRE? (s/n): ")
    try:
        if validacion.lower() == 's':
            local_ocupado = False
            return local_ocupado
    except AttributeError:
        pass
    return False

def finalizar_jornada(hora_actual, hora_cierre, local_ocupado):
    """Finaliza la jornada laboral"""
    estado_puerta = False
    estado_aire_luces = False
    if hora_actual > hora_cierre and not local_ocupado:
        estado_puerta = False
        estado_aire_luces = False

    return estado_puerta, estado_aire_luces

def puerta_automatica():
    """Simula detección automática"""
    detectar_persona = random.choice([True, False])
    if detectar_persona:
        print("Persona detectada.")
        print("Puerta abierta.")
    else:
        print("No hay personas.")
        print("Puerta cerrada.")
