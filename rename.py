from pathlib import Path
import os
sep = os.path.sep
carpeta = Path("/media/mayra/Acer/Users/User1/Desktop/Nova pasta (2)/Proyecto/Cena 1 VF").resolve()



for archivo in carpeta.iterdir():
    name = archivo.name
    if " .jpg" in name:
      print(archivo.name)
      nuevoNombre = name.split(" .")
      nombreFinal = nuevoNombre[0] + ".jpg"
      archivo.rename(f'/media/mayra/Acer/Users/User1/Desktop/Nova pasta (2)/Proyecto/Cena 1 VF/{nombreFinal}')
      print(nombreFinal)
