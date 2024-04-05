import pygame
import sys
import my_policy_iteration
import value_iteration
import maze_gen_merv
# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Maze Solver")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up fonts
font = pygame.font.Font(None, 36)

# Define Button class
class Button:
    def __init__(self, x, y, width, height, color, text, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.callback = callback

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = font.render(self.text, True, black)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def handle_event(self, event,n):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                pygame.quit()

                self.callback(n)

# Define button callbacks
def button1_callback(n):
    print(n)
    test_maze, test_mdp = maze_gen_merv.main(n,n)
    # print("here")
    my_policy_iteration.main2(test_maze, test_mdp)
    # print("y")

def button2_callback(n):
    test_maze, test_mdp = maze_gen_merv.main(w=n,h=n)

    value_iteration.main2(test_maze, test_mdp)

# Define InputField class
class InputField:
    def __init__(self, x, y, width, height, color, font_size):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = ""
        self.font = pygame.font.Font(None, font_size)
        self.active = False

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, black)
        text_surface = font.render("Enter a number:", True, black)
   
        text_surface = font.render(self.text, True, black)
 

        screen.blit(text_surface, self.rect.move(5, 5))


    def handle_event(self, event):
        m=15
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        if self.active and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
                p=self.text
                m=p
                print(m)
        try:
            number = int(self.text)  # Convert the text to an integer
        except ValueError:
            number = None  # Return None if the text is not a valid number
        return number
# Create buttons
button1 = Button(50, 100, 100, 50, (0, 255, 0), "Policy", button1_callback)
button2 = Button(250, 100, 100, 50, (0, 0, 255), "Value", button2_callback)

# Create input field
input_field = InputField(100, 30, 200, 30, white, 20)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        n=input_field.handle_event(event)
        button1.handle_event(event,n)
        button2.handle_event(event,n)

    #screen.fill(white)

    # Draw input field
    input_field.draw()

    # Draw buttons
    button1.draw()
    button2.draw()

    pygame.display.flip()