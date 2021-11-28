from flask_wtf import FlaskForm
from adam_v2.models.users import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1,64)])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    def validate(self):
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        print(user)
        if not user:
            self.username.errors.append('Unknown User')
            return False
        if not user.verify_password(self.password.data):
            self.password.errors.append('Invalid Password')
            return False
        return True
