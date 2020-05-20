import pygame
import sys,random
import time
from pygame import mixer


pygame.mixer.init()
# --- constants ---

WIDTH = 800
HEIGHT = 600

FPS = 5

ballx=380
bally=540

glovex=360
glovey=220

score=0
life=5

# --- class ---

class Button(object):

    def __init__(self, position, size, color, text):

        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = pygame.Rect((0,0), size)

        font = pygame.font.SysFont(None, 32)
        text = font.render(text, True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = self.rect.center

        self.image.blit(text, text_rect)

        # set after centering text
        self.rect.topleft = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                return self.rect.collidepoint(event.pos)

def kick_right():
    global ballx,bally,glovey,glovex,score,life
    lst=[207,360,513]
    glovex=random.choice(lst)
    while bally>glovey:
        bally-=10
        ballx+=5

    if (ballx-glovex>60):
        score+=1
    else:
        life-=1

    


def kick_left():
    global ballx,bally,glovey,glovex,score,life
    lst=[207,360,513]
    glovex=random.choice(lst)
    
    while bally>glovey:
        bally-=10
        ballx-=5

    if (glovex-ballx>60):
        score+=1
    else:
        life-=1

def kick_straight():
    global ballx,bally,glovey,glovex,score,life
    lst=[207,360,513]
    glovex=random.choice(lst)
    while bally>glovey:
        bally-=10

    if (glovex-ballx>60) or (ballx-glovex>60):
        score+=1
    else:
        life-=1

def randkick_right():
    global ballx,bally,glovey
    while bally>glovey:
        bally-=10
        ballx+=5


    

def randkick_left():
    global ballx,bally,glovey
    
    while bally>glovey:
        bally-=10
        ballx-=5




def randkick_straight():
    global bally,glovey
    
    while bally>glovey:
        bally-=10



def calculate_score():
    global ballx,glovex,score,life
    if (ballx-glovex<60) and (ballx-glovex>0):
        score+=1
        mixer.music.load('glovestop.wav')
        mixer.music.play()
    else:
        life-=1

        

    
def show_score():
    global score,life
    font=pygame.font.Font("freesansbold.ttf",30)
    life_text=font.render(str(life),True,(0,0,0))
    score_text=font.render(str(score),True,(0,0,0))
    screen.blit(life_text,(650,30))
    screen.blit(score_text,(760,30))

    

def stage1(screen):
    mixer.music.load('bgm.mp3')
    mixer.music.play(-1)
    

    button1 = Button((350,200), (150, 50), (250,200,0), "START")
    button2 = Button((350,300), (150, 50), (0,0,255), "CONTROLS")
    button3 = Button((350,400), (150, 50), (255,0,0), "EXIT")
    # - mainloop -
    
    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                # go to stage2
                stage2(screen)
            if button2.is_clicked(event):
                # go to stage2
                stage6(screen)
            if button3.is_clicked(event):
                # exit
                pygame.quit()
                exit()

        # - draws -

        bg=pygame.image.load('bgnew.jpg') 
        screen.blit(bg,(0,0)) 
        button1.draw(screen)
        button2.draw(screen)
        button3.draw(screen)
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)

def stage2(screen):
    mixer.music.load('game_bgm.mp3')
    mixer.music.play(-1)

    att=pygame.image.load('football-player (2).png')
    defe=pygame.image.load('keep.png')

    button1 = Button((350,270), (150, 50), (255,0,0), "ATTACK")
    button2 = Button((350,400), (150, 50), (0,0,255), "DEFEND")

    # - mainloop -
    

    clock = pygame.time.Clock()
    running = True

    while running:
        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button1.is_clicked(event):
                stage3(screen)
            if button2.is_clicked(event):
                stage4(screen)

        # - draws -

        bg=pygame.image.load('bgnew1.jpg') 
        screen.blit(bg,(0,0)) 
        button1.draw(screen)
        screen.blit(att,(290,270))
        button2.draw(screen)
        screen.blit(defe,(290,400))
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)

