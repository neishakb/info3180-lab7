from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    description = TextAreaField("Message", validators=[DataRequired()])

    photo = FileField("Photo Upload", validators=[ FileRequired(), FileAllowed(['jpg', 'png', 'IMAGES ONLY!']) ]) 
