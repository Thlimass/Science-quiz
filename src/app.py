
from src import create_app

app = create_app()


# Hello World!
@app.route('/')
def hello():
    return "Hello World!!"


# Applications Routes
from .controllers import category_controller

if __name__ == "__main__":
    app.run()
