def acertou_nota(nota, cont):
        if nota.atributos[1] in range(550,620) and nota.acerto==False and nota.cor=='verde':
                print("verde")
                nota.acerto = True
                cont+=1
                print(cont)
                return cont
        elif nota.atributos[1] in range(550,620) and nota.acerto==False and nota.cor=='vermelho':
                print("vermelho")
                nota.acerto = True
                cont+=1
                print(cont)
                return cont
        elif nota.atributos[1] in range(550,620) and nota.acerto==False and nota.cor=='amarelo':
                print("amarelo")
                nota.acerto = True
                cont+=1
                print(cont)
                return cont
        elif nota.atributos[1] in range(550,620) and nota.acerto==False and nota.cor=='azul':
                print("azul")
                nota.acerto = True
                cont+=1
                print(cont)
                return cont
        # elif tupla_pos2[1] in range(260,300):
        #         print("circulo2")
        #         cont+=1
        #         return cont
        # elif tupla_pos3[1] in range(260,300):
        #         print("circulo3")
        #         cont+=1
        #         return cont
        # elif tupla_pos4[1] in range(260,300):
        #         print("circulo4")
        #         cont+=1
        return cont