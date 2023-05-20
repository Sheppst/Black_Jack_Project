import pygame
from player import Player

screen = pygame.display.set_mode((1000, 700))


class Card(pygame.sprite.Sprite):
    # Creates a card with color and value at screen position
    def __init__(self, color, value, x=100, y=540):
        self.color = pygame.image.load(color)
        self.value = pygame.image.load(value)
        self.x = x
        self.y = y

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.player = Player(self)
        self.reserve = [["Pique"], ["1"]]
        self.hand = []
        self.count_hand = 0
        self.image = pygame.image.load(
            './asset/Pique.png')
        """self.image2 = pygame.image.load(
            'C:/Users/Antoine Yon/Documents/Travail/NSI/Projet/1.png')"""

        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x
        self.rect.y = 540
        self.velocity = 1

    def card_selection(self, a, b):
        self.image1 = pygame.image.load(
            'C:/Users/Antoine Yon/Documents/Travail/NSI/Projet/' + 'a')
        self.image2 = pygame.image.load(
            'C:/Users/Antoine Yon/Documents/Travail/NSI/Projet/' + 'b')

    def init_card_drawing(self, carte):
        cartes = {}
        self.color = cartes[carte[-1]]
        self.value = cartes[carte[:-1]]

    def new_card(self):
        color = self.color
        value = self.value
        carte = color.copy()
        carte.blit(value, (self.x, self.y))


"""self.rect2 = self.image2.get_rect()
        self.rect2.x = self.player.rect.x
        self.rect2.y = 540"""

"""def go_to_hand(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity"""

"""def check(self):
        if self.count_hand != len(self.hand):
            self.count_hand += 1
            return True"""
