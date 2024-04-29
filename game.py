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
WHITE = (235, 235, 208)
BLACK = (119, 148, 85)
RED = (255, 0, 0)  # New color for when a field is clicked


# Größe und Anzahl der Felder
rows = 8
cols = 8
square_size = screen_width // rows


allFields = []




# Hauptprogrammschleife
running = True



class Field():
    def __init__(self, row, col ,color):
        self.row = row
        self.col = col
        self.color = color
        self.piece = None
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.col * square_size, self.row * square_size, square_size, square_size))
    def setPiece(self, piece):
        self.piece = piece
        self.piece.col = self.col
        self.piece.row = self.row
        self.piece.draw()
        
##    def addPiece(self, ):
##        screen.blit(king_image, (piece.col * square_size, piece.row * square_size))  # Beispiel: König auf Feld D4



class Piece():
    def __init__(self, name, start_pos):
        self.name = name
        
        self.start_pos = start_pos
        self.row = start_pos[0]
        self.col = start_pos[1]
        self.image = pygame.image.load("img/"+str(self.name)+".png")
        self.image = pygame.transform.scale(self.image, (square_size-20, square_size-20))
##    def draw(self):
##        screen.blit(self.image, (self.col * square_size, self.row * square_size))  # Beispiel: König auf Feld D4

    def draw(self):
        # Calculate the center position of the square
        square_center_x = self.col * square_size + square_size // 2
        square_center_y = self.row * square_size + square_size // 2

        # Calculate the position to blit the image to center it in the square
        image_x = square_center_x - self.image.get_width() // 2
        image_y = square_center_y - self.image.get_height() // 2

        screen.blit(self.image, (image_x, image_y))
    def getReachableFields(self, allFields):
        reachableFields = []
        
        if "queen" in self.name:
            for f in allFields:
                if (f.row == self.row and f.col != self.col) or (f.col == self.col and f.row != self.row):
                    if f.piece is None:
                        reachableFields.append(f)
            for field in reachableFields:
                print(field.row, field.col)
                
        elif "rook" in self.name:
            print("THE ROOOOOK")
        elif "bishop" in self.name:
            print("THE bishop")
        elif "knight" in self.name:
            print("THE knight")
        elif "king" in self.name:
            print("THE king")
        elif "pawn" in self.name:
            print("THE pawn")
        return reachableFields
        
    

allPieces = [
    Piece("black_pawn",(1,0)),
    Piece("black_pawn",(1,1)),
    Piece("black_pawn",  (1,2)),
    Piece("black_pawn",(1, 3)),
    Piece("black_pawn",(1,4)),
    Piece("black_pawn",(1,5)),
    Piece("black_pawn",(1,6)),
    Piece("black_pawn",(1,7)),
    Piece("black_rook",(0,0)),
    Piece("black_rook",(0,7)),
    Piece("black_knight",(0,1)),
    Piece("black_knight",(0,6)),
    Piece("black_bishop",(0,2)),
    Piece("black_bishop",(0,5)),
    Piece("black_queen",(0,3)),
    Piece("black_king",(0,4)),

    Piece("white_pawn",(6,0)),
    Piece("white_pawn",(6,1)),
    Piece("white_pawn",(6,2)),
    Piece("white_pawn",(6,3)),
    Piece("white_pawn",(6,4)),
    Piece("white_pawn",(6,5)),
    Piece("white_pawn",(6,6)),
    Piece("white_pawn",(6,7)),
    Piece("white_rook",(7,0)),
    Piece("white_rook",(7,7)),
    Piece("white_knight",(7,1)),
    Piece("white_knight",(7,6)),
    Piece("white_bishop",(7,2)),
    Piece("white_bishop",(7,5)),
    Piece("white_queen",(7,3)),
    Piece("white_king",(7,4)),
]

def generate_fields():
    for row in range(rows):
        for col in range(cols):
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = BLACK
            allFields.append(Field(row, col, color))

def drawBoard():
    for field in allFields:
        field.draw()
        for piece in allPieces:
            if piece.col == field.col and piece.row == field.row:
                field.setPiece(piece)
    allFields[23].setPiece(allPieces[14])
                
##                field.draw()
##                if row == 0 or row == 7:
##                    field.addPiece()
                

def get_clicked_field(pos):
    x, y = pos
    row = y // square_size
    col = x // square_size
    return row, col
def pieceClickedHandler():
    #ist am Zug? Hat das Feld einen Piece? Dann berechne, welche züge möglich sind
    
    
    # Get the position of the mouse click
    clicked_pos = pygame.mouse.get_pos()
    # Get the row and column of the clicked field
    clicked_row, clicked_col = get_clicked_field(clicked_pos)
    # Change the color of the clicked field to red
    field_index = clicked_row * cols + clicked_col
    if allFields[field_index].piece is not None:
        allFields[field_index].color = RED
        rFields = allFields[field_index].piece.getReachableFields(allFields)
        for f in rFields:
            f.color = RED
            
##    print("Row: ",allFields[field_index].row)
##    print("Col: ",allFields[field_index].col)

def main():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    pieceClickedHandler()
               
                  
                  

        # Schachbrett zeichnen
        drawBoard()


        # Bildschirm aktualisieren
        pygame.display.flip()

generate_fields()

main()
# Pygame beenden
pygame.quit()
sys.exit()
