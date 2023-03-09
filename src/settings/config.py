import sys
from dataclasses import dataclass, asdict
import json

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
    dimenzije: list[DimenzijaConfig]
    izbira_jezika: list[JezikConfig]

    def __post_init__(self):
        self.dimenzija = DimenzijaConfig(**self.dimenzija)

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


@dataclass
class NastavitveConfig:
    clock_tick: int


@dataclass
class App:
    nastavitve: NastavitveConfig
    barve: BarveConfig
    font: FontConfig

    def __post_init__(self):
        self.nastavitve = NastavitveConfig(**self.nastavitve)
        self.font = FontConfig(**self.font)
        self.barve = BarveConfig(**self.barve)


this = sys.modules[__name__]
this.CONFIG: Config = None
this.JEZIK: Jezik = None
this.APP: App = None
print(pot.data)
this.jeziki_dir = pot.data("jeziki")
this.config_path = pot.data("config.json")
this.app_path = pot.data(".app.json")

def init():
    file = this.config_path.open("r")
    file_txt = file.read()
    file_dict = json.loads(file_txt)
    this.CONFIG = Config(**file_dict)

    file = this.app_path.open("r")
    file_txt = file.read()
    file_dict = json.loads(file_txt)
    this.APP = App(**file_dict)
    jezik_file = this.jeziki_dir.joinpath(f"{this.CONFIG.jezik}.json").open("r")
    jezik_txt = jezik_file.read()
    jezik_dict = json.loads(jezik_txt)
    this.JEZIK = Jezik(**jezik_dict)
print(pot.data())

def save():
    config_dict = asdict(this.CONFIG)
    file = this.config_path.open("w")
    file_txt = json.dumps(config_dict)
    file.write(file_txt)
