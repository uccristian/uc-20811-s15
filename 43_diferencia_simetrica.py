# La diferencia simétrica muestra los elementos que están en uno u otro conjunto, 
# pero no en los dos a la vez. 
# En otras palabras, excluye los elementos que tienen en común.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

resultado = A.symmetric_difference(B)
print(resultado)
