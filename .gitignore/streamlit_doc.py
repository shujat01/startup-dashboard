import streamlit as st
import pandas as pd
import time


st.title('Startup Dashboard')
st.header('i am learning streamlit')
st.subheader('and i am loving it')
st.write('thisb is a normal text')
 

# markdownguide.org  -->study from here
#number po '#' represents th level of heading
st.markdown("""
### my favourite movies
- race 3
- humshaka
- race4
""")

st.code("""
def foo(input):
        return foo**2
x=foo(2)
""")


# study latex from overleaf.com learn latex in 30 minutes
st.latex('x^2 +y^2 +2=0')


#DISPLAY ELEMENTS

#datafram
df=pd.DataFrame({
   'name':['nitish','ankit','anupam'],
   'marks':[54,56,70],
   'package':[10,12,14]
})

st.dataframe(df)

#metrics
st.metric('Revenue','RS=3L','-3%')

#json
st.json({
   'name':['nitish','ankit','anupam'],
   'marks':[54,56,70],
   'package':[10,12,14]
})

st.image('abc.JPEG')

#st.video('xyz.mp4')

st.sidebar.title('sidebar ka title')

col1,col2,col3=st.columns(3)

with col1:
    st.image('abc.JPEG')
with col2:
    st.image('abc.JPEG')
with col3:
    st.image('abc.JPEG')


st.error('failed!')
st.success('passed')
st.info('keep going')
st.warning('carefull!')

#progress bar

bar=st.progress(0)

for i in range(1,100):
    bar.progress(i)


#TAKING USERE INPUT
email=st.text_input('enter email')
number=st.number_input('enter age')
date=st.date_input('enter date')



#2
email=st.text_input('enter email')
password=st.text_input('enter password')

gender=st.selectbox('Gender',['male','female','mental'])

btn=st.button('login')

if btn:  #means if the button is clicked
    if email=='nitsh@gmail.com' and password=='1234':
        st.success('login succesful')
        st.balloons()
        st.write(gender)
    else:
        st.error('login failed')


file=st.file_uploader('upload a csv file')

#3
if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())


    #read treamlit documentation for more
