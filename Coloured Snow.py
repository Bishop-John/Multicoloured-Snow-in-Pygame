import pygame, random
pygame.init()

BLACK  = [0  , 0  , 0  ]
WHITE  = [255, 255, 255]
RED    = [255, 0  , 0  ]
BLUE   = [0  , 0  , 255]
GREEN  = [0  , 255, 0  ]
TEAL   = [0  , 128, 128]
YELLOW = [255, 255, 0  ]

screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

snowList = []

for i in range(1000):
    x = random.randint(0,600)
    y = random.randint(0,600)
    snowList.append([x,y])

snowing = True

while snowing == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            snowing = False
            pygame.quit()
            quit()

    screen.fill(BLACK)
    for i in range(len(snowList)):
        pygame.draw.circle(screen, randomSnowColour, snowList[i], 3)
        randomSnowSpeed = random.randint(1,10)
        snowList[i][1] = snowList[i][1] + randomSnowSpeed

        if snowList[i][1] > 600:
            y = random.randint(-50 ,-10)
            snowList[i][1] = y
            snowList[i][0] = snowList[i][0] - 20

    pygame.display.update()
    clock.tick(30)





















