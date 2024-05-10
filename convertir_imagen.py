import base64
import os

def imagen_a_base64_y_guardar_txt(ruta_imagen):
    # Verificar si la ruta de la imagen es válida
    if not os.path.isfile(ruta_imagen):
        print("La ruta de la imagen no es válida.")
        return

    # Leer el contenido de la imagen
    with open(ruta_imagen, "rb") as img_file:
        # Leer el contenido de la imagen en bytes
        img_bytes = img_file.read()

        # Convertir la imagen en base64
        base64_img = base64.b64encode(img_bytes).decode("utf-8")

        # Obtener la ruta y el nombre del archivo de la imagen
        directorio, nombre_archivo = os.path.split(ruta_imagen)

        # Crear la ruta para el archivo de texto
        ruta_txt = os.path.join(directorio, nombre_archivo.split(".")[0] + ".txt")

        # Escribir el contenido base64 en el archivo de texto
        with open(ruta_txt, "w") as txt_file:
            txt_file.write(base64_img)

        print(f"La imagen se ha convertido correctamente en base64 y se ha guardado en {ruta_txt}.")

# Ejemplo de uso
ruta_imagen = "E:\ProyectoAire\FormatosAirePdf\imagenes\FirmaDirector.png"  # Reemplaza con la ruta de tu imagen
imagen_a_base64_y_guardar_txt(ruta_imagen)
