import pygame
import requests

from src.view.the_end_screen import show_end_screen


def show_questions_by_category_screen(category_name):
    pygame.init()

    error_sound = pygame.mixer.Sound('smw_lemmy_wendy_incorrect.wav')
    correct_sound = pygame.mixer.Sound('smw_coin.wav')

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
                    answer_correct = False

                    # Verifica se a opção clicada é a correta
                    for index, answer in enumerate(question_list[current_question_index]['answer_option']):
                        rect = pygame.Rect(100, y_answer, screen.get_width() - 200, 50)

                        if rect.collidepoint(mouse_pos):
                            if answer == question_list[current_question_index]['correct_answer']:
                                # Resposta correta
                                answer_correct = True
                                current_question_index += 1  # Avança para a próxima pergunta

                                # Verifica se todas as perguntas foram respondidas
                                if current_question_index >= len(question_list):
                                    running = False  # Sai do loop ao final das perguntas
                            break
                        y_answer += 70

                    # Reproduz o som com base na resposta
                    if answer_correct:
                        correct_sound.play()
                    else:
                        error_sound.play()

            screen.fill((0, 0, 0))  # Limpa a tela

            if current_question_index < len(question_list):
                current_question = question_list[current_question_index]
                question_text = current_question['question_text']

                # Renderização da pergunta atual...
                max_width = screen.get_width() - 100  # Largura máxima da área de exibição

                words = question_text.split()
                lines = []
                current_line = ''

                for word in words:
                    test_line = current_line + word + ' '
                    test_width, _ = font_question.size(test_line)

                    if test_width < max_width:
                        current_line = test_line
                    else:
                        lines.append(current_line)
                        current_line = word + ' '

                lines.append(current_line)

                y_position = 50
                for line in lines:
                    text_line = font_question.render(line, True, color_text)
                    screen.blit(text_line, (screen.get_width() // 2 - text_line.get_width() // 2, y_position))
                    y_position += font_question.get_height()  # Ajusta a posição vertical para a próxima linha

                # Exibição das respostas da pergunta atual
                answers = current_question['answer_option']  # Obtém as opções de resposta
                y_answer = 200  # Posição inicial das respostas

                for index, answer in enumerate(answers):
                    rect = pygame.Rect(100, y_answer, screen.get_width() - 200, 50)
                    pygame.draw.rect(screen, color_retangulo, rect)

                    text_answer = font_answer.render(f"{chr(65 + index)}. {answer}", True, color_text)
                    screen.blit(text_answer, (120, y_answer + 10))

                    y_answer += 70  # Incrementa a posição Y para a próxima resposta

            else:
                # Se todas as perguntas foram respondidas, exibe a tela de fim de jogo
                show_end_screen()
                running = False

            pygame.display.flip()

        pygame.quit()
