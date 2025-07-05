from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="my webpage", page_icon="🤫🤔", layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


lottie_coding=load_lottieurl("https://lottie.host/309564d8-f160-4a41-a7a6-60a169319469/AHJek3Ivzq.json")
lottie_gigachad=load_lottieurl("https://lottie.host/fcb43a9e-1a76-48cb-bc07-ea998211954f/6XcL6AA695.json")
img_contact_form=Image.open("images/Screenshot 2025-07-05 121516.png")
img_giga_form=Image.open("images/Screenshot 2025-07-05 125614.png")
img_last_form=Image.open("images/9f26373bace02400237f1b93a465cf9f.jpg")

with st.container():
 st.markdown("<h1 style='text-align: center;'>How to Be a GigaChad Like Me 🤫</h1>", unsafe_allow_html=True)
 


#Hello i am muhammet,i would like to reshape the world where wherever i look i see gigachads left and right looking at me the ultimate giga chad🤫🤫🤫
st.markdown("<p style='font-size: 24px;'>Hello i am muhammet,i would like to reshape the world where wherever i look i see gigachads left and right looking at me the ultimate giga chad🤫🤫🤫</p>", unsafe_allow_html=True)




with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)  
    with left_column:
        st.header("what i do to become a gigachad")
        st.write("##")
        st.markdown("<p style='font-size: 24px;'>I wake up every day at 5 AM, listen to Giga Chad music for 10 hours,go to the gym for another 10 hours, and then spend 10 hours posing.I only sleep for 10 minutes, and then repeat the cycle.  </p>", unsafe_allow_html=True)




with right_column:
    st_lottie(lottie_coding,height=400,key="gigachad")
#---- Projects---
with st.container():
    st.write("---")
    st.header("How I Became the GigaChad")
    st.markdown("##")

    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)

    with text_column:
        st.subheader("GigaChad Cats - World")
        st.markdown("""
This is only the beginning of your journey into giga chad greatness.  
Watching this video **90 times a day** is how you start your transformation.

👉 [Watch Video...](https://youtu.be/tHGhnmc964Q?si=7fUBV4X9lOYC58l3)
""")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_giga_form)
    with text_column:
        st.subheader("GigaChad Cat & GigaChad Kitten Sing Together (10 Hours Extended)")
        st.write("When you think you are ready to become a gigachad i would recommend watching this daily")
        st.markdown("👉 [Watch Video...](https://youtu.be/cKtlwrkRSXA?si=y0PhPsZ0UaDZpfPE)")
#final transformation
with st.container():
    st.write("---")
    st.markdown("##")
    st.markdown("<p style='font-size: 60px;'>THIS MUST BE HOW YOU LOOK AFTER YOU FINISH MY PROGRAM</p>", unsafe_allow_html=True)
    st.image(img_last_form,use_container_width=True)


#contacts
with st.container():
    st.write("---")
    st.header("If you face any problems in my gigachad program dont be shy to send an email for assistance")
    st.write("##")
    contact_form="""
<form action="https://formsubmit.co/muhammet.anuti@bilgiedu.net" method="POST">
   <input type="hidden" name="_captcha" value="false">
   <input type="text" name="name" placeholder="your name" required>
   <input type="email" name="your email" placeholder="your email" required>
   <textarea name="message" placeholder="your message here" required></textarea>
   <button type="submit">Send</button>
</form>
"""
left_column,right_column=st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()