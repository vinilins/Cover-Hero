def acertou_nota(nota, cont):
        if nota.atributos[1] in range(550,620) and nota.acerto==False and nota.cor=='verde':
                print("verde")
                nota.acerto = True
                new_contador = cont + 1
                print(new_contador)
                return new_contador
        elif nota.atributos[1] in range(550,620) and nota.acerto==False and nota.cor=='vermelho':
                print("vermelho")
                nota.acerto = True
                new_contador = cont + 1
                print(new_contador)
                return new_contador
        elif nota.atributos[1] in range(550,620) and nota.acerto==False and nota.cor=='amarelo':
                print("amarelo")
                nota.acerto = True
                new_contador = cont + 1
                print(new_contador)
                return new_contador
        elif nota.atributos[1] in range(550,620) and nota.acerto==False and nota.cor=='azul':
                print("azul")
                nota.acerto = True
                new_contador = cont + 1
                print(new_contador)
                return new_contador
        return cont