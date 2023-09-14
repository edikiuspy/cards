from flask import Flask, send_from_directory, session, request
from flask_session import Session  # Import Flask-Session
import random
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a secure secret key
app.config['SESSION_TYPE'] = 'filesystem'  # Store session data in the filesystem

# Initialize Flask-Session
Session(app)

colors = ['green', 'yellow', 'red', 'black']
weight = [50, 30, 10, 5]



# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/card")
def card():
        global session
        if 'x' not in session:
            session['x'] = 0
        session['x'] = session.get('x', 0) + 1
        session['color'] = random.choices(colors, weights=weight, k=1)[0]
        if 'history_images' not in session:
            session['history_images'] = []
        con = sqlite3.connect("Game.db")
        cur = con.cursor()
        images = cur.execute(f"SELECT * from Cards where Color='{session['color']}'").fetchall()
        new_image = random.choice(images)

        while new_image in session['history_images']:
            new_image = random.choice(images)
            if all([new_image in session['history_images'] for new_image in images]):
                index = colors.index(session['color'])
                colors.remove(session['color'])
                weight.pop(index)
                session['color'] = random.choices(colors, weights=weight, k=1)[0]
                images = cur.execute(f"SELECT * from Cards where Color='{session['color']}'").fetchall()
                new_image = random.choice(images)
        session['history_images'].append(new_image)
        return new_image[2]


@app.route('/color')
def colorget():
    global session
    return session['color']

@app.route('/count')
def count():
    return str(session['x'])

if __name__ == "__main__":
    app.run(debug=True)
