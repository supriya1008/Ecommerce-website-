from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired,ValidationError
from market.models import User
class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username.')

    # Custom validation for email
    def validate_email_address(self, email_to_check):
        user = User.query.filter_by(email=email_to_check.data).first()
        if user:
            raise ValidationError('Email already exists! Please try a different email.')
        
    username = StringField(label='User Name:',validators=[Length(min=2,max=30),DataRequired()] )
    email = StringField(label='Email Address:',validators=[Email(),DataRequired()])
    password = PasswordField(label='Password:',validators=[Length(min=6),DataRequired()])
    confirm_password = PasswordField(label='Confirm Password:',validators=[EqualTo('password'),DataRequired()])
    submit = SubmitField(label='submit')

class LoginForm(FlaskForm):
    username=StringField(label='User Name',validators=[DataRequired()])
    password=PasswordField(label='Password',validators=[DataRequired()])
    submit=SubmitField(label='sign in')


class PurchaseItemForm(FlaskForm):
    submit=SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit=SubmitField(label='Sell Item!')