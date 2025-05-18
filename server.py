from flask import Flask
from random import randrange

app = Flask(__name__)

@app.route('/')
def home():
    number = randrange(9)
    gif_url = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
    return f'<h1> Guess a number between 0 and 9 </h1><img src="{gif_url}">'

@app.route()






if __name__ == "__main__":
    app.run(debug=True)

