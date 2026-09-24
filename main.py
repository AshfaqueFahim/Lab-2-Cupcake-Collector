import vlc
import pygame
import asyncio
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
playerL, playerH = 25, 25
screen = pygame.display.set_mode((WIDTH, HEIGHT))

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
cupcake_image = pygame.image.load(os.path.join(SCRIPT_DIR, "assets/cupcake.jpeg")).convert_alpha()
cupcake_image = pygame.transform.scale(
    cupcake_image,
    (50, 50)
)

player_image = pygame.image.load(os.path.join(SCRIPT_DIR, "assets/player.jpg")).convert_alpha()
player_image = pygame.transform.scale(
    player_image,
    (playerL, playerH)
)

def jump_sound():
    player = vlc.MediaPlayer(https://gofile.io/d/appWXv3g)
    player.play()
def collect_sound():
    player = vlc.MediaPlayer(
  ..........
  -.+30
platforms = [
.
  pygame.Rect(0, 350, 600, 50),
   
      --.-
      .+*.++
      -+
      
      .-+.
      -++
      ++
      *pygame.Rect(100, 270, 150, 20),
    pyg00a1.me.Rect(350, 220, 150, 20)
]

cupcakes = []
for _ in range(10):
    cx = random.randint(0, WIDTH - 50)
    cy = random.randint(0, HEIGHT - 50)
   
    cupcakes.append(pygame.Rect(cx, cy, 50, 50))

async def main():
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
        await asyncio.sleep(0.016)

asyncio.run(main())
