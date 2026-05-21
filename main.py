"""Programa para controlar el encendido y apagado de luces,
aire acondicionado y puerta de un local comercial"""
#pylint: disable= w1203
import datetime
import logging

logging.basicConfig(
    filename='registro.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
#Hora actual
hora_actual = datetime.datetime.now().time()

#Horario del local y trabajadores
hora_inicio_jornada = datetime.time(6, 0, 0)  # 6:00 AM
hora_fin_jornada = datetime.time(18, 0, 0)  # 6:00 PM
hora_apertura = datetime.time(7, 0, 0)  # Hora de apertura del local 7:00 AM
hora_cierre = datetime.time(18, 0, 0)  # Hora de cierre del local 6:00 PM

#Se pone en True cuando llega el primer trabajador
#Se pone en False cuando se va el ultimo trabajador
LOCAL_OCUPADO = False

estado_aire = False
estado_luces = False
estado_puerta = False

#Si la hora actual esta entre hora apertura y hora cierre, se inicia la jornada laboral
if hora_apertura <= hora_actual <= hora_cierre:
    logging.info(f"Inicio de jornada laboral: {hora_actual}")
    estado_puerta = True
    logging.info(f"Puerta abierta: {hora_actual}")

#Si la hora actual esta entre la hora de inicio y fin de jornada, se encienden el aire y las luces
if hora_inicio_jornada <= hora_actual <= hora_fin_jornada:
    estado_aire = True
    estado_luces = True
    logging.info(f"Aire y luces encendidos: {hora_actual}")

#Si la hora actual es mayor a la hora de cierre, se cierra la puerta y se apagan el aire y las luces
if hora_actual > hora_cierre and LOCAL_OCUPADO == False:
    estado_puerta = False
    estado_aire = False
    estado_luces = False
    logging.info("Jornada laboral finalizada.")
    logging.info(f"Puerta cerrada, aire y luces apagados: {hora_actual}")
