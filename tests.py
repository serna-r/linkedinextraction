
import re

def hex_to_ascii(match):
    # Extraer la cadena hexadecimal dentro de $HEX[]
    hex_str = match.group(1)
    # Convertir la cadena hexadecimal a bytes
    bytes_obj = bytes.fromhex(hex_str)
    # Convertir los bytes a una cadena ASCII
    ascii_str = bytes_obj.decode('ascii', errors='ignore')
    return ascii_str

def replace_hex_strings(text):
    # Expresión regular para detectar el formato $HEX[3132333435360000]
    hex_pattern = re.compile(r'\$HEX\[([0-9A-Fa-f]+)\]')
    # Reemplazar todas las coincidencias en el texto
    return hex_pattern.sub(hex_to_ascii, text)

# Ejemplo de uso
text = "Esto es un ejemplo: $HEX[3132333435360000] y otro $HEX[48656c6c6f21]"
result = replace_hex_strings(text)
print(result)