nuevaLista= []

contraseñasGuardadas = open('segundoEjercicio/input.txt', 'r')
line = contraseñasGuardadas.readlines()

for i in line:
    valor = i.split()
    posiciones= valor[0].split("-")
    clave=valor[1].replace(":", "")
    contraseña=valor[2]
    nuevaLista.append([posiciones,clave,contraseña])

contraseñasGuardadas.close() 

def evaluarContraseña(listaContraseñas):
    contadorValidas = 0
    contadorInvalidas = 0
    for i in listaContraseñas:
        primeraPosicion = int(i[0][0]) 
        segundaPosicion = int(i[0][1]) 
        clave = i[1]
        contraseña = i[-1]
        if (contraseña[primeraPosicion-1]==clave) and (contraseña[segundaPosicion-1]==clave):
            contadorInvalidas+=1
        elif (contraseña[primeraPosicion-1]==clave) or (contraseña[segundaPosicion-1]==clave):
            contadorValidas+=1
        else:
            contadorInvalidas+=1
            
    return f'Numero de contraseñas validas: {contadorValidas} \nNumero de contraseñas invalidas: {contadorInvalidas}'
  
print(evaluarContraseña(nuevaLista))



        
    

    
   

 



