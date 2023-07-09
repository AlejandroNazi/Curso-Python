    # Operadores aritmeticos; suma, resta, multp., division
print(7 + 3)
print(7 - 3)
print(7 * 3)
print(7 / 3)    #-El resultado es un Float; ¨1.5¨
print(7 % 3)
print(7 ** 3)   #-Expoentes

print(7 // 3)   #-El resultado es un Int; ¨1¨

#LOS OPERADORES TAMBIEN FUNCIONAN CON STRINGS:

print('Hola '+ 'Mundo')
print('Adiós ' * 5)     #-Los operadores también funcionan con strings
print('Bienvenido ' + str('10'))    #-Los operadores pueden escribirse como strings con: str ó ''
print('Bienvenido ' + '10')

    #Operadores Comparativos: Booleanos
print(4 < 8 )
print(4 > 8 )
print( 4 == 4) #-Un ¨=¨significaría asignar un valor. Dos ¨==¨ significa pregunta.
print(4 >= 8 )
print(4 <= 8 )
print(8 != 8 )

    #Comparativos con strings
print('hola' > 'mundo') #-Esto cuenta la poscición de la primer letra en el abecedario
print(len('hola') > len('mundo')) #- Con la función ¨Len¨ se cuenta la cantidad de caracteres
print(len('hola') < len('mundo'))
print(len('hola') == len('mundo'))
print(len('hola') != len('mundo'))
print(len('a') > len('b')) #False
print(len('a') > len('bb')) #False
print(len('B') > len('a'))

    #Operadores Lógicos
print(False and True) #and      #En and; solo será True sí todos los operadores son True.
print(False or False)  #or      #En or; solo será False sí todos los operadores son False.
print(not(False or False) )  #not       #En not; el resultado de or o and se vuelve lo contrario

print((not(7 != 7) and 6 > 5 ) and ('rozar' < 'rotar' or not ( 3 == 5)))
print(True and True)

la_contraseña_es= '905421'
print('Contraseña: ', (la_contraseña_es == la_contraseña_es))
print
    