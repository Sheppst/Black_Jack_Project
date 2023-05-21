import pygame
from black_jack import Black_Jack
from card import Card

cartes = []
nom = ["C", "Ca", "T", "P"]
for i in range(4):
    for j in range(1, 14):
        cartes.append((j, nom[i]))

pygame.init()

pygame.display.set_caption("Black Jack")
screen = pygame.display.set_mode((1000, 700))

background = pygame.image.load('./asset/Fond vert.jpg')
background1 = pygame.image.load(
    './asset/cadre blanc.png')
surf1 = pygame.image.load(
    './asset/1.png')
reserve = []
nom = ["C", "Ca", "T", "P"]
for i in range(4):
    for j in range(1, 14):
        reserve.append((Card(nom[i], str(j))))
hand = []
game = Black_Jack()
running = True
while running:
    # Display

    screen.blit(background, (-100, 0))
    screen.blit(background1, (80, 500))
    screen.blit(surf1, (5, 5))

    """screen.blit(game.player.image, game.player.rect)"""
    # affichage des cartes de la main du joueur
    x = 100
    y = 540
    for each_card in hand:
        screen.blit(each_card.image, (x, y))
        x += 100

    """for card in game.all_card:
        card.go_to_hand()
        print(card.rect.x)
    game.all_card.draw(screen)"""
    """game.player.rect.x += game.all_card.rect.x"""
    """print(game.player.rect.x)"""
    """for player in game.all_players:
        b = 1
        a = 0
        if game.check_card() == b:
            print(a + 1)
            b = b + 1
        player.replace()


    game.all_players.draw(screen)"""

    """if game.check_collision(game, game.all_players):
        print ("collision")"""

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_SPACE:
                carte = Card('P', '13', x, y)
                hand.append(carte)
            elif event.key == pygame.K_b:
                hand = []

        """elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False"""
