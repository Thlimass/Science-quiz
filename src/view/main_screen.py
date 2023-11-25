import pygame
from src.view.category_selection_screen import show_category_selection_screen

def show_main_screen():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Quiz Ciências')

    font = pygame.font.Font('angrybirds.ttf', 80)  # Aumenta o tamanho da fonte

    background_color = (173, 216, 230)
    button_color = (65, 105, 225)
    hover_color = (50, 205, 50)  # Alterada para verde

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                button_rect = pygame.Rect(300, 275, 200, 100)
                if button_rect.collidepoint(mouse_pos):
                    show_category_selection_screen()

        screen.fill(background_color)

        text = font.render('Quiz Ciências', True, (0, 0, 0))
        text_rect = text.get_rect(center=(400, 200))
        screen.blit(text, text_rect)

        button_rect = pygame.Rect(300, 275, 200, 100)
        if button_rect.collidepoint(pygame.mouse.get_pos()):  # Verifica se o mouse está sobre o botão
            pygame.draw.rect(screen, hover_color, button_rect)  # Muda para a cor verde
        else:
            pygame.draw.rect(screen, button_color, button_rect)  # Mantém a cor azul
        button_text = font.render('Start', True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, button_text_rect)

        pygame.display.flip()

    pygame.quit()

    show_category_selection_screen()
