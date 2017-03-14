'''
Routes deals with URL routing.

1. A user issues a request for a domain's URL
2. routes.py maps the URL to a python function
3. The python function finds the relevant web template inside the templates folder.
4. The web template looks in the static folder for any images, css or js it needs.  
5. Rendered html is sent back to routes.py
6. routes.py sends the html back to the browser.
'''
import os, random
from flask import request, render_template, url_for, jsonify, redirect, session, Response
from app import forms
from app import app

app.secret_key = 'development key'

@app.route('/')
@app.route('/index')
def index():
	# Display a list of hyperlinks to the other pages
	links = [
		{"name": "Feedback Form", "url": "feedback"},
		{"name": "Display Static Image", "url": "picture"},
		{"name": "Automatically update number using Ajax", "url": "ajax"}
	]
	return render_template('index.html', title="index", links=links)


@app.route('/help')
def help():
	return render_template('help.html')
	
@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/picture')
def picture():
	return render_template('picture.html')
	
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
	form=forms.FeedbackForm()
	if request.method == 'POST':
		# Check that the user has filled out all the required fields. If not, tell them which one is missing.
		if form.validate() == False:
			return render_template('feedback.html', response=list(form.errors.values())[0][0], form=form)
		else:
			# Deal with the returned data
			# ***Code here***
			print(form.name.data)
			# Send a response (classification) to the user
			# ***Code here***
			return render_template('feedback.html', response='Thank you for your feedback', form=form)
	else:
		# Ask the user for feedback
		return render_template('feedback.html', response ='', form=form)
		
# Route that will process the AJAX request, and return a random number as a proper JSON response (Content-Type, etc.)
@app.route('/_get_random')
def get_random():
    #a = request.args.get('a', 0, type=int)
    #b = request.args.get('b', 0, type=int)
    return jsonify(result=random.random())
	
@app.route('/ajax')
def ajax():
	return render_template('ajax.html')