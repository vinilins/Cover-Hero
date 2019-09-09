def movimento_verde(posicao_notas, mult, tamanho):
        new_position = [posicao_notas[0]-(0.52*mult),posicao_notas[1]+mult,posicao_notas[2]+(tamanho*mult),posicao_notas[3]+(tamanho*mult)]
        return new_position

def movimento_vermelho(posicao_notas, mult, tamanho):
        new_position = [posicao_notas[0]-(0.3*mult),posicao_notas[1]+mult,posicao_notas[2]+(tamanho*mult),posicao_notas[3]+(tamanho*mult)]
        return new_position

def movimento_amarelo(posicao_notas, mult, tamanho):
        new_position = [posicao_notas[0]-(0.073*mult),posicao_notas[1]+mult,posicao_notas[2]+(tamanho*mult),posicao_notas[3]+(tamanho*mult)]
        return new_position

def movimento_azul(posicao_notas, mult, tamanho):
        new_position = [posicao_notas[0]+(0.15*mult),posicao_notas[1]+mult,posicao_notas[2]+(tamanho*mult),posicao_notas[3]+(tamanho*mult)]
        return new_position

def movimento_laranja(posicao_notas, mult, tamanho):
        new_position = [posicao_notas[0]+(0.37*mult),posicao_notas[1]+mult,posicao_notas[2]+(tamanho*mult),posicao_notas[3]+(tamanho*mult)]
        return new_position