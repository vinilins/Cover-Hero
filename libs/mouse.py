def movimento_verde(posicao_notas):
        mult = 2
        new_position = [posicao_notas[0]-(0.28*mult),posicao_notas[1]+mult,posicao_notas[2]+(0.081*mult),posicao_notas[3]+(0.054*mult)]
        return new_position

def movimento_vermelho(posicao_notas):
        mult = 2
        new_position = [posicao_notas[0]-(0.12*mult),posicao_notas[1]+mult,posicao_notas[2]+(0.081*mult),posicao_notas[3]+(0.054*mult)]
        return new_position

def movimento_amarelo(posicao_notas):
        mult = 2
        new_position = [posicao_notas[0]+(0.04*mult),posicao_notas[1]+mult,posicao_notas[2]+(0.081*mult),posicao_notas[3]+(0.054*mult)]
        return new_position

def movimento_azul(posicao_notas):
        mult = 2
        new_position = [posicao_notas[0]+(0.18*mult),posicao_notas[1]+mult,posicao_notas[2]+(0.081*mult),posicao_notas[3]+(0.054*mult)]
        return new_position


def click_botao_iniciar(mouse_pos, mouse_pressed):
        if 50+170 > mouse_pos[0] > 50 and 214+31 > mouse_pos[1] > 214 and mouse_pressed[0]==1:
                return True
                
        return False

def sobre_botao_iniciar(mouse_pos):
        if 50+170 > mouse_pos[0] > 50 and 214+31 > mouse_pos[1] > 214:
                return True
        return False

def sobre_botao_preferencia(mouse_pos):
        if 46+176 > mouse_pos[0] > 46 and 273+32 > mouse_pos[1] > 273:
                return True
        return Falses