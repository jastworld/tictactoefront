from flask import Flask
app = Flask(__name__)
app.debug = True

from FlaskApp import routes

if __name__ == "__main__":
    app.run()
