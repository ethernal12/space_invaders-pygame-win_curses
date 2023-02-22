import sys
import os

from app.GUI import GUI

# adding directory to python path!
sys.path.append(os.getcwd())

app = GUI(700, 700)
app.inicializacija_igre()

running = True
while running:
    app.narisi_igro()
    app.input_igralca()

