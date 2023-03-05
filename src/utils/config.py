import sys
from dataclasses import dataclass, asdict
import json
from typing import Dict, List, Tuple
from src.utils import pot


@dataclass
class Config:
    # gui atributi
    barve: Dict[str, List[int]]
    gui_velikost: Dict[str, int]
    ime_igralca: str
    naslov_igre: str
    font_type: str
    font_size: int
    meni_ime: str
    default_ime: str
    meni_igraj: str
    meni_config: str
    meni_izhod: str
    theme_color: str
    # vesolje atributi
    pozicija_ladje_x: int
    pozicija_ladje_y: int
    velikost_ladje_x: int
    velikost_ladje_y: int
    hitrost_ladje: int


this = sys.modules[__name__]
this.CONFIG: Config = None
this.path = pot.data("config.json")


def init():
    file = this.path.open("r")
    file_txt = file.read()
    file_dict = json.loads(file_txt)
    this.CONFIG = Config(**file_dict)


def save():
    config_dict = asdict(this.CONFIG)
    file = this.path.open("w")
    file_txt = json.dumps(config_dict)
    file.write(file_txt)
