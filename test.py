print('hola')
lista = [1,2,3,4]

def filtrar_pares(list):
    final = []
    for item in list:
        if item%2==0:
            final.append(item)
    return final
            