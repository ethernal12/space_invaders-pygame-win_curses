from src.app._app import App


class Gui(App):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.dx: int = 0
        self.dy: int = 0
        self.windowSurface: Optional[pygame.Surface] = None
        self.clock = pygame.time.Clock()
    def inicializacija_igre(self):
        pass

    def narisi_igro(self):
        pass

    def input_igralca(self):
        pass

    def konec(self):
        pass
