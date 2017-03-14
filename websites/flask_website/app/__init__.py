from flask import Flask
app = Flask(__name__)
from app import routes

# If we are running with docker, we need the line below.
#app.run(debug=True,host='0.0.0.0')
