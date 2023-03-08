import sys
from dataclasses import dataclass, asdict
import json

from src.settings.app import App
from src.utils import pot
from src.settings.jeziki import Jezik


@dataclass
class IgralecConfig:
    ime: str


@dataclass
class FontConfig:
    ime: str
    velikost: int


@dataclass
class DimenzijaConfig:
    sirina: int
    visina: int


@dataclass
class FontConfig:
    velikost: int
    tip: str


@dataclass
class BarveConfig:
    rdeca: list[int]
    bela: list[int]
    crna: list[int]

@dataclass
class JezikConfig:
    jezik: str


@dataclass
class PyGameConfig:
    dimenzija: DimenzijaConfig
    barve: BarveConfig
    dimenzije: list[DimenzijaConfig]
    font: FontConfig
    izbira_jezika: list[JezikConfig]

    def __post_init__(self):
        self.dimenzija = DimenzijaConfig(**self.dimenzija)
        self.font = FontConfig(**self.font)
        self.barve = BarveConfig(**self.barve)
        for i in range(len(self.dimenzije)):
            self.dimenzije[i] = DimenzijaConfig(**self.dimenzije[i])
        for i in range(len(self.izbira_jezika)):
            self.izbira_jezika[i] = JezikConfig(**self.izbira_jezika[i])


@dataclass
class CursesConfig:
    pass


@dataclass
class Config:
    jezik: str
    igralec: IgralecConfig
    pygame: PyGameConfig
    curses: CursesConfig

    def __post_init__(self):
        self.igralec = IgralecConfig(**self.igralec)
        self.pygame = PyGameConfig(**self.pygame)
        self.curses = CursesConfig(**self.curses)


this = sys.modules[__name__]
this.CONFIG: Config = None
this.JEZIK: Jezik = None
this.APP: App = None
this.jeziki_dir = pot.data("jeziki")
this.config_path = pot.data("config.json")
this.app_path = pot.data("app.json")


# file_dict = json.loads(file_txt) pretvori json object v pytoh object, ki ga lahko uporablja program
def init():
    file = this.config_path.open("r")
    file_txt = file.read()
    file_dict = json.loads(file_txt)
    this.CONFIG = Config(**file_dict)

    # file = this.app_path.open("r")
    # file_txt = file.read()
    # file_dict = json.loads(file_txt)
    # this.CONFIG = Config(**file_dict)

    jezik_file = this.jeziki_dir.joinpath(f"{this.CONFIG.jezik}.json").open("r")
    jezik_txt = jezik_file.read()
    jezik_dict = json.loads(jezik_txt)
    this.JEZIK = Jezik(**jezik_dict)


# save() pretvori python object v json in shrani v config.json
def save():
    config_dict = asdict(this.CONFIG)
    file = this.config_path.open("w")
    file_txt = json.dumps(config_dict)
    file.write(file_txt)
