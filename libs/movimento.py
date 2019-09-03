mult = 7
def movimento_verde(posicao_notas):
        new_position = [posicao_notas[0]-(0.27*mult),posicao_notas[1]+mult,posicao_notas[2]+(0.081*mult),posicao_notas[3]+(0.054*mult)]
        return new_position

def movimento_vermelho(posicao_notas):
        new_position = [posicao_notas[0]-(0.1*mult),posicao_notas[1]+mult,posicao_notas[2]+(0.081*mult),posicao_notas[3]+(0.054*mult)]
        return new_position

def movimento_amarelo(posicao_notas):
        new_position = [posicao_notas[0]+(0.055*mult),posicao_notas[1]+mult,posicao_notas[2]+(0.081*mult),posicao_notas[3]+(0.054*mult)]
        return new_position

def movimento_azul(posicao_notas):
        new_position = [posicao_notas[0]+(0.2*mult),posicao_notas[1]+mult,posicao_notas[2]+(0.081*mult),posicao_notas[3]+(0.054*mult)]
        return new_position
