import pygame
import requests

def show_questions_by_category_screen(category_name):
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Exibição de Perguntas')

    font_question = pygame.font.Font(None, 36)
    font_answer = pygame.font.Font(None, 28)
    color_text = (255, 255, 255)
    color_retangulo = (50, 50, 50)
    color_highlight = (100, 100, 100)

    response = requests.get(f'http://127.0.0.1:5000/question/{category_name}')
    if response.status_code == 200:
        question_list = response.json()

        running = True
        current_question_index = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    y_answer = 200  # Posição inicial das respostas

                    # Verifica se a opção clicada é a correta
                    for index in range(len(question_list[current_question_index]['incorrect_answer']) + 1):
                        rect = pygame.Rect(100, y_answer, screen.get_width() - 200, 50)

                        if rect.collidepoint(mouse_pos):
                            if index == len(question_list[current_question_index]['incorrect_answer']):
                                # Última opção (resposta correta)
                                current_question_index += 1  # Avança para a próxima pergunta

                                # Verifica se ainda há perguntas restantes
                                if current_question_index >= len(question_list):
                                    running = False  # Sai do loop ao final das perguntas
                            break
                        y_answer += 70  # Incrementa a posição Y para a próxima resposta

            screen.fill((0, 0, 0))  # Limpa a tela

            # Exibição da pergunta atual
            if current_question_index < len(question_list):
                current_question = question_list[current_question_index]
                question_text = current_question['question_text']
                text_question = font_question.render(question_text, True, color_text)
                screen.blit(text_question, (screen.get_width() // 2 - text_question.get_width() // 2, 50))

            # Exibição das respostas da pergunta atual
            answers = current_question['incorrect_answer'] + [current_question['correct_answer']]
            y_answer = 200  # Posição inicial das respostas

            for index, answer in enumerate(answers):
                rect = pygame.Rect(100, y_answer, screen.get_width() - 200, 50)
                pygame.draw.rect(screen, color_retangulo, rect)

                text_answer = font_answer.render(f"{chr(65 + index)}. {answer}", True, color_text)
                screen.blit(text_answer, (120, y_answer + 10))

                y_answer += 70  # Incrementa a posição Y para a próxima resposta

            pygame.display.flip()

    pygame.quit()
