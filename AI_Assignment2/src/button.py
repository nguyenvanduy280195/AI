class Button():
    def __init__(self, image, x, y):
        self.__image__ = image
        self.__rect__ = self.__image__.get_rect()
        self.__rect__.x = x
        self.__rect__.y = y

    @property
    def rect(self): return self.__rect__

    def draw(self, screen): screen.blit(self.__image__, self.__rect__)
