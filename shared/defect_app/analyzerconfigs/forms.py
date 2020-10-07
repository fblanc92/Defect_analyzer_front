from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class AnalyzerConfigForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    model_path = StringField('Model Path', validators=[DataRequired()])
    labels_path = StringField('Labels Path', validators=[DataRequired()])
    input_images_path = StringField('Input Images Path', validators=[DataRequired()])
    output_images_path = StringField('Output Images Path', validators=[DataRequired()])
    image_saving = BooleanField('Save Output Images')
    generate_template =  BooleanField('Generate Templates')
    submit = SubmitField('Create')
