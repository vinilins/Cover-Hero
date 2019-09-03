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