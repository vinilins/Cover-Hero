def notas():
    lista_notas=[]
    f = open("./musicas/musica.txt", "r")
    for x in f:
        l = []
        j = x.split('-->')
        if j[0] == 'a':
            l.append('verde')
        elif j[0] == 's':
            l.append('vermelho')
        elif j[0] == 'j':
            l.append('amarelo')
        elif j[0] == 'k':
            l.append('azul')
        l.append(float(j[1]))
        if len(l) == 2:
            lista_notas.append(l)
    f.close()
    return lista_notas
