from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# CONFIGURATION
# This creates a local database file named sdn.db
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'sdn.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- DATABASE MODELS ---
class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    alias = db.Column(db.String(100))
    status = db.Column(db.String(50))
    power = db.Column(db.String(200))
    image_filename = db.Column(db.String(100))
    description = db.Column(db.Text)

# --- ROUTES ---

@app.route('/')
def home():
    # Show active heroes on dashboard
    # We use a try/except block in case the DB is empty at first run
    try:
        top_heroes = Hero.query.filter_by(status='Active').limit(4).all()
    except:
        top_heroes = []
    return render_template('index.html', heroes=top_heroes)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name = request.form['name']
        alias = request.form['alias']
        occupation = request.form['occupation']
        power = request.form['power']
        image = request.form['image']
        desc = request.form['desc']

        new_hero = Hero(name=name, alias=alias, occupation=occupation, power=power, image_filename=image, description=desc)
        db.session.add(new_hero)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('admin.html')

# --- INITIAL SETUP ---
if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Creates the sdn.db file automatically
    app.run(debug=True)