import streamlit as st
import sidebar
import textPage
# import audioPage
import imdbReviewsPage
import imagePage
# import videoPage
# import twitterAnalysisPage

# st.title("Hello")
page = sidebar.show()

if page=="Text":
    textPage.renderPage()
elif page=="IMDb movie reviews":
    imdbReviewsPage.renderPage()
elif page=="Image":
    imagePage.renderPage()