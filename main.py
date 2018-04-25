from lib import cilok
#from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
	return "Welcome to Indonesia Electronic KTP Middleware"
	#return render_template('index.html')

	
@app.route("/<gurih>")
def get(gurih):
	return "Hash Cilok %s" % cilok.urlDecode16(gurih)

