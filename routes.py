from flask import render_template, request, Flask
app = Flask(__name__)

@app.route('/')
def render_main():
	return render_template('index.html')