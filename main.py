from turtle import width
import pygame
import os

WIDTH, HEIGHT= 1920, 1080
WIN = pygame.display.set_mode((WIDTH,HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Cow Climbs")

FPS=60


WIZARD_IMAGE = pygame.image.load(os.path.join('Assets',"wizard.png"))
WIZARD=pygame.transform.scale(WIZARD_IMAGE,(200 ,200))


class Wizard:
    def __init__(self,x,y,width,height,image):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.image=image
    def move(self,keys_pressed):
        if keys_pressed[pygame.K_d]:
            self.x+=1
    def draw(self,win):
        win.blit(self.image,(self.x,self.y))



def draw(win,wizard):
    win.blit(WIZARD,(wizard.x,wizard.y))



mago=Wizard(0,0,100,100,WIZARD)

def main():
    wizard=pygame.Rect(0,0,100,100)
    run=True
    clock= pygame.time.Clock()
    while run:
        clock.tick(FPS)
        keys_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
        WIN.fill((255,255,255))
        mago.draw(WIN)
        mago.move(keys_pressed)

        print()
        #draw(WIN,wizard)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
        