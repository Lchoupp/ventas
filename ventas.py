"""
Programa: ventas.py
Proyecto: CaféCode · sistema de la tostadora de café
Autor: TU NOMBRE AQUÍ · Ficha 3601599
Fecha: AAAA-MM-DD
Versión: 0.2
Descripción: TU DESCRIPCIÓN AQUÍ (2 o 3 líneas: qué hace este programa)
"""

# =====================================================================
# TALLER 1 · CaféCode v0.2 · Módulo de ventas
# Lee el enunciado completo antes de empezar. Trabaja parte por parte y
# ejecuta el archivo después de cada una: python ventas.py
# Borra cada comentario «# TU CÓDIGO AQUÍ» cuando lo hayas resuelto.
# =====================================================================

# ---------------------------------------------------------------------
# PARTE A · CONSTANTES (valores fijos del negocio, en MAYÚSCULAS)
# Ya tienes tres. Define las que faltan con el valor indicado:
#   PORCENTAJE_DESCUENTO  -> 5 %  (escríbelo como decimal: 0.05)
#   GRAMOS_POR_LIBRA      -> 500  (la libra comercial en Colombia)
#   GRAMOS_POR_KILO       -> 1000
#   GRAMOS_POR_BOLSA      -> 250
#   ANCHO_RECIBO          -> 40   (caracteres de ancho del recibo)
# Agrega un comentario corto al lado de cada constante que lo necesite.
# ---------------------------------------------------------------------
NOMBRE_TOSTADORA = "CaféCode · Tostadora de Café"
PRECIO_LIBRA_ESPECIAL = 38000     # pesos por libra de café especial
PRECIO_LIBRA_TRADICIONAL = 26000  # pesos por libra de café tradicional

PORCENTAJE_DESCUENTO = 0.05       #porcentaje de descuento del produxcto
GRAMOS_POR_LIBRA = 500            #cantidad de gramos por libra
GRAMOS_POR_KILO = 1000            #cantidad de gramos por kilo
GRAMOS_POR_BOLSA =  250           #cantidad de gramos por bolsa
ANCHO_RECIBO = 40                 #diametro en ancho del recibo
# ---------------------------------------------------------------------
# PARTE B · ENTRADA DE DATOS
# Pide con input():
#   1. el nombre del cliente           -> nombre_cliente
#   2. las libras de café especial     -> libras_especial (float)
#   3. las libras de café tradicional  -> libras_tradicional (float)
# Recuerda: input() SIEMPRE devuelve texto. Conviértelo con float().
# Pista: el usuario puede escribir 2,5 (con coma). Usa
#        .replace(",", ".") antes de convertir. Mira el ejemplo:
#        texto = input("Libras: ")
#        libras = float(texto.replace(",", "."))
# ---------------------------------------------------------------------
# nombre_cliente = input("nombre: ")
texto_especial = input("Libras de café especial: ")
libras_especial = float(texto_especial.replace(",", "."))
texto_tradicional = input("Libras de café tradicional: ")
libras_tradicional = float(texto_tradicional.replace(",", "."))
# ---------------------------------------------------------------------
# PARTE C · PROCESO (solo cálculos, nada de print aquí)
# Calcula y guarda en variables con nombres claros:
#   subtotal_especial    = libras de especial × precio del especial
#   subtotal_tradicional = libras de tradicional × precio tradicional
#   subtotal             = suma de los dos subtotales
#   descuento            = subtotal × porcentaje de descuento
#   total                = subtotal − descuento
#   total_libras         = libras especial + libras tradicional
#   total_gramos         = total_libras × gramos por libra
# Usa SIEMPRE las constantes, nunca escribas 38000 o 0.05 aquí.
# ---------------------------------------------------------------------
# 
subtotal_especial = libras_de_especial * PRECIO_LIBRA_ESPECIAL
subtotal_tradicional = libras_de_tradicional * PRECIO_LIBRA_TRADICIONAL
subtotal = suma_de_los_subtotales
descuento = subtotal * porcentaje_de_descuento
total


# ---------------------------------------------------------------------
# PARTE D · SALIDA: RECIBO
# Primero prepara los textos con formato (una variable por valor):
#        especial_txt = f"${subtotal_especial:,.0f}".replace(",", ".")
#        lb_especial_txt = f"{libras_especial:.1f}".replace(".", ",")
# Haz lo mismo para: tradicional_txt, subtotal_txt, descuento_txt
# (empieza con "-$"), total_txt, lb_tradicional_txt, lb_total_txt y
# gramos_txt. Para la etiqueta del descuento usa una variable:
#        etiqueta_descuento = "Descuento (5 %)"
#
# Después imprime el recibo. Hay tres tipos de fila; ya tienes un
# ejemplo resuelto de cada uno. Copia el patrón para las demás filas:
#   Fila de producto: 3 columnas de 18 + 8 + 14 = 40 caracteres
#        print(f"{'Café especial':<18}{lb_especial_txt:>8}{especial_txt:>14}")
#   Fila de total: 2 columnas de 26 + 14 = 40 caracteres
#        print(f"{'TOTAL A PAGAR':<26}{total_txt:>14}")
#   Fila de total con etiqueta guardada en una variable:
#        print(f"{etiqueta_descuento:<26}{descuento_txt:>14}")
# ---------------------------------------------------------------------
# print()
# print("=" * ANCHO_RECIBO)
# print(f"{NOMBRE_TOSTADORA:^{ANCHO_RECIBO}}")
# print("=" * ANCHO_RECIBO)
# print(f"Cliente: {nombre_cliente}")
# (Quita el # de las 5 líneas anteriores cuando tengas las Partes A y B)
# TU CÓDIGO AQUÍ


# ---------------------------------------------------------------------
# PARTE E · RETO: EMPAQUE DE UN LOTE EN BOLSAS DE 250 g
# 1. Pide los kilos de café tostado de un lote (acepta coma decimal).
# 2. Convierte los kilos a gramos con la constante GRAMOS_POR_KILO.
#    Usa round() sobre el resultado: 8.11 * 1000 da 8109.999...
# 3. Calcula con // cuántas bolsas de 250 g se llenan completas.
# 4. Calcula con % cuántos gramos sobran.
# 5. Muestra los dos resultados con f-strings.
# ---------------------------------------------------------------------
# TU CÓDIGO AQUÍ
