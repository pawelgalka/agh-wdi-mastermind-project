import pygame,sys

FPS = 60
width = 680
height = 800
ball_height = 60
m = False
m2 = False
pygame.init()

display = pygame.display.set_mode((width, height)) #tuple width,height

pygame.display.set_caption("MASTERMIND") #change title of window

clock = pygame.time.Clock()

background = pygame.image.load('background.png') #import an image
yellow = pygame.image.load("yellow.png")
orange = pygame.image.load("orange.png")
blue = pygame.image.load("blue.png")
green = pygame.image.load("green.png")
turkish = pygame.image.load("turkish.png")
brown = pygame.image.load("brown.png")
pink = pygame.image.load("pink.png")
red = pygame.image.load("red.png")
deck = pygame.image.load("deck.png")
field = pygame.image.load("field.png")
mode1 = pygame.image.load("mode1.png")
mode2 = pygame.image.load("mode2.png")
level1 = pygame.image.load("level1.png")
level2 = pygame.image.load("level2.png")

def menu():
    global mode, m
    m=False
    while not m:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()
                if (540 > mouse[0] > 140) and (300 > mouse[1] > 150):
                    mode=1
                    m = True
                if (540 > mouse[0] > 140) and (650 > mouse[1] > 500):
                    mode=2
                    m = True
        display.blit(background, (0, 0))
        display.blit(mode1, (140, 150))
        display.blit(mode2, (140, 500))

        pygame.display.update()

def level_menu():
    global level, m2
    m2 = False
    while not m2:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()
                if (540 > mouse[0] > 140) and (300 > mouse[1] > 150):
                    level=1
                    m2 = True
                if (540 > mouse[0] > 140) and (650 > mouse[1] > 500):
                    level=2
                    m2 = True
        display.blit(background, (0, 0))
        display.blit(level1, (140, 150))
        display.blit(level2, (140, 500))

        pygame.display.update()

while True: #main loop
    # Handle events in window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5


            #print(event) #display event in a console to check what's happening

    if m==False:
        menu()

    if m2==False:
        level_menu()

    #display.fill((255, 255, 0))
    display.blit(background, (0, 0))
    if level==2:
        display.blit(yellow, (width * 0.8, height - 100))
        display.blit(orange, (width * 0.8, height - 100 - ball_height*1))
    display.blit(blue, (width * 0.8, height - 100 - ball_height*2))
    display.blit(green, (width * 0.8, height - 100 - ball_height*3))
    display.blit(turkish, (width * 0.8, height - 100 - ball_height*4))
    display.blit(brown, (width * 0.8, height - 100 - ball_height*5))
    display.blit(pink, (width * 0.8, height - 100 - ball_height*6))
    display.blit(red, (width * 0.8, height - 100 - ball_height*7))
    display.blit(deck, (width * 0.2, height - 100))
    display.blit(field, (width * 0.1, height - 780))

    pygame.display.update()



    clock.tick(FPS)

pygame.quit()
