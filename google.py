import base64
# Cadena codificada en base64
cadena_base64 = "sBAAAAcWdckibwA0qHDnej40ObBAAAAAACAAAAAAAQZgAAAAEAACAAAAAlIq/NHEijc63XldtP"
# Decodificar la cadena
cadena_decodificada = base64.b64decode(cadena_base64)
texto_decodificado = cadena_decodificada.decode('utf-8')
print("Cadena decodificada:", texto_decodificado)
