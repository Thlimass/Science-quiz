# src/game/game_screen.py
import pygame


def run_game_screen(categories):
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Selecione uma Categoria')

    font = pygame.font.Font(None, 36)

    category_y = 50
    selected_category = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for category in categories:
                    text_rect = font.render(category, True, (0, 0, 0)).get_rect(topleft=(50, category_y))
                    if text_rect.collidepoint(mouse_pos):
                        selected_category = category
                        running = False
                        break
                category_y += 50

        screen.fill((255, 255, 255))

        for category in categories:
            render_text(category, font, (0, 0, 0), screen, 50, category_y)
            category_y += 50

        pygame.display.flip()

    pygame.quit()

    return selected_category


def render_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)
