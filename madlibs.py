"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]
madlib_template= ["madlib.html","madlib_1.html"]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)
@app.route('/game')
def show_madlib_form():
    """Greet user with compliment."""

    decision = request.args.get("decision")
    if decision == "yes":
        return render_template("game.html")
    return render_template("goodbye.html")

@app.route('/madlib',methods=['GET','POST'])
def show_madlib():
    # madlib_template= ["madlib.html","madlib_1.html"]
    person = request.form.get("name")
    color = request.form.getlist("color")
    noun = request.form.get("noun")
    adjective = request.form.get("adjective")
    random_template = choice(madlib_template)

    print(person)
    print(color)
    print(noun)
    print(adjective)



    return render_template(random_template,
                            person=person,
                            noun=noun,
                            adjective=adjective,
                            colors=color)

    # compliment = choice(AWESOMENESS)

    
if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
