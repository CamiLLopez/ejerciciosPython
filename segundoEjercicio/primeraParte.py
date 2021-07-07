nuevaLista= []

contraseñasGuardadas = open('segundoEjercicio/input.txt', 'r')
line = contraseñasGuardadas.readlines()

for i in line:
    valor = i.split()
    rango= valor[0].split("-")
    clave=valor[1].replace(":", "")
    contraseña=valor[2]
    nuevaLista.append([rango,clave,contraseña])
    
contraseñasGuardadas.close() 

def evaluarContraseña(listaContraseñas):
    contadorValidas = 0
    contadorInvalidas = 0
    for i in listaContraseñas:
        minimo = i[0][0]
        maximo = i[0][1]
        clave = i[1]
        repeticiones = i[2].count(clave)
        if repeticiones>=int(minimo) and repeticiones<=int(maximo):
            contadorValidas+=1
        else:
            contadorInvalidas+=1
    return f'Numero de contraseñas validas: {contadorValidas} \nNumero de contraseñas invalidas: {contadorInvalidas}'
  
print(evaluarContraseña(nuevaLista))




        
    

    
   

 



