import pygame


def show_category_selection_screen(categories):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Selecione uma Categoria')

    font = pygame.font.Font(None, 36)

    category_y = 50
    button_height = 40

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))  # Fundo branco

        for category in categories:
            # Crie um retângulo para o botão da categoria
            button_rect = pygame.Rect(50, category_y, 200, button_height)
            pygame.draw.rect(screen, (200, 200, 200), button_rect)  # Desenhe o botão

            # Renderize o texto da categoria no botão
            text = font.render(category['name'], True, (0, 0, 0))
            text_rect = text.get_rect(center=button_rect.center)
            screen.blit(text, text_rect)

            category_y += button_height + 10  # Adicione um espaço entre os botões

        pygame.display.flip()

    pygame.quit()
