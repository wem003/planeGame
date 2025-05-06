# import pygame
import pygame
import random
from pygame import Color
from pygame.math import Vector2
import time

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)

shipSpeed = 8
level = 1
enemyDelay = 250
highScores = []
highScore = 0

# Player object
class Player(pygame.sprite.Sprite):

    def __init__(self):

        shipXSize = 112
        shipYSize = 37

        super(Player, self).__init__()
        self.images = []
        ship1 = pygame.image.load('./graphics/rocket1.png').convert()
        ship1 = pygame.transform.smoothscale(ship1, (shipXSize, shipYSize))
        self.images.append(ship1)

        ship2 = pygame.image.load('./graphics/rocket2.png').convert()
        ship2 = pygame.transform.smoothscale(ship2, (shipXSize, shipYSize))
        self.images.append(ship2)

        ship3 = pygame.image.load('./graphics/rocket3.png').convert()
        ship3 = pygame.transform.smoothscale(ship3, (shipXSize, shipYSize))
        self.images.append(ship3)

        self.index = 0
        self.surf = self.images[self.index]

        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.y = 450


    # Move the sprite based on user keypresses
    def update(self, pressed_keys):

        global shipSpeed

        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        self.surf = self.images[self.index]

        if self.index >= len(self.images):
            self.index = 0
        self.surf = self.images[self.index]

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -shipSpeed)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, shipSpeed)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-shipSpeed, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(shipSpeed, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


    # Move the sprite based on user joystick
    def update_joystick(self, horiz_axis_pos, vert_axis_pos):

        global shipSpeed

        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        self.surf = self.images[self.index]


        # if self.index >= len(self.images):
        #     self.index = 0
        # self.surf = self.images[self.index]

        # x postion
        self.rect.move_ip(int(horiz_axis_pos * shipSpeed), 0)

        # y postion
        self.rect.move_ip(0, int(vert_axis_pos * shipSpeed))

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.speed = random.randint(5, 20)
        if self.speed < 10:
            self.surf = pygame.image.load("./graphics/laser1.png").convert()
        else:
            self.surf = pygame.image.load("./graphics/laser2.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )


    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Define the asteroid object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super(Asteroid, self).__init__()
        asteroidNumber=random.randint(1,3)
        self.surf = pygame.image.load("./graphics/asteroid" + str(asteroidNumber) + ".png").convert()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        # The starting position is randomly generated
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

        self.speed = random.randint(5, 15)

    # Move the Asteroid based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


def print_text(surface, text, font, color=Color("tomato")):
    text_surface = font.render(text, True, color)

    rect = text_surface.get_rect()
    rect.center = Vector2(surface.get_size()) / 2

    surface.blit(text_surface, rect)


def print_highscore1(surface, text, font, color=Color("tomato")):
    text_surface = font.render(text, True, color)

    rect = text_surface.get_rect()
    rect.center = Vector2(525)


    surface.blit(text_surface, rect)

def print_highscore2(surface, text, font, color=Color("tomato")):
    text_surface = font.render(text, True, color)

    rect = text_surface.get_rect()
    rect.center = Vector2(625)

    surface.blit(text_surface, rect)

def print_highscore3(surface, text, font, color=Color("tomato")):
    text_surface = font.render(text, True, color)

    rect = text_surface.get_rect()
    rect.center = Vector2(725)

    surface.blit(text_surface, rect)


def print_end_text(surface, text, font, color=Color("tomato")):
    text_surface = font.render(text, True, color)

    rect = text_surface.get_rect()
    rect.center = Vector2(850)

    surface.blit(text_surface, rect)

def print_score(surface, text, font, color=Color("tomato")):
    text_surface = font.render(text, True, color)

    rect = text_surface.get_rect()
    rect.left = 25
    rect.top = 25
    surface.blit(text_surface, rect)



# init pygame
pygame.init()
pygame.display.set_caption("Space: Get the Heck Out of the Way")

# constants for screen width and height
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

# create screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, enemyDelay)

ADDASTEROID = pygame.USEREVENT + 2
pygame.time.set_timer(ADDASTEROID, 1000)

player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

# Setup for sounds. Defaults are good.
pygame.mixer.init()

pygame.mixer.music.load("./sounds/Apoxode.mp3")
pygame.mixer.music.play(loops=-1)


move_up_sound = pygame.mixer.Sound("./sounds/harddriveBroken.ogg")
move_down_sound = pygame.mixer.Sound("./sounds/harddriveBroken.ogg")
collision_sound = pygame.mixer.Sound("./sounds/explosion.ogg")

font = pygame.font.Font(None, 64)
scoreFont = pygame.font.Font(None, 32)
scoreFont2 = pygame.font.Font(None, 24)
endFont = pygame.font.Font(None, 32)
message = ""
score = 0
scoreCounter = 30
playerLives = 3
ivFrame = 0

# Setup the clock for a decent framerate
clock = pygame.time.Clock()


# Count the joysticks the computer has
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print("Error, I didn't find any joysticks.")
else:
    # Use joystick #0 and initialize it
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()


startPause = 60

startGame = False

while not startGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        startButton = my_joystick.get_button(9)
        if startButton:
            startGame = True

    screen.fill((255, 255, 255))

    titleImage = pygame.image.load("./graphics/space_title.png").convert()
    titleImage = pygame.transform.smoothscale(titleImage, (1200, 900))
    screen.blit(titleImage, (0, 0))
    pygame.display.flip()
    clock.tick(60)


updateHighScore = True

while running:

    if startPause > 0:
        startPause = startPause - 1

    # inspect event queue
    for event in pygame.event.get():
        # did the user hit a key
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
                running = False
        # Add a new enemy?
        elif event.type == ADDENEMY and playerLives > 0 and startPause == 0:
            newEnemyDelay = enemyDelay-(level*50)
            if newEnemyDelay == 0:
                newEnemyDelay = 30
           # print("newEnemyDelay -->" + str(newEnemyDelay))
            pygame.time.set_timer(ADDENEMY, newEnemyDelay)
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        # Add a new asteroid?
        elif event.type == ADDASTEROID:
            # Create the new cloud and add it to sprite groups
            new_asteroid = Asteroid()
            asteroids.add(new_asteroid)
            all_sprites.add(new_asteroid)

    # As long as there is a joystick
    if joystick_count != 0:
        # This gets the position of the axis on the game controller
        # It returns a number between -1.0 and +1.0
        horiz_axis_pos = my_joystick.get_axis(0)
        vert_axis_pos = my_joystick.get_axis(1)
        player.update_joystick(horiz_axis_pos, vert_axis_pos)
    else:
        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()
        # update player sprite
        player.update(pressed_keys)


    # Update enemy position
    enemies.update()
    asteroids.update()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Check if any enemies have collided with the player
    if ((pygame.sprite.spritecollideany(player, enemies)) and (ivFrame <= 0) and playerLives > 0):
        playerLives = playerLives - 1
        collision_sound.play()
        ivFrame = 20

    scoreCounter = scoreCounter - 1

    if scoreCounter <= 0 and playerLives > 0:
        scoreCounter = 30
        score = score + 10
        if score % 50 == 0:
            level = level + 1


    # Do we need to get faster?  Every 50 points shave 5ms * level off enemy delay


    message = "Score :" + str(score) + "     Lives: " + str(playerLives) + "     Level: " + str(level) + "     High Score: " + str(highScore)
    print_score(screen, message, scoreFont)

    startButton = my_joystick.get_button(9)
    backButton = my_joystick.get_button(8)

    if playerLives <= 0:
        message = "You lost! Your score was: " + str(score)

        if joystick_count != 0 :
            message2 = "Start to play again, back to quit"
        else:
            message2 = "Enter to play again"
        print_text(screen, message, font)
        print_end_text(screen, message2, endFont)

        # If so, then remove the player and stop the loop
        player.kill()
        level = 1
        # Stop any moving sounds and play the collision sound
        move_up_sound.stop()
        move_down_sound.stop()
        newEnemyDelay = enemyDelay

        if updateHighScore:
            highScores.append(score)
            highScores.sort(reverse=True)
            newHighScores = []
            if len(highScores) > 5:
                for n in range(0, 5):
                    newHighScores.append(highScores[n])
                highScores = newHighScores

            highScore = highScores[0]
            print("High Scores:", highScores)

            updateHighScore = False


        if len(highScores) > 0:
            #print("Hi 1")
            print_highscore1(screen, "High Score 1: " + str(highScores[0]), scoreFont2)
        if len(highScores) > 1:
            #print("Hi 2")
            print_highscore2(screen, "High Score 2: " + str(highScores[1]), scoreFont2)
        if len(highScores) > 2:
            #print("Hi 3")
            print_highscore3(screen, "High Score 3: " + str(highScores[2]), scoreFont2)

        if startButton:


            updateHighScore = True
            playerLives = 3
            score = 0
            #time.sleep(2)
            player = Player()

            for x in all_sprites:
                x.kill()

            # make a new player
            all_sprites.add(player)
            startPause = 60



        if backButton:
            player.kill()
            running = False

    # update display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(30)
    ivFrame = ivFrame - 1

#time.sleep(5)
pygame.mixer.music.stop()
pygame.mixer.quit()





