def abrirArchivo():
    nuevaLista= []
    passwordsGuardadas = open('segundoEjercicio/input.txt', 'r')
    line = passwordsGuardadas.readlines()
    #Ciclo para convertir en vector al archivo txt 
    for i in line:
        valor = i.split()   
        posiciones= valor[0].split("-")
        clave=valor[1].replace(":", "")
        password=valor[2]
        nuevaLista.append([posiciones,clave,password])

    passwordsGuardadas.close()
    return nuevaLista 

def evaluarPassword(listaPasswords):
    contadorValidas = 0
    contadorInvalidas = 0
    for i in listaPasswords:
        #identificando el valor de las posiciones de la politica de password
        primeraPosicion = int(i[0][0]) 
        segundaPosicion = int(i[0][1]) 
        caracterPolitica = i[1] 
        password = i[-1]
        if (password[primeraPosicion-1]==caracterPolitica) and (password[segundaPosicion-1]==caracterPolitica):
            contadorInvalidas+=1
        elif (password[primeraPosicion-1]==caracterPolitica) or (password[segundaPosicion-1]==caracterPolitica):
            contadorValidas+=1
        else:
            contadorInvalidas+=1
            
    return f'Numero de contraseñas validas: {contadorValidas} \nNumero de contraseñas invalidas: {contadorInvalidas}' 
  
print(evaluarPassword(abrirArchivo()))




    
   

 



