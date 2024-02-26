import os
import psutil
import logging

def analizar_espacio_disco():

    # Ruta del archivo de log
    ruta_log = "/home/berny/Escritorio/espacio.log"

    # Crear la carpeta de logs si no existe
    if not os.path.exists(os.path.dirname(ruta_log)):
        os.makedirs(os.path.dirname(ruta_log))

    # Configurar logging
    logging.basicConfig(filename=ruta_log, level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

    # Obtener información de la partición raíz
    particion_raiz = psutil.disk_usage("/")

    # Calcular porcentaje de espacio ocupado
    porcentaje_ocupado = round(particion_raiz.percent, 1)

    # Generar mensaje de log según el porcentaje
    if porcentaje_ocupado > 80:
        logging.error("Espacio en disco crítico: ¡%s%% ocupado!", porcentaje_ocupado)
    elif porcentaje_ocupado > 60:
        logging.warning("Espacio en disco bajo: %s%% ocupado.", porcentaje_ocupado)
    else:
        logging.info("Espacio en disco disponible: %s%% ocupado.", porcentaje_ocupado)

    # Mensaje final
    print("Proceso ya hecho mira el archivo de log en el Escritorio:", ruta_log)

# Llamada a la función
analizar_espacio_disco()
