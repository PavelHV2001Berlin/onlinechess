import pygame
import sys

# Initialisierung von Pygame
pygame.init()

# Bildschirm erstellen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Schachbrett mit Pygame")

# Farben definieren
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Größe und Anzahl der Felder
rows = 8
cols = 8
square_size = screen_width // rows


king_image = pygame.image.load("img/black_king.png")
king_image = pygame.transform.scale(king_image, (square_size, square_size))


# Hauptprogrammschleife
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Schachbrett zeichnen
    for row in range(rows):
        for col in range(cols):
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            pygame.draw.rect(screen, color, (col * square_size, row * square_size, square_size, square_size))

    screen.blit(king_image, (3 * square_size, 3 * square_size))  # Beispiel: König auf Feld D4

    # Bildschirm aktualisieren
    pygame.display.flip()

# Pygame beenden
pygame.quit()
sys.exit()
