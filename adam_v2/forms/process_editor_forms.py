from flask_wtf import FlaskForm
from wtforms import SelectField


# A simple select field to select which theme elements are shown in the process editor
class SelectThemeForm(FlaskForm):
    theme = SelectField('theme', choices=[])

    def __init__(self, *args, **kwargs):
        super(SelectThemeForm, self).__init__(*args, **kwargs)