def stage3(screen):
    global ballx,bally,glovex,glovey,life,score

    goal=pygame.image.load('score.png')
    heart=pygame.image.load('heart.png')
    home=pygame.image.load('buthome.png')
    ball=pygame.image.load('football.png')
    keep=pygame.image.load('keeper.png')
    button2 = Button((5, 5), (50, 50), (255,255,255),"")
    mixer.music.load('game_bgm.mp3')
    mixer.music.play(-1)

    score=0
    life=5

    ballx=380
    bally=540
    glovex=360
    glovey=220

    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                
                if event.key==pygame.K_RIGHT:
                    mixer.music.load('ballhit.wav')
                    mixer.music.play()
                    kick_right()
                    
                elif event.key==pygame.K_LEFT:
                    mixer.music.load('ballhit.wav')
                    mixer.music.play()
                    kick_left()
                    
                elif event.key==pygame.K_UP:
                    mixer.music.load('ballhit.wav')
                    mixer.music.play()
                    kick_straight()
                elif event.key==pygame.K_SPACE:
                    if life==0:
                        stage5(screen)
                    else:
                        ballx=380
                        bally=540
                        glovex=360
                        glovey=220

            if button2.is_clicked(event):
                stage1(screen)
            

        # - draws -

        bg=pygame.image.load('background.jpg') 
        screen.blit(bg,(0,0))
        screen.blit(goal,(690,20))
        screen.blit(heart,(590,20))
        screen.blit(keep,(glovex,glovey))
        screen.blit(ball,(ballx,bally))
        button2.draw(screen)
        screen.blit(home,(17,17))
        show_score()
        pygame.display.flip()
        

        # - FPS -

        clock.tick(FPS)

def stage4(screen):
    global ballx,bally,glovex,glovey,score,life

    saves=pygame.image.load('gloves.png')
    heart=pygame.image.load('heart.png')
    home=pygame.image.load('buthome.png')
    ball=pygame.image.load('football.png')
    keep=pygame.image.load('keeper.png')
    button2 = Button((5, 5), (50, 50), (255,255,255),"")

    score=0
    life=5

    ballx=380
    bally=540
    glovex=360
    glovey=220



    # - mainloop -

    clock = pygame.time.Clock()
    running = True

    while running:

        # - events -


        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    glovex=513
                    lst=[380,540,220]
                    ballx=random.choice(lst)
                    bally=220
                    calculate_score()
                elif event.key==pygame.K_LEFT:
                    
                    glovex=207
                    lst=[380,540,220]
                    ballx=random.choice(lst)
                    bally=220
                    calculate_score()
                elif event.key==pygame.K_UP:
                    
                    glovex=360
                    lst=[380,540,220]
                    ballx=random.choice(lst)
                    bally=220
                    calculate_score()
        
                elif event.key==pygame.K_SPACE:
                    if life==0:
                        stage5(screen)
                    else:
                        ballx=380
                        bally=540
                        glovex=360
                        glovey=220
                    
                    

            
                
                    
            if button2.is_clicked(event):
                stage1(screen)
            

        # - draws -

        bg=pygame.image.load('background.jpg') 
        screen.blit(bg,(0,0))
        screen.blit(saves,(690,20))
        screen.blit(heart,(590,20))
        screen.blit(keep,(glovex,glovey))
        screen.blit(ball,(ballx,bally))
        button2.draw(screen)
        screen.blit(home,(17,17))
        show_score()
        pygame.display.flip()

        # - FPS -

        clock.tick(FPS)
        
def stage5(screen):
    mixer.music.load('scoremusic.wav')
    mixer.music.play()
    go=pygame.image.load('gameover.png')
    home=pygame.image.load('buthomebig.png')
    button2 = Button((350,450), (100, 100), (255,255,255),"")

    clock = pygame.time.Clock()
    running = True

    while running:
        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button2.is_clicked(event):
                stage1(screen)

        screen.fill((255,255,255))
        screen.blit(go,(0,0))
        button2.draw(screen)
        screen.blit(home,(375,475))
        pygame.display.flip()
        

        clock.tick(FPS)


def stage6(screen):
    rule=pygame.image.load('rules.jpg')
    button2 = Button((350,545), (100, 40), (0,0,0),"BACK")

    clock = pygame.time.Clock()
    running = True

    while running:
        # - events -

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if button2.is_clicked(event):
                stage1(screen)
            
        screen.blit(rule,(0,0))
        button2.draw(screen)
        pygame.display.flip()
        

        clock.tick(FPS)



# --- main ---

# - init -

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Penalty Shootout Game")

# - start -

stage1(screen)

# - end -


pygame.quit()