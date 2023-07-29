import streamlit as st 
import pickle
import pandas as pd
import requests

def fetch(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recom(movie):
    index = mov[mov['title'] == movie].index[0]
    dis = sim[index]
    movie_list = sorted(list(enumerate(dis)),reverse=True,key=lambda x:x[1])[1:6]
    recom_movies =[]
    recom_movies_image =[]
    for i in movie_list:
        movie_id=mov.iloc[i[0]].movie_id
        recom_movies.append(mov.iloc[i[0]].title)
        recom_movies_image.append(fetch(movie_id)) #fetch image from Api
    return recom_movies,recom_movies_image

mo = pickle.load(open('mo.pkl','rb'))
mov = pd.DataFrame(mo)

sim = pickle.load(open('sim.pkl','rb'))
st.title('Movie Recommender System')

select1 = st.selectbox('Enter', mov['title'].values)

if st.button('Recommend'):
    recommendations,image = recom(select1)
    
    A1, A2, A3, A4, A5 = st.columns(5)
    with A1:
        st.text(recommendations[0])
        st.image(image[0])
    with A2:
        st.text(recommendations[1])
        st.image(image[1])
    with A3:
        st.text(recommendations[2])
        st.image(image[2])
    with A4:
        st.text(recommendations[3])
        st.image(image[3])
    with A5:
        st.text(recommendations[4])
        st.image(image[4])