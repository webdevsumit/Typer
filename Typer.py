import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    K_a,
    K_b,
    K_c,
    K_d,
    K_e,
    K_f,
    K_g,
    K_h,
    K_i,
    K_j,
    K_k,
    K_l,
    K_m,
    K_n,
    K_o,
    K_p,
    K_q,
    K_r,
    K_s,
    K_t,
    K_u,
    K_v,
    K_w,
    K_x,
    K_y,
    K_z,
    )
    
keys =  ( K_a,
                K_b,
                K_c,
                K_d,
                K_e,
                K_f,
                K_g,
                K_h,
                K_i,
                K_j,
                K_k,
                K_l,
                K_m,
                K_n,
                K_o,
                K_p,
                K_q,
                K_r,
                K_s,
                K_t,
                K_u,
                K_v,
                K_w,
                K_x,
                K_y,
                K_z,
)


pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
word_y_pos = 600
wordSpeed = 5
initialHeart = 5
heart = initialHeart
score = 0

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Typer')

font = pygame.font.Font('freesansbold.ttf', 100)
font2 = pygame.font.Font('freesansbold.ttf', 32)
font32 = pygame.font.Font('freesansbold.ttf', 50)
startGame = True


#DEFINE WHICH SCREEEN IS APPEARING
SHOWN_SCREEN = 'main_screen'

randNum = []
checkNum = []
randNumSize = 20
for i in range(randNumSize):
    randNum.append(random.randint(65,90))

def matchList(l,lst):
    for a in l:
        if a not in lst:
            return False
    return True


class words:
    def __init__(self, surface, pos, y):
        self.surf = surface
        self.pos = pos
        self.x = (randNum[self.pos]-62)*45
        self.y = y
        self.R = random.randint(190,225)
        self.B = random.randint(190,225)
        self.G = random.randint(190,225)
        pygame.draw.circle(self.surf, (0,125,125), (self.x,self.y),100)
        self.text = font.render(chr(randNum[pos]),True, (self.R,self.B,self.G))
        self.surf.blit(self.text, (self.x-37,self.y-40))
        
        self.text_score = font32.render('score '+str(score),True, (self.R,self.B,self.G))
        self.surf.blit(self.text_score, (0,0))
        
        self.text_life = font32.render('% '+('*'*heart),True, (self.R,self.B,self.G))
        self.surf.blit(self.text_life, (0,50))
        
#MAIN SCREEN        
def main_screen():
    surf = pygame.Surface((screen.get_width(),screen.get_height()))
    surf.fill((0,0,0))
    
    x = surf.get_width()
    y = surf.get_height()
    
    pygame.draw.circle(surf, (0,125,125), (x*0.35,y*0.2),500)
    
    text_TYPER = font.render('TYPER', True,  (0,0,0))
    surf.blit(text_TYPER,((x*0.2,y*0.15)))
    
    text_desc = font2.render('Speed up your typing skill' , True,  (0,0,0))
    surf.blit(text_desc,((x*0.3,y*0.3)))
    
    pygame.draw.rect(surf, (225,225,225), (x*0.7,y*0.65,240,105))
    
    text_start_button = font.render('Start' , True,  (100,100,100), (25,225,225))
    surf.blit(text_start_button,((x*0.7,y*0.65)))
    return surf

#GAME SCREEN
def game_screen(y):
    surf = pygame.Surface((screen.get_width(),screen.get_height()))
    surf.fill((0,0,0))
    
    x = surf.get_width()
    for i in range(randNumSize):
        y_pos = (y+(i*400))
        if ((y_pos <= 0) and (randNum[i] not in checkNum)):
            global heart
            heart -= 1
            checkNum.append(randNum[i])
        elif ((y_pos > 0) and (randNum[i] not in checkNum)):
            words(surf, i , y_pos)
        
    return surf

#SCORE BOARD SCREEN
def score_board():
    surf = pygame.Surface((screen.get_width(),screen.get_height()))
    surf.fill((0,0,0))
    
    x = surf.get_width()
    y = surf.get_height()
    
    pygame.draw.circle(surf, (0,125,125), (x*0.35,y*0.2),500)
    
    text_TYPER = font.render('TYPER', True,  (0,0,0))
    surf.blit(text_TYPER,((x*0.2,y*0.15)))
    
    text_desc = font2.render('Speed up your typing skill' , True,  (0,0,0))
    surf.blit(text_desc,((x*0.3,y*0.3)))
    
    text_score = font32.render('SCORE : '+str(score) , True,  (125,0,125))
    surf.blit(text_score,((x*0.05,y*0.7)))
    
    pygame.draw.rect(surf, (225,225,225), (x*0.7,y*0.65,346,105))
    
    text_start_button = font.render('Replay' , True,  (100,100,100), (25,225,225))
    surf.blit(text_start_button,((x*0.7,y*0.65)))
    return surf
    

while startGame:
    #basic code of pygame
    
    screen.fill((200,200,200))
    for event in pygame.event.get():
        if event.type == QUIT:
            startGame = False
           
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                startGame = False
    
    #game start from here
    if SHOWN_SCREEN == 'main_screen':
        screen.blit(main_screen(), (0,0))
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                x = main_screen().get_width()+45
                y = main_screen().get_height()+45
                if((  x*0.7 <= mouse[0]  <=  x*0.7+240) and (  y*0.65 <= mouse[1]  <=  y*0.65+105)):
                    SHOWN_SCREEN = 'game_screen'
                
                pygame.draw.rect(screen, (125,125,125), (x*0.7,y*0.65,240,105))

    elif SHOWN_SCREEN == 'game_screen':
        word_y_pos -= wordSpeed
        screen.blit(game_screen(word_y_pos), (0,0))
        
        if score%2==0 and score>0:
            wordSpeed += wordSpeed*score*10
            
        if heart==0:
            SHOWN_SCREEN='score_board'
            heart = initialHeart
            wordSpeed = 5
        
        score +=0.01
        if (matchList(randNum,checkNum)):
            randNum = []
            checkNum = []
            word_y_pos = 600
            for i in range(randNumSize):
                randNum.append(random.randint(65,90))
        
        for event in pygame.event.get():
            
            if event.type == KEYDOWN:
                for key_pos,key in enumerate(keys):
                    if event.key == key:
                        no = 65+key_pos
                        if ((no in randNum) and (no not in checkNum)):
                            checkNum.append(no)
                        
            
        
            
    
    elif SHOWN_SCREEN == 'score_board':
        screen.blit(score_board(), (0,0))
        
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                x = main_screen().get_width()+45
                y = main_screen().get_height()+45
                if((  x*0.7 <= mouse[0]  <=  x*0.7+346) and (  y*0.65 <= mouse[1]  <=  y*0.65+105)):
                    SHOWN_SCREEN = 'game_screen'
                    score = 0
                pygame.draw.rect(screen, (125,125,125), (x*0.7,y*0.65,346,105))
        
        
    #fliping display
    pygame.display.flip()
pygame.quit()