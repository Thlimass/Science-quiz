import threading

from flask import request, render_template

from ..app import app
from ..services.category_services import list_all
from ..services.question_services import get_questions_for_category
from ..view.game_screen import run_game_screen


@app.route('/play_game', methods=['GET'])
def play_game():
    categories = list_all()
    selected_category = run_game_screen(categories)  # Inicia a lógica do jogo do Pygame

    if selected_category:
        questions = get_questions_for_category(selected_category)
        # ... (código para exibir as perguntas usando Pygame ou renderizar um template com Flask)
        return f"Categoria selecionada: {selected_category}"  # Substitua por render_template se preferir usar templates HTML

    return "Nenhuma categoria selecionada"
