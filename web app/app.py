import requests
import streamlit as st
import pickle


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=ec399ee20c4efa250c1a866c5f41c945&language=en-US'.format(movie_id))

    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True,
                        key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list:

        movie_id = new_df.iloc[i[0]].movie_id
        recommended_movies.append(new_df.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


new_df = pickle.load(open("movies.pkl", "rb"))
movie_list = new_df['title'].values

similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("Movie Recommendation System")

selected = st.selectbox("Select a movie to see recommendations...", movie_list)


if st.button("Recommend"):
    names, posters = recommend(selected)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
