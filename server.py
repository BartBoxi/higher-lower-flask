from flask import Flask, render_template_string
import random
app = Flask(__name__)

random_number =  random.randint(0,9)
print(f"The secret number is: {random_number}")

@app.route('/<int:guess>')
def check_guess(guess):
    if guess > random_number:
        gif_url_high = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
        return f'<h2>Too high</h2><img src="{gif_url_high}">'
    elif guess < random_number:
        gif_url_low = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
        return f'<h2>Too low</h2><img src="{gif_url_low}">'
    elif guess == random_number:
        gif_url_correct = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
        return f'<h2>Its correct </h2><img src="{gif_url_correct}">'

# @app.route('/<str:guess1>')
# def check_string(guess1):
#     if guess1 == 'home':
#         return home()


@app.route('/')
def home():
    gif_url = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
    return f'<h1> Guess a number between 0 and 9 </h1><img src="{gif_url}">'



if __name__ == "__main__":
    app.run(debug=True)

