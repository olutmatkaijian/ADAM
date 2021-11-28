from flask_wtf import FlaskForm


from wtforms import SubmitField

class RefreshDataForm(FlaskForm):
    refreshfield = SubmitField('refresh')

