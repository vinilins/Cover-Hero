#cordenadas iniciais
tamanho_x = tamanho_y = 40
verde_y = vermelho_y = amarelo_y = azul_y = laranja_y = 295
verde_x = 555
vermelho_x = 590
amarelo_x = 625
azul_x = 660
laranja_x = 695

#recebe uma lista com listas indicando a cor e o tempo de aparição ex: [['verde', 3.4],['vermelho',5.5]]
def criar_objetos(lista_notas):
    lista_objetos=[]
    for e in lista_notas:
        if e[0] == 'verde':
            nota = Notas(verde_x, verde_y, tamanho_x, tamanho_y,'verde',  e[1])
        elif e[0] == 'vermelho':
            nota = Notas(vermelho_x, vermelho_y, tamanho_x, tamanho_y,'vermelho', e[1])
        elif e[0] == 'amarelo':
            nota = Notas(amarelo_x, amarelo_y, tamanho_x, tamanho_y,'amarelo',  e[1])
        elif e[0] == 'azul':
            nota = Notas(azul_x, azul_y, tamanho_x, tamanho_y,'azul',  e[1])
        elif e[0] == 'laranja':
            nota = Notas(laranja_x, laranja_y, tamanho_x, tamanho_y,'laranja',  e[1])
        lista_objetos.append(nota)
    return lista_objetos

#classe para criar os objetos
class Notas():
    def __init__(self, cord_x, cord_y, tamanho_x, tamanho_y, cor, time):
        self.cor = cor
        self.time = time
        self.atributos = [cord_x, cord_y, tamanho_x, tamanho_y]
        self.acerto = False
