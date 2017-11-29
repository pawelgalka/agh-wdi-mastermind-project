import pygame,sys

FPS = 60
width = 680
height = 800
ball_height=60
pygame.init()
m=False
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

def menu(m):
    while not m:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse = pygame.mouse.get_pos()
                if (322 > mouse[0] > 272) and (370 > mouse[1] > 320):
                    m = True
        pygame.draw.rect(display, (255, 0, 0), (width * 0.4, height * 0.4, 50, 50))

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


            print(event) #display event in a console to check what's happening


    display.fill((255, 255, 0))
    display.blit(background, (0, 0))
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

    menu(m)
    m=True

    clock.tick(FPS)

pygame.quit()
