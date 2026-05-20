"""
====================================================================
SISTEMA DE GESTIÓN DE PRÉSTAMO DE LAPTOPS (RESO-LAP)
====================================================================
Descripción: Aplicación backend en Django para el control, 
             asignación y devolución de laptops.
Organización: ESTUDIO DAFARO
Contacto:     EstudioDafaro@techedu.sv | +503 2301-0000
Año de Creación: 2026
País: El Salvador

Licencia: Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional 
          (CC BY-NC-ND 4.0)
© 2026 Estudio Dafaro. Algunos derechos reservados.

Usted es libre de: Compartir y utilizar este software bajo las siguientes condiciones:
  - Atribución: Debe dar crédito a Estudio Dafaro.
  - No Comercial: No puede utilizar este material con fines comerciales.
  - Sin Derivadas: Si remezcla, transforma o crea a partir del material, 
    no puede distribuir el material modificado.

Para ver una copia de esta licencia, visita: http://creativecommons.org/licenses/by-nc-nd/4.0/
====================================================================
"""

"""
Script para generar imágenes placeholder de los integrantes.
Ejecutar: python generate_avatar_images.py
Ubicación: Raíz del proyecto (junto a manage.py)
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Datos de los integrantes
integrantes_data = [
    {'first_name': 'Daniel', 'last_name': 'Pozo', 'filename': 'daniel_pozo.jpg', 'color': '#E69894'},
    {'first_name': 'Karla', 'last_name': 'Pineda', 'filename': 'karla_pineda.jpg', 'color': '#C9627D'},
    {'first_name': 'Ana', 'last_name': 'Villeda', 'filename': 'ana_villeda.jpg', 'color': '#A85B6B'},
    {'first_name': 'Fabio', 'last_name': 'de la Cruz', 'filename': 'fabio_de.jpg', 'color': '#8B4F59'},
    {'first_name': 'Samuel', 'last_name': 'Ventura', 'filename': 'samuel_ventura.jpg', 'color': '#791F1B'},
    {'first_name': 'Diego', 'last_name': 'Escobar', 'filename': 'diego_escobar.jpg', 'color': '#6B1B17'},
    {'first_name': 'Ervin', 'last_name': 'Durán', 'filename': 'ervin_duran.jpg', 'color': '#5D1713'},
    {'first_name': 'William', 'last_name': 'Deras', 'filename': 'william_deras.jpg', 'color': '#4F130F'},
]

# Carpeta de destino
output_dir = os.path.join('static', 'img', 'integrantes')
os.makedirs(output_dir, exist_ok=True)

def hex_to_rgb(hex_color):
    """Convierte color hex a RGB"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def generate_avatar(first_name, last_name, filename, color_hex):
    """Genera una imagen de avatar con las iniciales"""
    
    # Dimensiones de la imagen
    width, height = 500, 500
    
    # Crear imagen con fondo degradado
    img = Image.new('RGB', (width, height), hex_to_rgb(color_hex))
    draw = ImageDraw.Draw(img)
    
    # Crear un círculo blanco en el centro para las iniciales
    circle_center_x, circle_center_y = width // 2, height // 2
    circle_radius = 120
    
    # Dibujar círculo blanco
    draw.ellipse(
        [circle_center_x - circle_radius, circle_center_y - circle_radius,
         circle_center_x + circle_radius, circle_center_y + circle_radius],
        fill=(255, 255, 255)
    )
    
    # Texto: iniciales
    initials = (first_name[0] + last_name[0]).upper()
    
    # Intentar usar una fuente mejor, si no existe usar la por defecto
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
    except:
        font = ImageFont.load_default()
    
    # Obtener dimensiones del texto para centrarlo
    bbox = draw.textbbox((0, 0), initials, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    # Dibujar iniciales
    text_x = circle_center_x - text_width // 2
    text_y = circle_center_y - text_height // 2
    
    draw.text((text_x, text_y), initials, fill=hex_to_rgb(color_hex), font=font)
    
    # Guardar imagen
    filepath = os.path.join(output_dir, filename)
    img.save(filepath, quality=95)
    print(f"✓ Generado: {filename}")

# Generar todas las imágenes
print("Generando imágenes placeholder de integrantes...")
print(f"Carpeta destino: {output_dir}\n")

for data in integrantes_data:
    generate_avatar(
        data['first_name'],
        data['last_name'],
        data['filename'],
        data['color']
    )

print(f"\n✓ {len(integrantes_data)} imágenes generadas exitosamente.")
print(f"Ubicación: {os.path.abspath(output_dir)}")
