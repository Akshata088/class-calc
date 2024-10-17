from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/project'  # Replace with your database URI
app.config['SECRET_KEY'] = '1234'  # Replace with a strong secret key
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):  # Corrected method name
        return f'<User {self.username}>'

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/templates/signup')
def signup():
    return render_template('signup.html')

@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        flash('Login successful!', 'success')
        return redirect('/success')
    else:
        flash('Invalid username or password', 'danger')
        return redirect(url_for('index'))  # Redirect to the index

@app.route('/signup', methods=['POST'])
def handle_signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if password != confirm_password:
        flash('Passwords do not match', 'danger')
        return redirect(url_for('signup'))  # Redirect to signup

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        flash('Username already exists', 'danger')
        return redirect(url_for('signup'))

    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        flash('Email already exists', 'danger')
        return redirect(url_for('signup'))

    new_user = User(username=username, email=email, password_hash=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    flash('Signup successful!', 'success')
    return redirect(url_for('index'))  # Redirect to index

@app.route('/success')
def success():
    return 'Login successful!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
