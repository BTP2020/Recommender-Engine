from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    m1 = IntegerField('Toy Story')
    m2 = IntegerField('Jumanji')
    m3 = IntegerField('Grumpier Old Men')
    m4 = IntegerField('Waiting to Exhale')
    m5 = IntegerField('Father of the Bride Part II')
    m6 = IntegerField('Heat')
    m7 = IntegerField('Sabrina')
    m8 = IntegerField('Tom and Huck')
    m9 = IntegerField('Sudden Death')
    m10 = IntegerField('Golden Eye')
    m11 = IntegerField('American President')
    m12 = IntegerField('Dracula: Dead and Loving It')
    m13 = IntegerField('Balto')
    m14 = IntegerField('Nixon')
    m15 = IntegerField('Cutthroat Island')
    m16 = IntegerField('Casino')
    m17 = IntegerField('Sense and Sensibility')
    m18 = IntegerField('Four Rooms')
    m19 = IntegerField('Ace Venture: When Nature Calls')
    m20 = IntegerField('Money Train')

    submit = SubmitField('Rate')