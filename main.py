from turtle import width
import pygame
import os
pygame.font.init()
WIDTH, HEIGHT= 1920, 1080
WIN = pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Cow Climbs")

FPS=60

FONT = pygame.font.SysFont('consolas',40)

WIZARD_IMAGE = pygame.image.load(os.path.join('Assets',"wizard.png"))
WIZARD=pygame.transform.scale(WIZARD_IMAGE,(200 ,200))



class Wizard:
    def __init__(self,x,y,width,height,image):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.image=image
        self.health=100
    def move(self,keys_pressed):
        if keys_pressed[pygame.K_d]:
            self.x+=1
            self.health=self.health-1
    def draw(self,win):
        health_text=FONT.render("Health: "+str(self.health),1,(0,0,0))
        win.blit(health_text, (200,20))
        win.blit(self.image,(self.x,self.y))






mago=Wizard(0,0,100,100,WIZARD)

def main():
    wizard=pygame.Rect(0,0,100,100)
    run=True
    clock= pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
        keys_pressed = pygame.key.get_pressed()
        WIN.fill((255,255,255))

        mago.draw(WIN)
        mago.move(keys_pressed)

        print(mago.health)
        if mago.health==0:
            run=False
        pygame.display.update()
    pygame.quit() 

if __name__ == "__main__":
    main()
        