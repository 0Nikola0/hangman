import pygame
import time


# ###### WORD FOR GUESSING ######
#      It must be uppercase
word = list('PYTHON')
guessed_letters = ['_' for i in word]
guess = ''
guesses = []
mistakes = 0
#################################
screenWidth, screenHeight = 600, 600
pygame.init()
pygame.display.set_caption('Hangman')
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

FONT_1 = pygame.font.SysFont('Arial', 35, True)
FONT_2 = pygame.font.SysFont('Arial', 60, True)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (70, 70, 70)
RED = (255, 0, 0)
# Global position x and y, to easily repostion all parts at once when needed
gpx, gpy = 150, 0


def draw_holder(color=BLACK):
    pygame.draw.line(screen, color, (gpx + 40, gpy + 446), (gpx + 220, gpy + 446), 9)   # lower horizontal line
    pygame.draw.line(screen, color, (gpx + 50, gpy + 446), (gpx + 70, gpy + 406), 10)   # lower left angle line
    pygame.draw.line(screen, color, (gpx + 90, gpy + 446), (gpx + 70, gpy + 406), 10)   # lower right angle line
    pygame.draw.line(screen, color, (gpx + 70, gpy + 180), (gpx + 70, gpy + 442), 9)    # vertical line
    pygame.draw.line(screen, color, (gpx + 66, gpy + 180), (gpx + 200, gpy + 180), 9)   # upper horizontal line
    pygame.draw.line(screen, color, (gpx + 100, gpy + 180), (gpx + 70, gpy + 210), 10)  # upper agnle line
    pygame.draw.line(screen, color, (gpx + 179, gpy + 180), (gpx + 179, gpy + 201), 6)  # 2nd small vertical line


def draw_stickman(misses, color=BLACK):
    if misses >= 1:
        pygame.draw.circle(screen, color, (gpx + 180, gpy + 235), 33, 9)  # head
        if misses >= 2:
            pygame.draw.line(screen, color, (gpx + 180, gpy + 265), (gpx + 180, gpy + 352), 9)  # body
            if misses >= 3:
                pygame.draw.line(screen, color, (gpx + 180, gpy + 265), (gpx + 155, gpy + 317), 9)  # left arm
                if misses >= 4:
                    pygame.draw.line(screen, color, (gpx + 180, gpy + 265), (gpx + 205, gpy + 317), 9)  # right arm
                    if misses >= 5:
                        pygame.draw.line(screen, color, (gpx + 180, gpy + 350), (gpx + 155, gpy + 412), 9)  # left leg
                        if misses >= 6:
                            pygame.draw.line(screen, color, (gpx + 180, gpy + 350), (gpx + 205, gpy + 412), 9)  # right leg


def draw_word(gword, pos, color=BLACK, size='small'):
    font = FONT_1 if size == 'small' else FONT_2
    word_block = font.render(gword, True, color)
    word_pos = word_block.get_rect()
    word_pos.center = pos
    screen.blit(word_block, word_pos)


def dead_scene():
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        screen.fill(BLACK)
        draw_word("You ded", (300, 300), color=RED, size='big')
        pygame.display.flip()


def play_scene():
    global guessed_letters, guess, guesses, mistakes

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # If a key is pressed
            if event.type == pygame.KEYDOWN:
                # If the key is a letter (for example if it's not ENTER, SPACE, etc.)
                if event.unicode.isalpha():
                    guess = event.unicode
                    # We convert the letter to uppercase
                    guess = guess.upper()
                    # If you haven't guessed the letter before
                    if guess not in guesses:
                        # We add the guess in already guessed letters list
                        guesses.append(guess)
                        # If the guess is in the word
                        if guess in word:
                            # We check in which place it is
                            for i, letter in enumerate(word):
                                if guess == letter:
                                    # We replace the underscore ('_') with the correct letter
                                    guessed_letters[i] = guess
                        # if the guess is not in the word
                        else:
                            # We increase the mistakes made
                            mistakes += 1

        screen.fill(GRAY)
        draw_holder()
        draw_stickman(mistakes)
        # To make string from the list we use " ".join(guessed_letters), with space between each letter
        draw_word(" ".join(guessed_letters), (300, 520))
        pygame.display.flip()

        if mistakes == 6:
            time.sleep(0.5)
            running = dead_scene()


if __name__ == "__main__":
    play_scene()
