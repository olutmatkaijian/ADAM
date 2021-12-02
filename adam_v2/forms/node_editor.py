from flask_wtf import FlaskForm
from wtforms import widgets, SelectField, StringField, SubmitField, BooleanField, IntegerField, SelectMultipleField, DateTimeField, FieldList
from wtforms import FileField, FormField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Length, regexp
from wtforms import validators
from config import POSSIBLE_ELEMENTS
# Simple form to add define elements to add to the process editor
# TODO: Add a way to import JSON objects so that multiple elements can be defined at once



class AddNodeForm(FlaskForm):
    dfn_name = StringField('dfn_name', validators=[DataRequired(), Length(1,64)])
    dfn_inputs = IntegerField('dfn_inputs')
    dfn_outputs = IntegerField('dfn_outputs')
    dfn_class = StringField('dfn_class', validators=[DataRequired()])
    # Might have to remove the below html element stuff if I figure out how I did the 
    # adding of html elements
    dfn_html_element = SelectField('dfn_html_element', choices=POSSIBLE_ELEMENTS)
    dfn_html_element_name = StringField('dfn_html_element_name')
    dfn_html_element_data = StringField('dfn_html_element_data')
    dfn_add_html_element = SubmitField('Add another HTML Element')
    dfn_typenode_status = BooleanField('dfn_typenode_status')
    dfn_data = StringField('dfn_data')
    # There is no regexp validator here becaus I found another way (see routes.py)
    dfn_svg_element = FileField("Upload SVG")
    dfn_submit = SubmitField('Submit')

class AddHTMLForm(FlaskForm):
    dfn_html_element = SelectField('dfn_html_element', choices=POSSIBLE_ELEMENTS)
    dfn_html_element_name = StringField('dfn_html_element_name')
    dfn_html_element_data = StringField('dfn_html_element_data')
    
# This is work for the future, so that multiple HTML elements can be added to a form
class FL_AddHTMLForm(FlaskForm):
    FieldList(FormField(AddNodeForm))
