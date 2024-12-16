import streamlit as st
import time as t
#title-used to add the title of an app
st.title("Welcome")

#header-
st.header("Hellow world")

#subheader
st.subheader("Getting started")

#To give information

st.info("Used to give information to the user")

# To give warning message
st.warning("Erro 404 not found")

# write

st.write("Used to write text in the page")

#sucess

st.success("Congratulations task is completed")

#error message
st.error("Wrong password")

#Markdown

st.markdown("Python")
st.markdown("# Python")
st.markdown("## Python")
st.markdown(":moon:")

#text

st.text("Learning streamlit")

#to write caption

st.caption("Caption")

#to display math equations

st.latex(r''' ax^2+bx+c''')


#widget
#checkbox
st.checkbox('login')

#button
st.button("click to login")

#radio

st.radio("Correct ture or false",['true', 'false'])

#selectbox

st.selectbox("Pick your course",['C','Python','Data Analysics'])

#multiselect

st.multiselect("Pick your course",['C','Python','Data Analysics'])

#slectslider

st.select_slider("Rating",['good','bad','worst'])

#slider

st.slider("Rate out of 5",0,5)

#number input

st.number_input("Pick a number",0,100)

#text input

st.text_input("Enter email address")

#date input

st.date_input("Enter doj")

#time input

st.time_input("select the time")

#text area

st.text_area("Please explain about your previous project experience")

#file upload

st.file_uploader("Uplaod the CV")

#color

st.color_picker("Slelct color")

#progress
st.progress(50)

#spinner
with st.spinner("Loading"):
    t.sleep(2)


#sidebar

st.sidebar.title("StreamLit")
st.sidebar.text_input("Enter Mail id")
st.sidebar.text_input("Enter password")
st.sidebar.button("submit")
st.sidebar.radio("Type of experience",['Fresher','Experienced'])


#ballon

st.balloons()
