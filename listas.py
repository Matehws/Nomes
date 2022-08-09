import re
def adicionar_elemento(lista: list, elemento: str) -> bool:
    x = bool(re.findall('[A-Z]+[a-z]+$', elemento)) #tested and working
    if x == True:
        lista.append(elemento)
        print(lista)
        return True
    else:
        return False


def buscar_elemento(lista: list, elemento: str) -> bool:
    if elemento in lista: #tested and working
        return True
    else:
        return False

def remover_elemento(lista: list, elemento: str) -> bool:
    if elemento in lista: #tested and working
        lista.remove(elemento)
        return True
    else:
        return False

def limpar_lista(lista: list) -> None:
    lista.clear() #tested and working



def ordenar_lista(lista: list) -> None:
    lista.sort() #tested and working
    
    


def pegar_quantidade(lista: list) -> int:
    return len(lista) #tested and working


def converter_maiusculo(lista: list) -> list:
    lista = [maiusculo.upper() for maiusculo in lista] #tested and working
    return lista

def eliminar_repetidos(lista: list) -> list:
    new_lista = list(dict.fromkeys(lista))
    return new_lista