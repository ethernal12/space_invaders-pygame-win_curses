import sys
import os

from app.GUI import GUI

# adding directory to python path!
sys.path.append(os.getcwd())

app = GUI(500, 500)
app.inicializacija_igre()

running = True
while running:
    app.input_igralca()
    app.narisi_igro()
