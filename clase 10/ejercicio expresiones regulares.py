import re

tema ={
        'title': 'QUEVEDO || BZRP Music Sessions #52',
        'views': 227192970,
        'length': 204,
        'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg',
        'url': 'https://youtube.com/watch?v=A_g3lMcWVy0',
        'date': '2022-07-06 00:00:00'
}

# Tipo : BZRP MUSIC SESSIONS
# Artista: QUEVEDO
# Numero: 52
# Reproducciones: 227 M
# Duración: 204 segundos
# Codigo: A_g3lMcWVy0
# Fecha de carga:6/7/2022
# Hora de carga: 00:00

tipo = re.findall(r"B[a-zA-Z\s]+", tema['title'])
print(f"Tipo: {tipo[0]}")

artist = re.findall(r"Q[a-zA-Z]+", tema['title'])
print(f"Artista: {artist[0]}")

number = re.findall(r"\d{2}", tema['title'])
print(f"Numero: {number[0]}")


cast_views = str(tema['views'])
views = re.sub(r"\d{6}$", " M", cast_views)
print(f"Reproducciones: {views}")

cast_lenght = str(tema['length'])
print(f"Duración: {cast_lenght} segundos")

img_url = re.findall(r"\w+", tema['img_url'])
print(f"Codigo: {img_url[5]}")


# fecha = re.sub(r"[-", "/", tema['date'])
fecha_hora = re.findall(r"\d{1,4}", tema['date'])
print(f"Fecha de carga: {fecha_hora[2]}/{fecha_hora[1]}/{fecha_hora[0]}")
print(f"Hora de carga: {fecha_hora[3]}:{fecha_hora[4]}")
# mes = re.findall(r"")
# print(fecha)