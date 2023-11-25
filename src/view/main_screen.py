import pygame
from flask import Flask

from src.view.category_selection_screen import show_category_selection_screen

app = Flask(__name__)


def show_main_screen():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Quiz Ciências')

    font = pygame.font.Font(None, 36)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                button_rect = pygame.Rect(300, 300, 200, 50)
                if button_rect.collidepoint(mouse_pos):
                    show_category_selection_screen()  # Passe as categorias para a função

        screen.fill((255, 255, 255))  # Fundo branco

        text = font.render('Quiz Ciências', True, (0, 0, 0))
        text_rect = text.get_rect(center=(400, 200))
        screen.blit(text, text_rect)

        button_rect = pygame.Rect(300, 300, 200, 50)  # Retângulo do botão
        pygame.draw.rect(screen, (0, 128, 255), button_rect)  # Botão
        button_text = font.render('Start', True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, button_text_rect)

        # Verifica se o cursor está sobre o botão
        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()

    pygame.quit()

    show_category_selection_screen()
