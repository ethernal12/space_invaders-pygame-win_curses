import sys
import os

from app.GUI import GUI
from src.settings import config as S

# adding directory to python path!
sys.path.append(os.getcwd())

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
