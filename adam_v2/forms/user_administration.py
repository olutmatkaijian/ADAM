from flask_wtf import FlaskForm
from adam_v2.models.users import User
from wtforms import widgets, StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectMultipleField, DateTimeField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Length
from config import GROUPS

# Have to add this because it's not included in Wtforms for some reason
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()
class AddUserForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1,64)])
    groups = MultiCheckboxField('groups', choices=GROUPS)
    expires = DateTimeField('Expiry date in %d-%m-%Y %H:%M (If nothing entered, the user will not expire)', format="%d-%m-%Y %H:%M") #TODO: Add validator
    
    submit = SubmitField('Add User')
    
    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)

    def validate(self):
        initial_validation = super(AddUserForm, self).validate()
        if not initial_validation:
            return False            
        return True
       
