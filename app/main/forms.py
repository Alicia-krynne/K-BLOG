from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')

class BlogForm(FlaskForm):
    title = StringField('Title of your Blog Post', validators=[Required()])
    category = SelectField('Choose a Category', choices=[('food','food'),('music','music'),('fashion','fashion')],validators=[Required()])
    post = TextAreaField('Write Here', validators=[Required()])
    submit = SubmitField('Post Blog')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')



