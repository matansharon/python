from flask import Flask
import random

app = Flask(__name__)
number_to_guess = random.choice([0, 1, 2, 3, 4, 5   , 6, 7, 8, 9, 10])
welcome_html = '<h1 style="color:black">Welcome to guess the number game</h1>' \
               "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=200/>"
lower_html = '<h1 style="color:blue">Too low! guess again</h1>' \
             "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=200/>"
higher_html = '<h1 style="color:red">Too high! guess again</h1>' \
              "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=200/>"
correct_html = '<h1 style="color:red">Correct!!!</h1>' \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=200/>"


@app.route("/")
def welcome_to_the_game():
    if app.debug:
        print(number_to_guess)
    return welcome_html


@app.route("/<int:number>")
def guess(number):
    if number < number_to_guess:
        return lower_html
    elif number > number_to_guess:
        return higher_html
    else:
        return correct_html


if __name__ == "__main__":
    app.run(debug=True)
