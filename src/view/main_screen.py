import pygame
from flask import Flask

from src.view.category_selection_screen import show_category_selection_screen
from ..services.category_services import list_all_categories

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                categories = list_all_categories()
                print(categories)
                show_category_selection_screen(categories)

        screen.fill((255, 255, 255))  # Fundo branco

        text = font.render('Quiz Ciências', True, (0, 0, 0))
        text_rect = text.get_rect(center=(400, 200))
        screen.blit(text, text_rect)

        pygame.draw.rect(screen, (0, 128, 255), (300, 300, 200, 50))  # Botão
        button_text = font.render('Start', True, (255, 255, 255))
        button_text_rect = button_text.get_rect(center=(400, 325))
        screen.blit(button_text, button_text_rect)

        pygame.display.flip()

    pygame.quit()
