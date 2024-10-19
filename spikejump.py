import pygame
from pygame.mixer import music, Sound
from math import sqrt
from random import randint

pygame.init()


# Screen and background
screen = pygame.display.set_mode((1200, 600))
background_picture = pygame.image.load("./assets/art/background.png")

# Window title and icon
pygame.display.set_caption("Spike Jump")
window_icon = pygame.image.load("./assets/art/window-icon.png")
pygame.display.set_icon(window_icon)

# Music and sound effects
music.load("./assets/sounds/backgroundSong.wav")
music.play(-1)
point_sound = Sound("./assets/sounds/pointSound.wav")
death_sound = Sound("./assets/sounds/deathSound.wav")

# Player
player_icon = pygame.image.load("./assets/art/player.png")
player_x = 200
player_y = 450
player_width = player_icon.get_width()
player_height = player_icon.get_height()

# Physics
gravity = 0.5
player_velocity_y = 0
jump_force = -12
is_jumping = False

# Spike
spike_icon = pygame.image.load("./assets/art/spike.png")
spike_width = spike_icon.get_width()
spike_height = spike_icon.get_height()
spike_x = 1200
spike_y = 450
spike_speed = 6

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# Function to display the score
def show_score():
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Function to reset the game
def reset_game():
    global spike_x, player_y, player_velocity_y, is_jumping, score
    spike_x = 1200
    player_y = 450
    player_velocity_y = 0
    is_jumping = False
    score = 0
    death_sound.play()

# Main loop
running = True
while running:

    screen.blit(background_picture, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if not is_jumping:
                    is_jumping = True
                    player_velocity_y = jump_force

    # Player jumping mechanics
    if is_jumping:
        player_velocity_y += gravity
        player_y += player_velocity_y

        if player_y >= 450:
            player_y = 450
            is_jumping = False

    # Spike reset and scoring
    if spike_x + spike_width < 0:
        spike_x = 1200
        score += 1
        point_sound.play()

    spike_x -= spike_speed

    # Collision detection
    if (spike_x < player_x + player_width < spike_x + spike_width) and (player_y + player_height >= spike_y):
        reset_game()

    # Draw player and spike
    screen.blit(player_icon, (player_x, player_y))
    screen.blit(spike_icon, (spike_x, spike_y))

    show_score()

    pygame.display.update()

pygame.quit()