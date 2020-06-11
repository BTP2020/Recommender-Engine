from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired
import csv
import random
import pandas as pd

colnames = ['movie_id', 'title', 'genres']
data = pd.read_csv('/home/kriti/RecommenderEngine/app/data/movies.csv', names=colnames)

names = data.movie_id.tolist()
sampled_name = random.sample(names, 20)

class LoginForm(FlaskForm):
    m1 = IntegerField(sampled_name[0])
    m2 = IntegerField(sampled_name[1])
    m3 = IntegerField(sampled_name[2])
    m4 = IntegerField(sampled_name[3])
    m5 = IntegerField(sampled_name[4])
    m6 = IntegerField(sampled_name[5])
    m7 = IntegerField(sampled_name[6])
    m8 = IntegerField(sampled_name[7])
    m9 = IntegerField(sampled_name[8])
    m10 = IntegerField(sampled_name[9])
    m11 = IntegerField(sampled_name[10])
    m12 = IntegerField(sampled_name[11])
    m13 = IntegerField(sampled_name[12])
    m14 = IntegerField(sampled_name[13])
    m15 = IntegerField(sampled_name[14])
    m16 = IntegerField(sampled_name[15])
    m17 = IntegerField(sampled_name[16])
    m18 = IntegerField(sampled_name[17])
    m19 = IntegerField(sampled_name[18])
    m20 = IntegerField(sampled_name[19])

    submit = SubmitField('Rate')