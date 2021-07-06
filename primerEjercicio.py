def generarLista():
    acumulador = []
    for i in range(1,100):
        if(divisible(i,3) and divisible(i,5)):
            acumulador.append('cyberclick')
        elif(divisible(i,3)):
            acumulador.append('cyber')
        elif(divisible(i,5)):
            acumulador.append('click')
        else:
            acumulador.append(i)

    return acumulador

def divisible(i,num):
    return i%num==0


print(generarLista())
        