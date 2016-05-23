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
deltaX=0
finalSize=7
leaf=pygame.image.load('leaf2.jpg')



def draw_tree(size,position,angel,length,deltaX,thick):
    global number
    global left
    global right
    global leaf
    ratio=0.7
    newleng=length*ratio
    (x,y)=position
    newX=x+length*math.cos(angel)
    newY=y-length*math.sin(angel)
    newThick=thick*0.8
    if size!=finalSize:
        newX+=(deltaX-SCREEN_WIDTH/2)/SCREEN_WIDTH*50
    newPosition=(newX,newY)
##    script=myfont.render(str(number),True,(0,0,0))
##    screen.blit(script,newPosition)
##    number+=1
    pygame.draw.line(screen,(128,64,0),position,newPosition,int(thick))
    if size>0:
        if size>2: 
            draw_tree(size-1,newPosition,angel-left,newleng,deltaX,int(newThick))
            draw_tree(size-1,newPosition,angel+right,newleng,deltaX,int(newThick))
        else:
            draw_tree(size-1,newPosition,angel-left,newleng,deltaX,int(newThick))
            draw_tree(size-1,newPosition,angel+right,newleng,deltaX,int(newThick))
            screen.blit(leaf,newPosition)
    
def main():
    global deltaX
#deltaX*1/t to make it go back automatically through time.
    position=(300,SCREEN_HEIGHT)
    angel=math.pi/2
    length=150
    thick=10
    running=True
    screen.fill((255,255,255))    
    while running:
        for event in pygame.event.get():
            if event.type==QUIT:
                running=False
        mosX,moxY=pygame.mouse.get_pos()
        if mosX!=deltaX:
            screen.fill((255,255,255))
            deltaX=mosX       
##            elif event.type==pygame.MOUSEMOTION:
##                (mosX,mosY)=pygame.mouse.get_pos()
            size=7
            draw_tree(size,position,angel,length,deltaX,thick)
            pygame.display.update()
main()


    
    
    
    


