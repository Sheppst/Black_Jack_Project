import pygame
from random import randint
from player import Player
from card import Card


class Black_Jack:

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_card = pygame.sprite.Group()
        self.pressed = {}
        self.draw_card()
        self.position_carte = 0
        self.know_player()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def draw_card(self):
        carte = Card(self)
        self.position_carte = carte.rect.width
        self.all_card.add(carte)
        """print(carte.rect.x)"""

    """def check_card(self):
        carte = Card(self)
        b=0
        if carte.check():
            b += 1
            return b"""

    def new_card(self):
        carte = Card(self)
        a = "Pique"
        b = "1"
        return carte.card_selection(a, b)

    def know_player(self):
        joueur = Player(self)
        self.all_players.add(joueur)
        """print(joueur.rect.x)
        print(joueur.rect)
        print(joueur.rect.width)"""

    """"def replace(self):
        if self.game.check_collision(self, self.game.all_card):
            self.all_players.rect.x = self.all_cards.rect.x"""
