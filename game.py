"""
This is a game that helps people learn about history, 
and create habits of always looking 
at the bigger picture when it comes down to history.
the player presses space to jump over the obsicales and the player must collect
all of the good history artifacts to win.
you play as a character named "history ball" whose goal is to collect all of the good artifacts and 
avoid the bad ones.
Written by Jahsan watkins , Pujan, Abel
"""
import pygame
import random
from sys import exit

pygame.init()

#create screen 
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("history game ")

#the amount of health the player has
health = 100

#start Screen
#all of the functions for the game 
start_screen = pygame. image.load ("assets/start_screen.png").convert ()
play_btn = pygame.image.load("Assets/play.png").convert_alpha()
play_rect = play_btn.get_rect(center= (400, 350))
#Lose/win screens
lose = pygame.image.load("assets/game over.png").convert_alpha() 
play_again_btn = pygame.image.load("assets/play.png").convert_alpha()
win = pygame.image.load("assets/you win.png").convert()
play_again_btn = pygame.image.load("assets/play.png").convert_alpha()
replay_btn = pygame.image.load("assets/replay.png").convert_alpha()
replay_rect = replay_btn.get_rect(center= (250, 300))
exit_btn = pygame.image.load("assets/exit.png").convert_alpha()
exit_rect = exit_btn.get_rect(center= (500, 300)) 
#the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(). __init__()
        self.image = pygame.image.load("assets/Elf.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = (200, 400))
        self.gravity = 0

    def player_input(self): 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 360:
            self.gravity = -25

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity 
        if self.rect.bottom >= 360:
            self.rect.bottom = 360

    def update(self):
        self.player_input()
        self.apply_gravity()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        # Position the obstacle just off-screen to the right
        start_x = random.randint(850, 1000)
        
        if type == "donut":
            self.image = pygame.image.load("assets/donut.png").convert_alpha()
        elif type == "ice_cream":
            self.image = pygame.image.load("assets/ice_cream.png").convert_alpha()
            
        elif type == "soda":
            self.image = pygame.image.load("assets/soda.png").convert_alpha()
        else: 
            self.image = pygame.image.load("assets/cookie.png").convert_alpha()
            
        self.rect = self.image.get_rect(midbottom = (start_x, 360))

    # De-indent these methods so they belong to the class, not __init__
    def update(self):
        self.rect.x -= 5
        self.destroy()
        
    def destroy(self):
        if self.rect.right <= 0:
            self.kill()




   
#the target class AKA enemy class
class Target(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.start = random.randint(800, 1000)
        if type == "apple":
            self.image = pygame.image.load("assets/apple.png").convert_alpha()
        elif type == "broccoli":
            self.image = pygame.image.load("assets/broccoli.png").convert_alpha()
        else:
            self.image = pygame.image.load("assets/broccoli.png").convert_alpha()

        self.rect = self.image.get_rect(center=(700, 200))

    def update(self):
        self.rect.x -= 5
        self.destroy()

    def destroy(self):
        if self.rect.x <= -1:
            self.kill()

#initialize variables
game_screen = 0 
score_font = pygame.font.Font(None, 36)
def check_collisions():
     global score
     global health
     if player_group.sprite:
        collided_target = pygame.sprite.spritecollide(player_group.sprite, target_group, True)
        if collided_target:
            score += 10    
            print(score)
        collided_obstacle = pygame.sprite.spritecollide( player_group.sprite, obstacle_group, True)
        if collided_obstacle:
            health -= 10
def display_score():
    score_surf = score_font.render("score:" + str(score), True, (50, 50, 50))
    score_rect = score_surf.get_rect(center = (100, 50))  
    screen.blit(score_surf, score_rect)    
def display_health():
    health_surf = score_font.render("Health: " + str(health), True, (50, 50, 50))
    health_rect = health_surf.get_rect(center = (100, 80))
    screen.blit(health_surf, health_rect)
target_group = pygame.sprite.Group()
player_group = pygame.sprite.GroupSingle()
player_group.add(Player())
score = 0
score_font = pygame.font.Font(None, 36)
obstacle_group = pygame.sprite.Group()
clock = pygame.time.Clock()
ground = pygame.image.load("assets/grass.png").convert()
sky = pygame.image.load("assets/sky.png").convert()
endscreen = pygame.image.load("assets/game over.png").convert()
start_screen = pygame.image.load("assets/start_screen.png").convert()
win_screen = pygame.image.load("assets/win_screen.png").convert()
pygame.init()

#playbackground music
pygame.mixer.init()
pygame.mixer.music.load("assets/firesong11.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


#the looping aspects for the game (Ex: game background, target spawning, and button pressing)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
        if event.type == pygame.KEYDOWN:
        # Check if that key was the P key
            if event.key == pygame.K_p:
                game_screen = 1
                health = 100
                score = 0
                
            
    if game_screen == 0:
        screen.blit(start_screen, (0,0))
    if game_screen == 1 :
        #background 
        screen.blit(ground, (0, 350))
        screen.blit(sky, (0, 00))
        player_group.draw(screen)
        player_group.update()
        
        target_group.draw(screen)
        target_group.update()
        if not target_group:
            i = random.randint(0,2)
            choices = ["apple", "broccoli", "carrot"]
            target_group.add(Target(choices[i]))
            
        #obstacles
        obstacle_group.draw(screen)
        obstacle_group.update()
        if not obstacle_group:
            i = random.randint(0,2)
            choices = ['cookie','ice_cream','donut']
            obstacle_group.add(Obstacle(choices[i]))
        
        check_collisions()
        display_score()
        display_health()
        if health <= 0:
            game_screen = 2
        if score >= 150:
            game_screen = 3
    if game_screen == 2: 
        screen.blit(endscreen, (0, 00))
    if game_screen == 3: 
        screen.blit(win_screen, (0, 00))
      
    pygame.display.update()
    clock.tick(60)
    


