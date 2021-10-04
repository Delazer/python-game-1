import pygame
pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption('Game')

clock=pygame.time.Clock()
x=250
y=425
width=40
height=60
speed=10
run=True
isjump=False
jumpcount=10

while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>5:
        x-=speed
    elif keys[pygame.K_RIGHT] and x<500-width-5:
        x+=speed
    if not(isjump):
        if keys[pygame.K_SPACE]:
            isjump=True
    else:
        if jumpcount>=-10:
            if jumpcount<0:
                y+=(jumpcount**2)/2
            else:
                y-=(jumpcount**2)/2
            jumpcount-=1
        else:
                isjump=False
                jumpcount=10

    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update()
