from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, TextField, SubmitField, FileField, RadioField, BooleanField, DecimalField,FieldList,FormField
from wtforms import validators, ValidationError

class FeedbackForm(FlaskForm):
	name = TextField("Name", [validators.Required("Please enter your name")])
	email = TextField("Email",[validators.Required("Please enter your email")])
	subject = TextField("Subject")
	message = TextAreaField("Message", [validators.Required("Please enter a message")])
	submit = SubmitField("Send")
	

class ClassifierForm(FlaskForm):
	text = TextAreaField("Text", [validators.Required("Please enter some text"), validators.Length(min=100, message='Please enter more than 100 characters'), validators.Length(max=100000, message='Too much text! Please enter less than 100,000 characters.')])
	submit = SubmitField("Classify")


class FileUploadForm(FlaskForm):
	file = FileField("File", [validators.Required("Please choose a file")])
	submit = SubmitField("Upload")
	

class ReturnCSV(FlaskForm):
	submit = SubmitField("Download")