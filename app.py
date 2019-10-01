from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    playlists = [
    { 'title': 'Cat Videos', 'description': 'Cats acting weird' },
    { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
]
@app.route('/playlists')
def playlists_index():
    """Show all playlists."""
    return render_template('playlists_index.html', playlists=playlists)
    
    """Return homepage."""
    return render_template('home.html', msg='Flask is Cool!')

if __name__ == '__main__':
    app.run(debug=True)