import streamlit as st
import langchain_helper

st.title("Restaurant name generator")

cuisine = st.sidebar.selectbox("pick a cuisine",  
                               ("indian" , "american", "mexcan" , "italian"))


if cuisine :
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response["restaurant_name"].strip())
    menu_items = response['menu_list'].strip().split(",")
    st.write("** Menu_Items **")
    for item in menu_items:
        st.write("-", item)

