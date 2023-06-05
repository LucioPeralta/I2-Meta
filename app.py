from flask import Flask, render_template, url_for, request,redirect
from src.routes import app_routes


app = Flask(__name__, static_folder='src/static', template_folder='src/templates')
app.register_blueprint(app_routes)

if __name__ == '__main__':
    app.run(debug=True)