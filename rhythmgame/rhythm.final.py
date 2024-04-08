import pygame, sys, time
from pygame.locals import *

class Button(pygame.sprite.Sprite):
    def __init__(self,x):
        super(Button,self).__init__()
        self.index = 0
        self.x = x
        self.buttons = ["rhythmgame/button.png","rhythmgame/button_hit.png"]
        self.images = [pygame.image.load(self.buttons[0]).convert_alpha(),pygame.image.load(self.buttons[1]).convert_alpha()]
        self.images = [pygame.transform.scale(self.images[0], (90,90)),pygame.transform.scale(self.images[1], (90,90))]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center = (self.x, 690))

    def hit(self):
        self.image = self.images[1]
    
    def not_hit(self):
        self.image = self.images[0]

class Notes(pygame.sprite.Sprite):
    def __init__(self,column,y):
        super(Notes,self).__init__()
        self.index = 0

        if column == 1:
            self.x = 335
        if column == 2:
            self.x = 440
        if column == 3:
            self.x = 545
        if column == 4:
            self.x = 650

        self.y = y
        
        self.note = "rhythmgame/circle.png" # white circle: https://www.pinterest.com/pin/download-white-circle-png--658510776779891347/ (ALL OTHER IMAGES USED IN THIS PROGRAM WERE MADE IN MS PAINT)
        self.image = pygame.image.load(self.note).convert_alpha()
        self.image = pygame.transform.scale(self.image, (110,110))
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def fall(self):
        self.rect.centery += 20

class Longnote(pygame.sprite.Sprite):
    def __init__(self,column,y,):
        super(Longnote,self).__init__()

        if column == 1:
            self.x = 335
        if column == 2:
            self.x = 440
        if column == 3:
            self.x = 545
        if column == 4:
            self.x = 650

        self.y = y

        self.longnote = "rhythmgame/long_note.png" 
        self.image = pygame.image.load(self.longnote).convert_alpha()
        self.image = pygame.transform.scale(self.image, (75,100))
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def fall(self):
        self.rect.centery += 20
        
class Health(pygame.sprite.Sprite):
    def __init__(self):
        self.health = "rhythmgame/rhythmhealth.png"
        self.image = pygame.image.load(self.health).convert_alpha()
        self.image = pygame.transform.scale(self.image, (500,100))
        self.rect = self.image.get_rect(center = (0,700))

def sort_notes(notes,hit,button,health):
    for note in notes:
        note.fall()
        if note.rect.centery >= 825:
            note.kill()
            health.rect.centerx -= 25
        if note.rect.centery>= button.rect.centery-25 and note.rect.centery<= button.rect.centery+25: 
            if hit == True:
                note.kill()
                if health.rect.right < 250:
                    health.rect.centerx += 10
        if note.rect.centery>= button.rect.centery-40 and note.rect.centery <= button.rect.centery-25 and note.rect.centery<= button.rect.centery+40 and note.rect.centery<= button.rect.centery+25: 
            if hit == True:
                note.kill()
                if health.rect.right < 250:
                    health.rect.centerx += 5

#-------------------------------------------------------------------------------------------------------------------#
###Variables###
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Rhythm Game")
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 48)
fonts = pygame.font.get_fonts()

display_surface = pygame.display.set_mode((1000, 800))
font = pygame.font.Font('freesansbold.ttf', 32)
healthbar = font.render("Map Failed :C", True, (255,255,255), (0,0,0))
healthRect = healthbar.get_rect(center = (500,400))

mapdone = font.render("You Made it!", True, (255,255,255), (0,0,0))
mapdonerect = mapdone.get_rect(center = (500,400))

quitearly= font.render("Quitting so early?", True, (255,255,255), (0,0,0))
quitearlyrect = quitearly.get_rect(center = (500,400))

button_a = Button(335) 
button_s = Button(440) 
button_l = Button(545) 
button_semico = Button(650)

health = Health()
health_status = 1

###MAP###
first_notes = pygame.sprite.Group()
second_notes = pygame.sprite.Group()
third_notes = pygame.sprite.Group()
fourth_notes = pygame.sprite.Group()

first_notes_pixel = [400,1500,3250,400,4850,400,400,375,200,1075,400,200,1550,200,825,675,400,400,400,400,200,1000,400,200,600,400,400,600,600,400,400,1675,1062.5,637.5,1700,1062.5,2320,850,850,318.75,318.75,212.5,212.5,212.5,212.5,212.5,212.5]
second_notes_pixel = [3625,3175,2000,2000,1800,1250,400,400,400,1850,625,1125,1025,1275,400,400,1800,600,800,900,300,700,200,300,1887.5,425,2975,425,4551.25,318.75,318.75,318.75,318.75,425,318.75]
third_notes_pixel = [1850,1350,3200,450,1550,1900,3550,600,400,375,425,450,400,1350,400,825,875,1200,800,400,400,400,1200,800,1000,400,400,200,10157.5,212.5,318.75,318.75,318.75,318.75,212.5]
fourth_notes_pixel = [1400,5500,400,2500,3300,750,800,800,450,800,425,525,400,400,425,400,475,400,400,800,800,400,800,400,400,400,400,400,400,400,400,300,6857.5,850,2762.5,212.5,212.5,318.75,318.75,318.75,531.25]

for i in range(len(first_notes_pixel)+1):
    ending = -6250-(sum(first_notes_pixel[0:i]))
    first_notes.add(Notes(1,ending))

