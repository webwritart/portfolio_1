import os
from flask import Flask
from routes.main import main
from routes.about import about


app = Flask(__name__)
app.secret_key = 'dgirgr8489yg90rjg0HG(U#UU(Ggrggj90rge5'


# ------------------------------------- BLUEPRINTS ---------------------------------- #

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(about, url_prefix='/about')


if __name__ == '__main__':
    app.run(debug=True)
