import pygame

def show_end_screen():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Fim do Jogo')

    font = pygame.font.Font(None, 36)
    color_text = (255, 255, 255)
    red_color = (255, 0, 0)  # Cor vermelha
    green_color = (0, 255, 0)  # Cor verde

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if 300 <= mouse_pos[0] <= 500 and 300 <= mouse_pos[1] <= 350:
                    from src.view.category_selection_screen import show_category_selection_screen
                    show_category_selection_screen()
                    running = False
                elif 300 <= mouse_pos[0] <= 500 and 400 <= mouse_pos[1] <= 450:
                    pygame.quit()

        screen.fill((0, 0, 0))

        end_text = font.render("Fim das perguntas!", True, color_text)
        text_rect = end_text.get_rect(center=(screen.get_width() // 2, 200))
        screen.blit(end_text, text_rect)

        button_width, button_height = 250, 50
        button_left = (screen.get_width() - button_width) // 2

        pygame.draw.rect(screen, green_color, (button_left, 300, button_width, button_height))  # Altera para a cor verde
        pygame.draw.rect(screen, red_color, (button_left, 400, button_width, button_height))

        return_text = font.render("Outra categoria", True, color_text)
        return_text_rect = return_text.get_rect(center=(screen.get_width() // 2, 325))
        screen.blit(return_text, return_text_rect)

        quit_text = font.render("Encerrar Jogo", True, color_text)
        quit_text_rect = quit_text.get_rect(center=(screen.get_width() // 2, 425))
        screen.blit(quit_text, quit_text_rect)

        pygame.display.flip()

    pygame.quit()
