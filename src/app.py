from src import create_app

app = create_app()


# Applications Routes
from .controllers import category_controller
from .controllers import question_controller
from .controllers import play_game_controller
from .controllers import home_controller

if __name__ == "__main__":
    app.run()
