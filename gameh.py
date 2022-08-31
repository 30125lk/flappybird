import pygame
from random import*
#py installerpygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)
pygame.init()
def bird_animation():
    new_bird = birds[animation]
    new_bird_rect = new_bird.get_rect(center = (80, bird_hb.centery))
    return new_bird, new_bird_rect
pygame.mixer.music.load('sound/roll.mp3')
pygame.mixer.music.play(-1)
wing = pygame.mixer.Sound('sound/wing.wav')
die = pygame.mixer.Sound('sound/die.wav')
hit = pygame.mixer.Sound('sound/hit.wav')
point = pygame.mixer.Sound('sound/point.wav')
pygame.display.set_caption('Flapping Berds')

window = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()
bg = pygame.image.load("img/background.png")
base = pygame.image.load('img/base.png')
pipe = pygame.image.load('img/pipe.png')
birdmid = pygame.image.load('img/bluebird.png')
birdup = pygame.image.load('img/bluebird-up.png')
birddown = pygame.image.load('img/bluebird-down.png')
birds = [birdmid, birddown, birdup]
animation = 0
bird = birds[animation]
pipe_flip = pygame.transform.flip(pipe, False, True)
message = pygame.image.load('img/message.png')
message_hb = message.get_rect(center = (144,256))
bird_hb = bird.get_rect(center = (50, 256))
ptica = pygame.USEREVENT
pygame.time.set_timer(ptica, 80)
pipe_x = 300
pipe_y = 350
base_x = 0
gravity = 0.2
speed = 0
height = [240, 260, 280, 300, 320, 340, 360, 380, 400]
score = 0

game_active = False
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            quit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                speed = 0 
                speed -= 5
                wing.play()
            if i.key == pygame.K_SPACE and game_active == False:
                game_active = True
                bird_hb.center = (50, 256)
                pipe_x = 300
                pipe_y = 350
                speed = 0
                score = 0
        if i.type == ptica:
            if animation < 2:
                animation += 1
            else:
                animation = 0
    bird, bird_hb = bird_animation()
    bird_flip = pygame.transform.rotozoom(bird, -speed*4,1)
    window.blit(bg, (0, 0))
    if game_active:
        window.blit(bird_flip, (bird_hb))
        speed += gravity
        bird_hb.centery += speed
        pipe__hb = pipe.get_rect(midtop = (pipe_x, pipe_y))
        pipe__hb2 = pipe_flip.get_rect(midbottom = (pipe_x, pipe_y - 150))
        window.blit(pipe, pipe__hb)
        window.blit(pipe_flip, pipe__hb2)
    
        pipe_x -= 2
        if pipe_x <= -50:
            pipe_x = 300
            pipe_y = choice(height)

        if bird_hb.colliderect(pipe__hb) or bird_hb.colliderect(pipe__hb2):
            game_active = False
            hit.play()
        if bird_hb.top <= 0 or bird_hb.bottom >= 450:
            game_active = False
            die.play()
        if pipe__hb.centerx == 50:
            score += 1
            point.play()
        window.blit(base, (base_x, 450))
        base_x -= 1
        if base_x <= -20:
            base_x = 0
    
       
    else:
        window.blit(message, message_hb)
    font = pygame.font.Font('04B_19 (2).TTF', 75)
    text = font.render(str(score), True, (250,250,250))
    window.blit(text, (130,30))
    pygame.display.update()
    clock.tick(120)

