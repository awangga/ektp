from lib import cilok
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "Welcome to Indonesia Electronic KTP Middleware"

	
@app.route("/<gurih>")
def get(gurih):
	return "Hash Cilok %s" % cilok.urlDecode16(gurih)

