import sys
import os

# adding directory to python path!
sys.path.append(os.getcwd())

from src.app.GUI import GUI
from src.settings import config as S

S.init()
app = GUI(
    S.CONFIG.pygame.dimenzija.sirina,
    S.CONFIG.pygame.dimenzija.visina
)
app.init()

while not app.konec():
    app.narisi()
    app.vnos()
S.save()
