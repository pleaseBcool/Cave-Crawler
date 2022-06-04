from turtle import width
import pygame
import os
pygame.font.init()
WIDTH, HEIGHT= 1920, 1080
WIN = pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Cave Crawler")

FPS=60

FONT = pygame.font.SysFont('consolas',40)

WIZARD_IMAGE = pygame.image.load(os.path.join('Assets',"wizard.png"))
WIZARD=pygame.transform.scale(WIZARD_IMAGE,(200 ,200))

POINT_IMG = pygame.image.load(os.path.join('Assets',"circlebad.png"))
POINT = pygame.transform.scale(POINT_IMG,(200 ,200))

GOBLIN_IMG = pygame.image.load(os.path.join('Assets',"goblin.png"))
GOBLIN = pygame.transform.scale(GOBLIN_IMG,(200 ,200))

CAVE_IMG = pygame.image.load(os.path.join('Assets',"cave.png"))
CAVE = pygame.transform.scale(CAVE_IMG,(WIDTH/1.25,HEIGHT/1.25))
class Enemy:
    global GOBLIN
    def __init__(self,x,y,width,height,type):
        self.Rect=pygame.Rect(x,y,width,height)
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.alive=True
        self.health=200
        self.type=type
        if type=="goblin_weak":
            self.image=GOBLIN
    def draw(self, win):
        
        if self.type=="goblin_weak":
            if self.alive==True:
                health_text=FONT.render("Health: "+str(self.health),1,(255,255,255))
                win.blit(health_text, (1200,50))
                win.blit(GOBLIN,(self.Rect.x,self.Rect.y))

class Point:
    def __init__(self,x,y,width,height,image):
        self.Rect=pygame.Rect(x+20,y,width+100,height+200)
        self.image=image
        self.alive=True
    def draw(self,win):
        if self.alive==True:
            
            win.blit(self.image,(self.Rect.x,self.Rect.y))
    def check(self, mouse_pos, enemy,wizard,ev):

        if self.Rect.collidepoint(mouse_pos):
                if ev[0]:
                    if self.alive==True:
                        #print("colliding")
                        enemy.health-=wizard.damage
                        self.alive=False

class Wizard:
    def __init__(self,x,y,width,height,image):
        self.Rect=pygame.Rect(x+20,y,width+100,height+200)
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.image=image
        self.health=100
        self.damage=10
        
    def move(self,keys_pressed):
        if keys_pressed[pygame.K_d]:
            self.Rect.x +=1
            # self.health=self.health-1
            #self.Rect=pygame.Rect(self.x,self.y,self.width,self.height)
        if keys_pressed[pygame.K_w]:
            self.Rect.y+=1
            # self.health=self.health-1
            #self.Rect=pygame.Rect(self.x,self.y,self.width,self.height)
    def draw(self,win):
        health_text=FONT.render("Health: "+str(self.health),1,(255,255,255))
        win.blit(health_text, (self.Rect.x,self.Rect.y))
        win.blit(self.image,(self.Rect.x,self.Rect.y))





wizard=Wizard(0,400,100,100,WIZARD)
point_test=Point(500,200,100,200,POINT_IMG)
enemy_test=Enemy(1200,400,100,100,"goblin_weak")
def main():
    run=True
    clock= pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
        keys_pressed = pygame.key.get_pressed()
        
        WIN.fill((255,255,255))
        WIN.blit(CAVE,(0,0))
        ev=pygame.mouse.get_pressed()

        mouse_pos = pygame.mouse.get_pos()
        point_test.check(mouse_pos, enemy_test,wizard,ev)
        point_test.draw(WIN)

        wizard.draw(WIN)
        wizard.move(keys_pressed)
        enemy_test.draw(WIN)
        
        if wizard.health==0:
            run=False
        pygame.display.update()
    pygame.quit() 

if __name__ == "__main__":
    main()
