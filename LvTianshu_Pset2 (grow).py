import pygame
from pygame.locals import *
import math

pygame.init()

SCREEN_HEIGHT=600
SCREEN_WIDTH=800
SCREEN_SIZE=(SCREEN_WIDTH,SCREEN_HEIGHT)
myfont=pygame.font.SysFont("arial", 20)

pygame.display.set_caption('Tree in Recursion')

screen=pygame.display.set_mode(SCREEN_SIZE,pygame.RESIZABLE)
background=pygame.Surface(screen.get_size())
background=background.convert()
background.fill((255,255,255))
clock=pygame.time.Clock()
number=0
left=math.radians(15)
right=math.radians(15)



def draw_tree(size,position,angel,length,thick):
    global number
    global left
    global right
    ratio=0.7
    newleng=length*ratio
    (x,y)=position
    newX=x+length*math.cos(angel)
    newY=y-length*math.sin(angel)
    newThick=thick*0.9
    newPosition=(newX,newY)
    pygame.draw.line(screen,(128,64,0),position,newPosition,int(thick))
    if size>0: 
        draw_tree(size-1,newPosition,angel-left,newleng,int(newThick))
        draw_tree(size-1,newPosition,angel+right,newleng,int(newThick))
    
def main():
    global deltaX
    position=(300,SCREEN_HEIGHT)
    angel=math.pi/2
    length=150
    thick=10
    running=True
    screen.fill((255,255,255))    
    for i in range (1,7):
        size=i
        draw_tree(size,position,angel,length,thick)
        pygame.display.update()
        clock.tick(1)
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                running=False

main()


    
    
    
    


