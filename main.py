"""Programa para controlar el encendido y apagado
de luces, aire acondicionado y puerta de un local comercial"""
# pylint: disable=w1203
# pylint: disable=c0103

import datetime
import logging
import funciones

# CONFIGURACION DEL LOG
logging.basicConfig(
    filename='registro.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

# HORA ACTUAL
hora_actual = datetime.datetime.now().time()

# HORARIOS DEL LOCAL
hora_inicio_jornada = datetime.time(6, 0, 0)
hora_fin_jornada = datetime.time(18, 0, 0)
hora_apertura = datetime.time(7, 0, 0)
hora_cierre = datetime.time(18, 0, 0)

def main():
    """Función principal para controlar el sistema del local"""

    # INGRESO DEL PRIMER TRABAJADOR
    local_ocupado = funciones.ingresar_trabajador(hora_actual,hora_inicio_jornada)
    logging.info(f"Local ocupado: {local_ocupado}")
    print(f"Local ocupado: {local_ocupado}")

    # ESTADOS INICIALES
    estado_puerta = False
    estado_aire_luces = False

    # INICIO DE JORNADA
    estado_puerta = funciones.iniciar_jornada(hora_actual,hora_apertura,local_ocupado)
    logging.info(f"Estado puerta: {estado_puerta}")
    print(f"Estado puerta: {estado_puerta}")

    # CONTROL DE AIRE Y LUCES
    estado_aire_luces = funciones.aire_luces(hora_actual,
        hora_inicio_jornada,
        hora_fin_jornada,
        local_ocupado)
    logging.info(f"Estado aire y luces: {estado_aire_luces}")
    print(f"Estado aire y luces: {estado_aire_luces}")

    # VALIDACION DE CIERRE

    salida_ultimo = funciones.validar_cierre(local_ocupado)
    if salida_ultimo:
        local_ocupado = False

    logging.info(f"Local ocupado despues de validar cierre: {local_ocupado}")
    print(f"Local ocupado despues de validar cierre: {local_ocupado}")

    # FINALIZAR JORNADA

    estado_puerta, estado_aire_luces = (
    funciones.finalizar_jornada(
            hora_actual,
            hora_cierre,
            local_ocupado))
    logging.info(f"Estado final puerta: {estado_puerta}")
    logging.info(f"Estado final aire y luces: {estado_aire_luces}")
    print(f"Estado final puerta: {estado_puerta}")
    print(f"Estado final aire y luces: {estado_aire_luces}")

logging.info("La puerta se abre automáticamente:")
print(f"La puerta se abre automáticamente: {funciones.puerta_automatica()}")
print(f"La puerta se abre automáticamente: {funciones.puerta_automatica()}")
print(f"La puerta se abre automáticamente: {funciones.puerta_automatica()}")
print(f"La puerta se abre automáticamente: {funciones.puerta_automatica()}")

if __name__ == "__main__":
    main()
