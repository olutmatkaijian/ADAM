from flask_wtf import FlaskForm
from flask import flash
from adam_v2.models.users import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, Regexp

class change_password_form(FlaskForm):
    newpassword = PasswordField('New Password', validators=[DataRequired(), 
    Length(min=8, max=128, 
    message="Password must be between 8 and 128 characters"),
    Regexp("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
    message="Must contain at least eight characters, one uppercase letter, one lowercase letter, one number and one special character")])
    repeatpassword = PasswordField('Repeat Password', validators=[DataRequired()])
    submit = SubmitField('Change Password')
    
    def __init__(self, *args, **kwargs):
        super(change_password_form, self).__init__(*args, **kwargs)

    def validate(self):
        initial_validation = super(change_password_form, self).validate()
        if not initial_validation:
            return False
        if self.newpassword.data == self.repeatpassword.data and initial_validation:
            print("passwords match")
            return True
