import sys
import os

from app.GUI import GUI
from src.utils import config

# adding directory to python path!
sys.path.append(os.getcwd())

config.init()
app = GUI(
    config.CONFIG.gui_velikost[0]["gui_width"],
    config.CONFIG.gui_velikost[0]["gui_height"])
app.init()

while not app.konec():
    app.narisi()
    app.vnos()

config.save()
