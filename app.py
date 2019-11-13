from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    """Renders the home page with link to Fortune page."""
    return render_template('index.html')


@app.route('/fortune')
def fortune_form():
    """Renders the fortune form page."""
    return render_template('fortune_form.html')

@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
    users_favorite_animal = request.args.get('animal')

    if users_favorite_animal == 'cat':
        # fortune is "You'll have a magical day!"
        fortune = "meow"
    elif users_favorite_animal == 'dog':
        # fortune is ...
        fortune = "woof"
    elif users_favorite_animal == 'rex':
        # fortune is ...
        fortune = "you have to use your head"
    elif users_favorite_animal == 'chicken':
        fortune = 'kfc > popeyes'
        # no other fortune applies, return default fortune
    else:
        # no other fortune applies, return default fortune
        fortune = "Just keep breathing, you will get their eventually"

    return render_template ('fortune_results.html', fortune=fortune)
