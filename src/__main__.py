import os
import sys

# adding directory to python path!
sys.path.append(os.getcwd())

from src.app.gui import Gui
from src.settings import config as S

S.init()
app = Gui()
app.init()

while not app.konec():
	app.narisi()
	app.vnos()
	app.pocakaj()
S.save()
