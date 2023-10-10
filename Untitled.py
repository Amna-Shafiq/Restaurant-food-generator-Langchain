import streamlit as st
import langchain_helper
st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a Cuisine",("Indian","Italian"))


if cuisine:
  response = langchain_helper.generate_restaurant_name_and_items(cuisine)

  st.header(response['restaurant'])
  menu_items = response['menu-items'].split(',')
  st.write("**Menu Items**")

  for item in menu_items:
    st.write("-",item)


