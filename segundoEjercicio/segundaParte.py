def abrirArchivo():
    nuevaLista= []
    contraseñasGuardadas = open('segundoEjercicio/input.txt', 'r')
    line = contraseñasGuardadas.readlines()
    #Ciclo para convertir en vector al archivo txt 
    for i in line:
        valor = i.split()   
        posiciones= valor[0].split("-")
        clave=valor[1].replace(":", "")
        contraseña=valor[2]
        nuevaLista.append([posiciones,clave,contraseña])

    contraseñasGuardadas.close()
    return nuevaLista 

def evaluarContraseña(listaContraseñas):
    contadorValidas = 0
    contadorInvalidas = 0
    for i in listaContraseñas:
        #identificando el valor de las posiciones de la politica de contraseña
        primeraPosicion = int(i[0][0]) 
        segundaPosicion = int(i[0][1]) 
        caracterPolitica = i[1] 
        contraseña = i[-1]
        if (contraseña[primeraPosicion-1]==caracterPolitica) and (contraseña[segundaPosicion-1]==caracterPolitica):
            contadorInvalidas+=1
        elif (contraseña[primeraPosicion-1]==caracterPolitica) or (contraseña[segundaPosicion-1]==caracterPolitica):
            contadorValidas+=1
        else:
            contadorInvalidas+=1
            
    return f'Numero de contraseñas validas: {contadorValidas} \nNumero de contraseñas invalidas: {contadorInvalidas}'
  
print(evaluarContraseña(abrirArchivo()))




    
   

 



