from src import create_app
from src.view.main_screen import show_main_screen

app = create_app()


# Applications Routes
from .controllers import category_controller
from .controllers import question_controller

if __name__ == "__main__":
    app.run()
    show_main_screen()
