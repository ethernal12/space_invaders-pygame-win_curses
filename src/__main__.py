import sys
import os

from app.GUI import GUI

# adding directory to python path!
sys.path.append(os.getcwd())
running = True
while running:
    app = GUI(800, 800)
    app.inicializacija_igre()
    app.input_igralca()
    app.narisi_igro()