import pygame
from random import randint
"""from player import Player"""

screen = pygame.display.set_mode((1000, 700))


class Card(pygame.sprite.Sprite):
    # Creates a card with color and value at screen position
    def __init__(self,  color='n', value='n', x=100, y=540,):
        super().__init__()
        self.image = None
        self.color = color #pygame.image.load(color)
        self.value = value #pygame.image.load(value)
        self.x = x
        self.y = y

        self.init_card_drawing()




    """def __init__(self, game):
        super().__init__()
        self.game = game
        self.player = Player(self)
        self.reserve = [["Pique"], ["1"]]
        self.hand = []
        self.count_hand = 0
        self.image = pygame.image.load(
            './asset/Pique.png')
        self.image2 = pygame.image.load(
            'C:/Users/Antoine Yon/Documents/Travail/NSI/Projet/1.png')

        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x
        self.rect.y = 540
        self.velocity = 1"""

    """def card_selection(self, a, b):
        self.image1 = pygame.image.load(
            'C:/Users/Antoine Yon/Documents/Travail/NSI/Projet/' + 'a')
        self.image2 = pygame.image.load(
            'C:/Users/Antoine Yon/Documents/Travail/NSI/Projet/' + 'b')"""

    def init_card_drawing(self):
        cartes = {
            'C': './asset/Coeur.png',
            'Ca': './asset/Carreau.png',
            'T': './asset/Trèfles.png',
            'P': './asset/Pique.png',
            '1': './asset/1.png',
            '2': './asset/2.png',
            '3': './asset/3.png',
            '4': './asset/4.png',
            '5': './asset/5.png',
            '6': './asset/6.png',
            '7': './asset/7.png',
            '8': './asset/8.png',
            '9': './asset/9.png',
            '10': './asset/10.png',
            '11': './asset/J.png',
            '12': './asset/Q.png',
            '13': './asset/K.png',
            'n': '/asset/vide.png'
        }
        str1=cartes[self.color]

        self.image = pygame.image.load(cartes[self.color])
        self.image.blit(pygame.image.load(cartes[self.value]), (0,0))


    """def new_card(self):
        color = self.color
        value = self.value
        return color, value"""


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
