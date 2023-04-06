from dataclasses import dataclass


@dataclass
class AplikacijaJezik:
	naslov: str


@dataclass
class MeniJezik:
	konfiguracija: str
	igraj: str
	izhod: str
	vnesi_ime: str
	ime: str


@dataclass
class ZaslonJezik:
	velikost: str
	fullscreen: str


@dataclass
class MeniKonfiguracijaJezik:
	zaslon: ZaslonJezik
	jezik: str

	def __post_init__(self):
		self.zaslon = ZaslonJezik(**self.zaslon)


@dataclass
class Jezik:
	aplikacija: AplikacijaJezik
	nazaj: str
	meni: MeniJezik
	meni_konfiguracija: MeniKonfiguracijaJezik

	def __post_init__(self):
		self.aplikacija = AplikacijaJezik(**self.aplikacija)
		self.meni = MeniJezik(**self.meni)
		self.meni_konfiguracija = MeniKonfiguracijaJezik(**self.meni_konfiguracija)
