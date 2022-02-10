
# Convertir el patrón de colores en un número entero
def color_list_to_int(color_list):
    return sum(color.value * (3**idx) for idx, color in enumerate(color_list))

# Función caché dado un Answer
def cached(func):

    cache = func.cache = {}

    def memorised_func(*args):

        key = color_list_to_int(args[1].colors)

        # Si el valor no está calculado, lo calculo
        if key not in cache:
            cache[key] = func(*args)

        # Si sí está calculado, lo devuelvo
        return cache[key]

    memorised_func.cache_reset = lambda: func.cache.clear()
    return memorised_func
