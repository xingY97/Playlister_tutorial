from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     """Return homepage."""
#     return render_template('home.html', msg='Flask is Cool!')

    #Our mock array of project
playlists = [
    { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
]

@app.route('/')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)
    


if __name__ == '__main__':
    app.run(debug=True)