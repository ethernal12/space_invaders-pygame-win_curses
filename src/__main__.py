import sys
import os

from app.GUI import GUI

# adding directory to python path!
sys.path.append(os.getcwd())

app = GUI(600, 600)
app.init()

while not app.konec():
    app.narisi()
    app.vnos()

