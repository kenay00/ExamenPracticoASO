import psutil

def obtener_particiones():
  """Obtiene la información de las particiones del sistema."""
  particiones = psutil.disk_partitions()
  return particiones

def mostrar_porcentaje_ocupado(particiones):
  """Muestra el porcentaje de espacio ocupado en cada partición."""
  for particion in particiones:
    try:
      uso = psutil.disk_usage(particion.mountpoint)
      porcentaje_ocupado = round(uso.percent, 1)
      print(f"{particion.mountpoint} {porcentaje_ocupado}%")
    except PermissionError:
      # Ignora particiones sin permisos de lectura
      pass

# Obtener particiones y mostrar porcentaje
particiones = obtener_particiones()
mostrar_porcentaje_ocupado(particiones)
