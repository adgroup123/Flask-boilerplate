from flask import render_template,request
from app import app

@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'POST':
		status = 'post'
	if request.method == 'GET':
		status = 'GET'
	return render_template('template.html',status=status)