import time
import pyxhook
ini = time.time()

arquivo = open('musica.txt', 'w')
c=0
def OnKeyPress(event):
    x = str(event.Key)
    t = time.time()-ini
    arquivo.write(x+'-->'+str(t)+'\n')
    if event.Ascii == 32:
        arquivo.close()
        exit(0)
hm = pyxhook.HookManager()
hm.KeyDown = OnKeyPress
hm.HookKeyboard()
hm.start()
