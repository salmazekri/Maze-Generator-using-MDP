import pygame
import sys

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame GUI")

# Set up fonts
font = pygame.font.Font(None, 36)

# Text box parameters
text_box_width, text_box_height = 200, 30
text_box_x, text_box_y = (screen_width - text_box_width) // 2, 100
text_box_rect = pygame.Rect(text_box_x, text_box_y, text_box_width, text_box_height)
text_box_text = ""
text_box_active = False

# Button parameters
button_width, button_height = 80, 40
button_x, button_y = (screen_width - button_width) // 2, 150
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

# Function to be called when the button is clicked
def on_button_click():
    print("Button Clicked! Text entered:", text_box_text)

# Main loop
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if text_box_rect.collidepoint(event.pos):
                text_box_active = not text_box_active
            elif button_rect.collidepoint(event.pos):
                on_button_click()
            else:
                text_box_active = False

        if event.type == pygame.KEYDOWN:
            if text_box_active:
                if event.key == pygame.K_RETURN:
                    print("Entered text:", text_box_text)
                    text_box_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    text_box_text = text_box_text[:-1]
                else:
                    text_box_text += event.unicode

    # Update the text box
    text_surface = font.render(text_box_text, True, BLACK)
    text_box_width = max(200, text_surface.get_width() + 10)
    text_box_rect.w = text_box_width

    # Draw text box and button
    pygame.draw.rect(screen, BLACK, text_box_rect, 2)
    screen.blit(text_surface, (text_box_rect.x + 5, text_box_rect.y + 5))

    pygame.draw.rect(screen, BLACK, button_rect)
    button_text = font.render("Click", True, WHITE)
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))

    pygame.display.flip()
