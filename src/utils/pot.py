from pathlib import Path


def root(*path):
    return Path(__file__).parent.parent.parent.joinpath(*path).resolve().absolute()


def data(*path):
    return root("data", *path)


def media(*path):
    return root("data/media", *path)
