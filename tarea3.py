import os

# Ruta del Escritorio
ruta_escritorio = os.path.join(os.environ["USERPROFILE"], "Desktop")

for i in range(1, 6):
  # Crear carpeta
  nombre_carpeta = f"folder{i}"
  ruta_carpeta = os.path.join(ruta_escritorio, nombre_carpeta)

  try:
    os.mkdir(ruta_carpeta)
  except FileExistsError:
    print(f"La carpeta '{nombre_carpeta}' ya existe.")

  # Crear 10 archivos dentro de la carpeta
  for j in range(1, 11):
    nombre_archivo = f"fichero{j}.txt"
    ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
    contenido = "Este es el contenido del fichero {}".format(j)
    with open(ruta_archivo, "w") as archivo:
      archivo.write(contenido)

print("Proceso hecho")
