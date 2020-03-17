def maior(a,b):
    """
      Retorna o maior valor entre a e b
      @author: Lorena Gomes de O. Cabral
      """
    if a>b:
        x = a
    else:
        x = b
    return x

def soma(lista,x=0):
    """
        Retorna o somatório dos valores passados pela lista
        @author: Lorena Gomes de O. Cabral
    """
    resultado = x
    for elementos in lista:
        resultado += elementos
    return resultado

def media(lista):
    """
        Retorna a média dos valores passados pela lista
        @author: Lorena Gomes de O. Cabral
    """
    media = 0
    num_elementos = 0
    resultado = 0
    for elementos in lista:
        media += elementos
        num_elementos += 1
    resultado = (media/num_elementos)
    return resultado

def valores_iguais(lista1, lista2):
    """
        Retorna uma lista contendo os valores iguais entre as duas listas passadas como parâmetro
        @author: Lorena Gomes de O. Cabral
    """
    lista = []
    for elementos1 in lista1:
            if elementos1 in lista2:
                lista.append(elementos1)

    return lista

def indice_prim_valor_igual(lista1,lista2):
    """
        Retorna a posição da lista1 do primeiro valor igual ao da lista2
        @author: Lorena Gomes de O. Cabral
    """

    for i in range(len(lista1)):
        if lista1[i] in lista2:
            return i

if __name__ == "__main__":

    a = maior(5,3)
    print("Maior número entre a e b: "+str(a))

    b = soma([2,2])
    print("Somatório lista: "+str(b))

    c = media([50,50,50,50])
    print("Media da lista: "+str(c))

    d = []
    d = valores_iguais([1,2,3,4],[1,2,3,5,8,6])
    print("Valores em comum nas duas lista: "+str(d))

    e = indice_prim_valor_igual([18,25,2,4],[1,2,3,5,8,6])
    print("Indice primeiro valor na lista1 comum ao da lista2: " +str(e))
