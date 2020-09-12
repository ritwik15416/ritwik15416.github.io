from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo
class RegistrationForm(FlaskForm):
    firstname=StringField('firstname',validators=[DataRequired(),Length(min=2,max=20)])
    lastname=StringField('lastname',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired()])
    phone=PhoneField('Phone',validators=[DataRequired(),Length(min=10,max=11)])
    submit=SubmitField('Sign Up!')
