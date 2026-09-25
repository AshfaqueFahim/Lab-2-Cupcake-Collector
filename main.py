import sys
import pygame
import asyncio
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
playerL, playerH = 25, 25
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

cupcake_image = pygame.image.load("assets/chopped cheese.png").convert_alpha()
cupcake_image = pygame.transform.scale(
    cupcake_image,
    (50, 50)
)

player_image = pygame.image.load("assets/mamdani.png").convert_alpha()
player_image = pygame.transform.scale(
    player_image,
    (playerL, playerH)
)

jump_sound = pygame.mixer.Sound("assets/sonic-pad-bounce.wav")
collect_sound = pygame.mixer.Sound("assets/money-soundfx.wav")

platforms = [
    pygame.Rect(0, 350, 600, 50),
    pygame.Rect(100, 270, 150, 20),
    pygame.Rect(350, 220, 150, 20)
]
platform_speeds = [0, 2, -2]

cupcakes = []
for _ in range(3):
    cx = random.randint(0, WIDTH - 50)
    cy = random.randint(0, HEIGHT - 50)
   
    cupcakes.append(pygame.Rect(cx, cy, 50, 50))

async def main():
    global playerL, playerH
    score = 0
    
    player_rect = pygame.Rect(50, 300, playerL, playerH)
    
    player_dx = 0
    player_dy = 0
    player_speed = 3

    gravity = 0.3
    jump_speed = -10
    
    is_grounded = False
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                 
        keys = pygame.key.get_pressed()
        
        player_dx = 0
        
        if keys[pygame.K_LEFT]:
            player_dx = -player_speed
        if keys[pygame.K_RIGHT]:
            player_dx = player_speed
        if keys[pygame.K_UP] and is_grounded:
            player_dy = jump_speed
            is_grounded = False
            jump_sound.play()
        
        player_rect.x += player_dx
        
        if player_rect.left < 0: 
            player_rect.left = 0
        if player_rect.right > WIDTH:
            player_rect.right = WIDTH
            
        for i in range(len(platforms)):
            platforms[i].x += platform_speeds[i]
            if platforms[i].left < 0 or platforms[i].right > WIDTH:
                platform_speeds[i] = -platform_speeds[i]

        player_dy += gravity
        
        player_rect.y += player_dy
        is_grounded = False  
   
        for platform in platforms:
            if player_rect.colliderect(platform):
                if player_dy > 0:
                    player_rect.bottom = platform.top
                    player_dy = 0
                    is_grounded = True
                elif player_dy < 0:
                    player_rect.top = platform.bottom
                    player_dy = 0

        for cupcake in cupcakes[:]:
            if player_rect.colliderect(cupcake):
                cupcakes.remove(cupcake)
                cx = random.randint(0, WIDTH - 50)
                cy = random.randint(0, HEIGHT - 50)
                cupcakes.append(pygame.Rect(cx, cy, 50, 50))
                score += 1
                playerL += 10
                playerH += 10
                collect_sound.play()
            
        screen.fill((0, 255, 0)) 
        
        for platform in platforms:
            pygame.draw.rect(
            screen,
            (100, 180, 100),
            platform
        )
        
        for cupcake in cupcakes:
            screen.blit(
            cupcake_image,
            (cupcake.x, cupcake.y)
        )

        font = pygame.font.Font(None, 50)
        text_surface = font.render("score: " + str(score), False, (255, 255, 255))
        screen.blit(text_surface, (0, 0))

        screen.blit(player_image, player_rect)

        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()

asyncio.run(main())
