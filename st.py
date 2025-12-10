##streamlit 
# pip install streamlit
##python lib 
##webpages for ml and data sci projects
#html and css no requirement
import streamlit as st  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt 
import time as time

##page configuration 
st.set_page_config(
    page_title="streamlit function demo",
    page_icon= "😎",
    layout="centered"
)
##title and text elemnts 
st.title("hello world")
st.header("1. Text elements")
st.subheader("markdown,code,latex")
st.markdown("**bold text**,*italic text*,`code`text")
st.code("print('hello everyone')",language="python")
st.latex(r"a^2+b^2=c^2")

st.divider()

##metrices and messages 
st.header("2. metrices and messages")
st.metric(label="Revenue",value=1234,delta="+10%",delta_color="inverse")  #normal delta color for green and inverse for red
st.error("this is an error message")
st.warning("this is a warning message")
st.info("this is an info message")      ## automatic color chosenp
st.success("this is a success message")
st.exception(ValueError("this is an exception message"))

st.divider()

##data display 
st.header("3. data display")
df=pd.DataFrame(np.random.randn(10,2),columns=["a","b"])
st.dataframe(df)
st.table(df.head(3))
st.json(df.to_dict())
st.divider()

#charts 
st.header("4.Charts")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
chart = alt.Chart(df.reset_index()).mark_line().encode(x="index",y="a")
st.altair_chart(chart,use_container_width=True)
fig , ax = plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)
st.divider()


#widgets
st.header("5. Widgets")
with st.form("Input Form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age")
    mood = st.radio("Select your mood",("Happy","Sad","Neutral"))
    languages = st.multiselect("Select your languages",("English","French","Hindi"))
    submit = st.form_submit_button("Submit")
    if submit:
        st.success(f"Name : {name}, Age : {int(age)}, Mood : {mood}, Languages : {languages}")
        

#col1, col2, col3 = st.columns(3)
#with col1:
#    st.text_input("Enter your name")
#    st.number_input("Enter your age")
#with col2:
#    st.radio("Select your mood",("Happy","Sad","Neutral"))
#    st.multiselect("Select your languages",("English","French","Hindi"))
#with col3:
#    st.title("Output")
    
col1, col2, col3 = st.columns([4,1,1])
with col1:
    st.text_input("Enter your name")
    st.number_input("Enter your age")
with col2:
    st.radio("Select your mood",("Happy","Sad","Neutral"))
    st.multiselect("Select your languages",("English","French","Hindi"))
with col3:
    st.title("Output")


col1, col2 = st.columns(2)
with col1:
    number = st.slider("Select a number",0,100)
with col2:
    #colour = st.color_picker("Select a color")
    colour = st.color_picker("Select a color", "#961313")
    
st.text_area("Enter your message")
st.date_input("Select a date")
st.time_input("Select a time")
st.file_uploader("Upload a file")

st.divider()

#media
st.header("6. Media")
st.image("https://www.verdissimo.com/wp-content/uploads/2023/08/Verdissimo_flores_bonitas_CONT_07.jpg")
st.video("https://www.youtube.com/watch?v=ryUxrFUk6MY")
st.audio("https://soundcloud.com/spamusicrelaxationmeditation/sets/nature-meditation-101-relaxing")
    
    
st.sidebar.header("SIDEBAR HEADER")
st.sidebar.write("THIS IS A SIDEBAR TEXT")
st.sidebar.button("CLICK ME")
option = st.sidebar.selectbox("SELECT AN OPTION",("OPTION 1","OPTION 2","OPTION 3"))


#tab1,tab2,tab3 = st.tabs(["tab1","tab2","tab3"])

      
with st.container():
    st.write("THIS IS A CONTAINER")     
    
    
with st.expander("EXPANDER HEADER"):
    st.write("THIS IS AN EXPANDER")     
    
    
with st.spinner("loading data..."):
    time.sleep(10)
st.success("Data loaded")
st.toast("Toast message", icon="👌")


st.page_link("http://streamlit.io", label = "streamlit webpage", icon="✌")