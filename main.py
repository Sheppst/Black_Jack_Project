import pygame
from black_jack import Black_Jack

pygame.init()

pygame.display.set_caption("Black Jack")
screen = pygame.display.set_mode((1000, 700))

background = pygame.image.load('./asset/Fond vert.jpg')
background1 = pygame.image.load(
    './asset/cadre blanc.png')

reserve = [[], []]
hand = []
game = Black_Jack()

running = True
while running:

    screen.blit(background, (-100, 0))
    screen.blit(background1, (80, 500))

    screen.blit(game.player.image, game.player.rect)

    for card in game.all_card:
        """card.go_to_hand()"""
        """print(card.rect.x)"""
    game.all_card.draw(screen)
    """game.player.rect.x += game.all_card.rect.x"""
    """print(game.player.rect.x)"""
    for player in game.all_players:
        """b = 1
        a = 0
        if game.check_card() == b:
            print(a + 1)
            b = b + 1"""
        player.replace()


    game.all_players.draw(screen)

    """if game.check_collision(game, game.all_players):
        print ("collision")"""

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        """elif event.key == pygame.K_SPACE:
            game.new_card()"""


        """elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False"""
