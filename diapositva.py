precioUSD = [10, 30, 25, 8, 23, 89, 2, 52]
notas = ['Adriana', [4.8, 3.1, 2.9, 4.8]]
print("Primer elemento de la lista anidada: ", notas[1][0])
print("\n Lista original: \t", precioUSD); print("Primer elemento:\t", precioUSD[0])
print("Ultimo elemento:\t ", precioUSD[-1]);
print("Pos. pares entre 0 y 2:\t", precioUSD[0:5:2])
print("Lista invertida:\t", precioUSD[::-1])
precioUSD[2] = precioUSD[2] + 500
print("Eliminado pos 2 cambiada: \t", precioUSD)
precioUSD.remove(89)
print("Eliminado coincide 89:\t", precioUSD)
del precioUSD[-2]; print("Eliminado el penultimo:\t", precioUSD)
precioUSD.append(69.5); print("Agregando elementos:\t", precioUSD)
precioUSD.extend([24, 18, 41]); print("Extendiendo elementos:\t", precioUSD)
precioUSD.insert(2, 43); print("Insertando elemento:\t", precioUSD)
del precioUSD[1:3]
print("Eliminando elementos:\t", precioUSD)
print("525 esta en la pos:\t", precioUSD.index(525))
precioUSD.sort(); print("Lista Ordenada: \t", precioUSD)
precioUSD.sort(reverse = True); print("Orden Inverso:\t \t", precioUSD)

print("Retorna lista Ordenada:\t", sorted(precioUSD))
