def abrirArchivo():
    nuevaLista= []
    contraseñasGuardadas = open('segundoEjercicio/input.txt', 'r')
    line = contraseñasGuardadas.readlines()

    #Ciclo para convertir el archivo txt en vector
    for i in line:
        valor = i.split()
        rango= valor[0].split("-")
        caracterPolitica=valor[1].replace(":", "")
        contraseña=valor[2]
        nuevaLista.append([rango,caracterPolitica,contraseña])
        
    contraseñasGuardadas.close() 
    return nuevaLista

def evaluarContraseña(listaContraseñas):
    contadorValidas = 0
    contadorInvalidas = 0
    for i in listaContraseñas:
        #identificando los argumentos numericos de la politica de la contraseña
        minimo = int(i[0][0]) 
        maximo = int(i[0][1]) 
        caracterPolitica = i[1] #identifica caracter de la politica de la contraseña
        repeticiones = i[2].count(caracterPolitica) #identifica repeticion de el caracter de la politica en contraseña
        if repeticiones>=minimo and repeticiones<=maximo:
            contadorValidas+=1
        else:
            contadorInvalidas+=1
    return f'Numero de contraseñas validas: {contadorValidas} \nNumero de contraseñas invalidas: {contadorInvalidas}'

  
print(evaluarContraseña(abrirArchivo()))




        
    

    
   

 



