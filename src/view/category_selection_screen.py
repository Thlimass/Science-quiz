import pygame
import requests

from src.view.question_screen import show_questions_by_category_screen


def show_category_selection_screen():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Exibindo Lista')

    font = pygame.font.Font('Purpose.ttf', 50)  # Aumenta o tamanho da fonte
    white = (255, 255, 255)
    black = (0, 0, 0)
    hover_color = (50, 205, 50)  # Alterada para verde
    background_color = (173, 216, 230)  # Cor de fundo da tela

    response = requests.get('http://127.0.0.1:5000/category')
    if response.status_code == 200:
        categories_list = response.content
    categories = [item['category_name'] for item in eval(categories_list.decode())]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                start_y = (screen.get_height() - (len(categories) * 60)) // 2  # Altera o tamanho para 60 pixels
                category_height = 60  # Altura da categoria aumentada

                clicked_index = (mouse_pos[1] - start_y) // category_height

                if 0 <= clicked_index < len(categories):
                    clicked_category = categories[clicked_index]
                    show_questions_by_category_screen(clicked_category)
                    running = False  # Sai do loop ao chamar a próxima tela

        screen.fill(background_color)  # Define o fundo com a nova cor

        # Define o tamanho e espaçamento dos retângulos
        rect_width, rect_height = 500, 60  # Aumenta o tamanho do retângulo

        # Calcula a posição inicial para centralizar na tela
        total_height = len(categories) * (rect_height + 10)  # Mantém o espaçamento vertical
        start_y = (screen.get_height() - total_height) // 2

        for category in categories:
            # Cria um retângulo para cada item
            rect = pygame.Rect((screen.get_width() - rect_width) // 2, start_y, rect_width, rect_height)

            # Verifica se o mouse está sobre o retângulo
            if rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, hover_color, rect)  # Muda a cor do retângulo se o mouse estiver sobre ele
            else:
                pygame.draw.rect(screen, black, rect)  # Mantém a cor preta

            # Renderiza o texto do item
            text = font.render(category, True, white)
            text_rect = text.get_rect(center=rect.center)

            screen.blit(text, text_rect)

            start_y += rect_height + 10  # Aumenta o espaçamento vertical

        pygame.display.flip()

    pygame.quit()
