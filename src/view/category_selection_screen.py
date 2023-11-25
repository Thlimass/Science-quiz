import pygame
import requests


def show_category_selection_screen():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Exibindo Lista')

    font = pygame.font.Font(None, 24)
    white = (255, 255, 255)
    black = (0, 0, 0)

    response = requests.get('http://127.0.0.1:5000/category')
    print(response.content)
    if response.status_code == 200:
        categories_list = response.content
    categories = [item['category_name'] for item in eval(categories_list.decode())]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)

        # Define o tamanho e espaçamento dos retângulos
        rect_width, rect_height = 200, 30
        vertical_spacing = 10

        # Calcula a posição inicial para centralizar na tela
        total_height = len(categories) * (rect_height + vertical_spacing)
        start_y = (screen.get_height() - total_height) // 2

        for category in categories:
            # Cria um retângulo para cada item
            rect = pygame.Rect((screen.get_width() - rect_width) // 2, start_y, rect_width, rect_height)
            pygame.draw.rect(screen, black, rect)

            # Renderiza o texto do item
            text = font.render(category, True, white)
            text_rect = text.get_rect(center=rect.center)

            screen.blit(text, text_rect)

            start_y += rect_height + vertical_spacing

        pygame.display.flip()

    pygame.quit()
