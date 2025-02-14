from flask import Flask, render_template, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from models import db, User, Passenger
from forms import RegistrationForm, LoginForm
from config import Config
import pandas as pd

# Initialize extensions (without app binding)
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'login'


def create_app():
    """Factory function to create a Flask app instance."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions with app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    @login_manager.unauthorized_handler
    def unauthorized():
        flash("Please log in to access this page", "warning")
        return redirect(url_for('login'))

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, int(user_id))

    # ─── Routes ───

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully! You can now log in.', 'success')
            return redirect(url_for('login'))
        return render_template('register.html', form=form)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('login_success'))
            else:
                flash('Login failed. Check email and password.', 'danger')
        return render_template('login.html', form=form)

    @app.route('/dashboard')
    @login_required
    def dashboard():
        # Query the Titanic dataset from the database
        passengers = Passenger.query.all()
        you = current_user.username

        # If you want to show more data about passengers, we can use pandas to get a summary
        df = pd.read_csv("data/titanic.csv")  # Or use a query to fetch the dataset from DB directly

        # Optional: You can perform some summary analysis and pass it to the template for display
        total_passengers = len(df)
        survived_count = df[df['Survived'] == 1].shape[0]
        non_survived_count = total_passengers - survived_count
        avg_fare = df['Fare'].mean()

        return render_template(
            "dashboard.html",
            total=total_passengers,
            survived=survived_count,
            non_survived=non_survived_count,
            avg_fare=avg_fare,
            passengers=passengers,  # Pass the data to the template,
            you=you
        )

    @app.route('/logout')
    def logout():
        logout_user()
        flash('You have been logged out.', 'info')
        return redirect(url_for('home'))

    @app.route('/login_success')
    def login_success():
        you = current_user.username
        return render_template('login_success.html', username=you)

    return app


# ─── Run the Flask App ───
if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Ensure database tables are created
    app.run(debug=True)
