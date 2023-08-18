import streamlit as st
from PIL import Image

st.title("This is My BMI Calculator")
st.write("-------------------------------------------------")

pic = Image.open("hdlcimage.jpg")
st.image(pic)


st.sidebar.text_input("Name :"," ")
st.sidebar.radio(label = "Gender : ",options=('Female','Male'))

st.sidebar.number_input("Age :",value = False)

st.sidebar.text_area("Address :")

st.sidebar.write("Hobbies :")
st.sidebar.checkbox("Reading Books")
st.sidebar.checkbox("Dancing")
st.sidebar.checkbox("Listening Songs")
st.sidebar.checkbox("Travelling")
st.sidebar.checkbox("Playing Games")
st.sidebar.checkbox("Singing Songs")

weight = st.number_input("Enter Weight(Kg) :",step = 1,value = False)

height = st.number_input("Enter Height(Cm) :",step = 1,value = True)

BMI = weight/(height)**2

BMI = BMI * 10000

st.success(f"Your BMI Value is {BMI} kg/m^2")

if BMI >= 18.5 and BMI <= 24.9:
    st.success(f"You are Healthy :muscle: Kindly,Maintain the Same")
else:
    st.warning(f"OH Shut! You are UnHealthy :cry: Kindly, Maintain Good Diet and Fitness")
    
    
#Footer 
    
    with st.container():
        st.write("--------")
        left_column,right_column = st.columns(2);
        
        with left_column:
            st.header("For More Details-")
            st.write("[LinkedIn](https://www.linkedin.com/in/ramya-deepthi-konduri-a4676721a)")
            st.write("[GitHub](https://github.com/RamyaDeepthiKonduri)")
            
            
           
            
            with right_column:
                st.header("Contact Me -")
                st.text_input("Mobile: "," ")
                st.text_input("E-Mail: "," ")
                
        
st.write('--------')
st.write('----- :copyright: 2K23,Ramya Deepthi-----')