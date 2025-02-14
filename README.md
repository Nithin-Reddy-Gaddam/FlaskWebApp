# FlaskWebApp
This is a Flask-based web application that provides user authentication and an interactive dashboard for exploring the Titanic dataset. Users can register, log in, and analyze passenger data via a dynamic table.


Features:

✅ User Authentication (Registration & Login)
✅ Secure Password Hashing (Flask-Bcrypt)
✅ JWT-based User Sessions (Flask-Login)
✅ Titanic Dataset Analysis
✅ Interactive Dashboard with Data Table
✅ Dockerized Deployment
✅ CI/CD with GitHub Actions
✅ Hosted on AWS

Backend: Flask, Flask-Login, Flask-Bcrypt, SQLAlchemy
Database: SQLite
Frontend: HTML, Jinja2, Bootstrap
Deployment: Docker, GitHub Actions, AWS

PROJECT STRUCTURE
📦 FlaskWebApp  
 ┣ 📂 data/               # Titanic dataset CSV file  
 ┣ 📂 templates/          # HTML templates (Jinja2)  
 ┣ 📂 static/             # CSS, JS, images  
 ┣ 📂 tests/              # Unit tests  
 ┣ 📜 app.py              # Main Flask application  
 ┣ 📜 models.py           # Database models (User, Passenger)  
 ┣ 📜 forms.py            # Flask-WTF forms for login/register  
 ┣ 📜 config.py           # App configuration  
 ┣ 📜 seed_db.py          # Script to populate database  
 ┣ 📜 requirements.txt     # Python dependencies  
 ┣ 📜 Dockerfile          # Docker configuration  
 ┣ 📜 .github/workflows/  # CI/CD GitHub Actions  
 ┗ 📜 README.md           # Project documentation  

 SETUP INSTRUCTIONS:
 Step1: Clone the Repository
 git clone https://github.com/YourUsername/YourRepo.git 
 cd YourRepo

Step2: Create and Activate virtual environment
python3 -m venv venv  
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

Step3: Install Dependencies
pip install -r requirements.txt

Step4: Set up the Database
python seed_db.py

Step5: Run the flask app
flask run

Running with Docker:
build: docker build -t "nameOfImage" .
run: docker run -p 5000:5000 "nameOfImage"

Testing:
pytest tests/

Deployment:
deploying to aws
