import redis

r = redis.Redis()

opcion = -1
while opcion != 0:
  print('========= MENU ========')
  print('[1] Mostrar')
  print('[2] Agregar')
  print('[3] Actualizar')
  print('[4] Eliminar')
  print('[5] Buscar')
  print('[0] Salir')
  opcion = int(input('Opcion: '))

  if opcion == 1:
    lista = [i for i in r.keys()]
    if len(lista) == 0:
      print('No hay palabras!')
    else:
      for i in lista:
        print('-'*30)
        print(f'Nombre: {i.decode("UTF-8")}\nSignificado: {r.get(i).decode("UTF-8")}')
    
  elif opcion == 2:
    r.set(
      input('Nombre: ').lower(),
      input('Significado: ').lower()
      )
    print('Palabra agregada!')

  elif opcion == 3:
    nombre = input('Ingrese el nombre de la palabra: ').lower()
    palabra = r.get(nombre)
    if palabra:
      significado = input('Ingrese el nuevo significado: ')
      r.set(nombre,significado)
      print('Palabra actualizada!')
    else:
      print('La palabra no existe!')
  
  elif opcion == 4:
    nombre = input('Ingrese el nombre de la palabra: ').lower()
    palabra = r.get(nombre)
    if palabra:
      r.delete(nombre)
      print('Palabra eliminada!')
    else:
      print('La palabra no existe!')
  
  elif opcion == 5:
    nombre = input('Ingrese el nombre de la palabra: ').lower()
    palabra = r.get(nombre)
    if palabra:
      print(f'Nombre: {nombre}\nSignificado: {palabra.decode("UTF-8")}')
    else:
      print('La palabra no existe!')