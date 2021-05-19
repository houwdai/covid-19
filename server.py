from app import app
app.config['SECRET_KEY'] = 'any secret string'
app.run(port=8080)