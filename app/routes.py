from flask import render_template, flash, redirect, request
from app import app
from app.forms import RateForm, sampled_name
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kriti'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/rate', methods=['GET', 'POST'])
def rate():
    form = RateForm()
    if request.method == "POST":

        req = request.form
        print(req)

        m1rate = request.form.get("m1")
        m2rate = request.form.get("m2")
        m3rate = request.form.get("m3")
        m4rate = request.form.get("m4")
        m5rate = request.form.get("m5")
        m6rate = request.form.get("m6")
        m7rate = request.form.get("m7")
        m8rate = request.form.get("m8")
        m9rate = request.form.get("m9")
        m10rate = request.form.get("m10")
        m11rate = request.form.get("m11")
        m12rate = request.form.get("m12")
        m13rate = request.form.get("m13")
        m14rate = request.form.get("m14")
        m15rate = request.form.get("m15")
        m16rate = request.form.get("m16")
        m17rate = request.form.get("m17")
        m18rate = request.form.get("m18")
        m19rate = request.form.get("m19")
        m20rate = request.form.get("m20")

        numbers = [m1rate, m2rate, m3rate, m4rate, m5rate, m6rate, m7rate, m8rate, m9rate, m10rate, m11rate, m12rate, m13rate, m14rate, m15rate, m16rate, m17rate, m18rate, m19rate, m20rate]
        list5 = []
        list4 = []
        list3 = []
        list2 = []
        list1 = []
        length = len(numbers)
        for i in range(length):
            if(numbers[i]=='5'):
                list5.append(i)
            elif(numbers[i]=='4'):
                list4.append(i)
            elif(numbers[i]=='3'):
                list3.append(i)
            elif(numbers[i]=='2'):
                list2.append(i)
            elif(numbers[i]=='1'):
                list1.append(i)

        final_list = []
        length5 = len(list5)
        if(length5 > 0):
            for i in range(length5):
                final_list.append(list5[i])
        
        lengthfinal = len(final_list)
        if(lengthfinal<5):
            length4 = len(list4)
            for i in range(length4):
                final_list.append(list4[i])
        lengthfinal = len(final_list)
        if(lengthfinal<5):
            length3 = len(list3)
            for i in range(length3):
                final_list.append(list3[i])
        lengthfinal = len(final_list)
        if(lengthfinal<5):
            length2 = len(list2)
            for i in range(length2):
                final_list.append(list2[i])
        lengthfinal = len(final_list)
        if(lengthfinal<5):
            length1 = len(list1)
            for i in range(length1):
                final_list.append(list1[i])

        lengthfinal = len(final_list)

        if(lengthfinal > 5):
            final_list = final_list[:5]


        # ratings = pd.read_csv('/home/kriti/RecommenderEngine/app/data/ratings.csv', sep='\t', encoding='latin-1', usecols=['user_id', 'movie_id', 'rating'])
        # users = pd.read_csv('users.csv', sep='\t', encoding='latin-1', usecols=['user_id', 'gender', 'zipcode', 'age_desc', 'occ_desc'])
        movies = pd.read_csv('/home/kriti/RecommenderEngine/app/data/movies.csv', sep='\t', encoding='latin-1', usecols=['movie_id', 'title', 'genres'])

        movies['genres'] = movies['genres'].str.split('|')
        movies['genres'] = movies['genres'].fillna("").astype('str')
        tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
        tfidf_matrix = tf.fit_transform(movies['genres'])
        print(tfidf_matrix.shape)

        cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
        print(cosine_sim[:4, :4])

        titles = movies['title']
        indices = pd.Series(movies.index, index=movies['title'])

        print(genre_recommendations(sampled_name[final_list[0]], indices, cosine_sim, titles).head(20))

        return redirect(request.url)

    return render_template('rate.html', title='Rate', form=form)

def genre_recommendations(title, indices, cosine_sim, titles):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:21]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]