for i in range(len(second_notes_pixel)+1):
    ending = -2400-(sum(second_notes_pixel[0:i]))
    second_notes.add(Notes(2,ending))

for i in range(len(third_notes_pixel)+1):
    ending = -2600-(sum(third_notes_pixel[0:i]))
    third_notes.add(Notes(3,ending))

for i in range(len(fourth_notes_pixel)+1):
    ending = -2800-(sum(fourth_notes_pixel[0:i]))
    fourth_notes.add(Notes(4,ending))

for i in range(4):
    fourth_notes.add(Longnote(4,-2875-(75*i)))
for i in range(4):
    third_notes.add(Longnote(3,-4525-(75*i)))
for i in range(3):
    first_notes.add(Longnote(1,-6725-(75*i)))
for i in range(3):
    fourth_notes.add(Longnote(4,-10175-(75*i)))
for i in range(3):
    first_notes.add(Longnote(1,-11875-(75*i)))
for i in range(4):
    second_notes.add(Longnote(2,-13275-(75*i)))
for i in range(5):
    fourth_notes.add(Longnote(4,-16725-(75*i)))
for i in range(5):
    third_notes.add(Longnote(3,-17125-(75*i)))
for i in range(5):
    second_notes.add(Longnote(2,-17525-(75*i)))
for i in range(6):
    first_notes.add(Longnote(1,-18100-(75*i)))
for i in range(5):
    first_notes.add(Longnote(1,-19775-(75*i)))
for i in range(5):
    first_notes.add(Longnote(1,-21525-(75*i)))
for i in range(3):
    first_notes.add(Longnote(1,-22350-(75*i)))
for i in range(5):
    fourth_notes.add(Longnote(4,-23425-(75*i)))
for i in range(5):
    third_notes.add(Longnote(3,-23825-(75*i)))
for i in range(5):
    second_notes.add(Longnote(2,-24225-(75*i)))
for i in range(5):
    first_notes.add(Longnote(1,-24825-(75*i)))
for i in range(5):
    first_notes.add(Longnote(1,-26425-(75*i)))
for i in range(3):
    first_notes.add(Longnote(1,-27025-(75*i)))
for i in range(3):
    first_notes.add(Longnote(1,-27425-(75*i)))
for i in range(3):
    first_notes.add(Longnote(1,-27825-(75*i)))
third_notes.add(Notes(3,-28150))
for i in range(15):
    third_notes.add(Notes(3,-30150-(425*i)))
    fourth_notes.add(Notes(4,-30150-(425*i)))
for i in range(5):
    second_notes.add(Longnote(2,-32137.5-(75*i)))
for i in range(5):
    second_notes.add(Longnote(2,-35537.5-(75*i)))
for i in range(4):
    first_notes.add(Notes(1,-36507.5-(212.5*i)))
    second_notes.add(Notes(2,-37357.5-(212.5*i)))
    third_notes.add(Notes(3,-38207.5-(212.5*i)))
    fourth_notes.add(Notes(4,-39057.5-(212.5*i)))
last = Notes(3,-42245)
third_notes.add(last)

###GAME RUN###
running = True
winlose = True
while winlose:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            winlose = False
            
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                health_status = 2

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            button_a.hit()
            a_hit = True
        else:
            button_a.not_hit()
            a_hit = False

        if keys[pygame.K_s]:
            button_s.hit()
            s_hit = True
        else:
            button_s.not_hit()
            s_hit = False

        if keys[pygame.K_l]:
            button_l.hit()
            l_hit = True
        else:
            button_l.not_hit()
            l_hit = False

        if keys[pygame.K_SEMICOLON]:
            button_semico.hit()
            semi_hit = True
        else:
            button_semico.not_hit()
            semi_hit = False

        
        sort_notes(first_notes,a_hit,button_a,health)
        sort_notes(second_notes,s_hit,button_s,health)
        sort_notes(third_notes,l_hit,button_l,health)
        sort_notes(fourth_notes,semi_hit,button_semico,health)

        if third_notes.has(last) == False:
            health_status = 1
            time.sleep(0.1)
            running = False

        screen.fill((0,0,0))

        screen.blit(button_a.image, button_a.rect.topleft)
        screen.blit(button_s.image, button_s.rect.topleft)
        screen.blit(button_l.image, button_l.rect.topleft)
        screen.blit(button_semico.image, button_semico.rect.topleft)

        first_notes.draw(screen)
        second_notes.draw(screen)
        third_notes.draw(screen)
        fourth_notes.draw(screen)

        if health.rect.right > 250:
            health.rect.centerx -= 5
        if health.rect.right < 0:
            running = False
            health_status = 0
        screen.blit(health.image, health.rect.topleft)

        pygame.display.flip()
        clock.tick(60)

    if health_status == 0:
        screen = pygame.display.set_mode((1000,800))
        display_surface.blit(healthbar,healthRect)
        pygame.display.set_caption("Failed")
        
    if health_status == 1:
        screen = pygame.display.set_mode((1000,800))
        display_surface.blit(mapdone,mapdonerect)
        pygame.display.set_caption("Completed") 

    if health_status == 2:
        screen = pygame.display.set_mode((1000,800))
        display_surface.blit(quitearly,quitearlyrect)
        pygame.display.set_caption("Quit")

    pygame.display.flip()
    clock.tick(1)

pygame.quit()
sys.exit()