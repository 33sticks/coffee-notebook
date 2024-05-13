import streamlit as st
from db_utils import fetch_unique_values, fetch_beans, fetch_brewing_methods, fetch_tasting_notes
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.set_page_config(layout="wide")
    st.title("Coffee Discovery Journey")

    # Step 1: Path Selection
    st.header("Choose Your Path")
    path = st.selectbox("Select a path to start your journey", ["Manufacturer", "Brewing Method", "Country of Origin"])

    if path == "Manufacturer":
        manufacturers = fetch_unique_values("manufacturer", "beans")
        selected_manufacturer = st.selectbox("Select Manufacturer", manufacturers)
        if selected_manufacturer:
            beans = fetch_beans('manufacturer', selected_manufacturer)
            st.subheader("Beans from Manufacturer: " + selected_manufacturer)
            bean_names = [bean['name'] for bean in beans]
            selected_bean_name = st.selectbox("Select Bean", bean_names)
            if selected_bean_name:
                selected_bean = next(bean for bean in beans if bean['name'] == selected_bean_name)
                st.subheader("Details for Bean: " + selected_bean_name)
                bean_details = {
                    "ID": selected_bean['id'],
                    "Name": selected_bean['name'],
                    "Origin": selected_bean['origin'],
                    "Roast Level": selected_bean['roast_level'],
                    "Manufacturer": selected_bean['manufacturer'],
                    "Process": selected_bean['process'],
                    "Variety": selected_bean['variety'],
                    "Elevation": selected_bean['elevation'],
                    "Manufacturer Website": selected_bean['manufacturer_website'],
                    "Price per lb": selected_bean['price_per_lb']
                }
                st.table(pd.DataFrame(bean_details.items(), columns=['Attribute', 'Value']))
                selected_bean_id = selected_bean['id']
                brewing_methods = fetch_brewing_methods(selected_bean_id)
                st.subheader("Brewing Methods for Selected Bean")
                st.dataframe(brewing_methods)
                selected_brewing_detail_id = st.selectbox("Select Brewing Method", [method['id'] for method in brewing_methods])
                if selected_brewing_detail_id:
                    tasting_notes = fetch_tasting_notes(selected_bean_id, selected_brewing_detail_id)
                    st.subheader("Tasting Notes for Selected Bean and Brewing Method")
                    st.dataframe(tasting_notes)

    elif path == "Brewing Method":
        brewing_methods = fetch_unique_values("type", "equipment")
        selected_brewing_method = st.selectbox("Select Brewing Method", brewing_methods)
        if selected_brewing_method:
            beans = fetch_beans('brew_method', selected_brewing_method)
            st.subheader("Beans Brewed with Method: " + selected_brewing_method)
            bean_names = [bean['name'] for bean in beans]
            selected_bean_name = st.selectbox("Select Bean", bean_names)
            if selected_bean_name:
                selected_bean = next(bean for bean in beans if bean['name'] == selected_bean_name)
                st.subheader("Details for Bean: " + selected_bean_name)
                bean_details = {
                    "ID": selected_bean['id'],
                    "Name": selected_bean['name'],
                    "Origin": selected_bean['origin'],
                    "Roast Level": selected_bean['roast_level'],
                    "Manufacturer": selected_bean['manufacturer'],
                    "Process": selected_bean['process'],
                    "Variety": selected_bean['variety'],
                    "Elevation": selected_bean['elevation'],
                    "Manufacturer Website": selected_bean['manufacturer_website'],
                    "Price per lb": selected_bean['price_per_lb']
                }
                st.table(pd.DataFrame(bean_details.items(), columns=['Attribute', 'Value']))
                selected_bean_id = selected_bean['id']
                brewing_methods = fetch_brewing_methods(selected_bean_id)
                st.subheader("Brewing Methods for Selected Bean")
                st.dataframe(brewing_methods)
                selected_brewing_detail_id = st.selectbox("Select Brewing Method", [method['id'] for method in brewing_methods])
                if selected_brewing_detail_id:
                    tasting_notes = fetch_tasting_notes(selected_bean_id, selected_brewing_detail_id)
                    st.subheader("Tasting Notes for Selected Bean and Brewing Method")
                    st.dataframe(tasting_notes)

    elif path == "Country of Origin":
        origins = fetch_unique_values("origin", "beans")
        selected_origin = st.selectbox("Select Country of Origin", origins)
        if selected_origin:
            beans = fetch_beans('origin', selected_origin)
            st.subheader("Beans from Country of Origin: " + selected_origin)
            bean_names = [bean['name'] for bean in beans]
            selected_bean_name = st.selectbox("Select Bean", bean_names)
            if selected_bean_name:
                selected_bean = next(bean for bean in beans if bean['name'] == selected_bean_name)
                st.subheader("Details for Bean: " + selected_bean_name)
                bean_details = {
                    "ID": selected_bean['id'],
                    "Name": selected_bean['name'],
                    "Origin": selected_bean['origin'],
                    "Roast Level": selected_bean['roast_level'],
                    "Manufacturer": selected_bean['manufacturer'],
                    "Process": selected_bean['process'],
                    "Variety": selected_bean['variety'],
                    "Elevation": selected_bean['elevation'],
                    "Manufacturer Website": selected_bean['manufacturer_website'],
                    "Price per lb": selected_bean['price_per_lb']
                }
                st.table(pd.DataFrame(bean_details.items(), columns=['Attribute', 'Value']))
                selected_bean_id = selected_bean['id']
                brewing_methods = fetch_brewing_methods(selected_bean_id)
                st.subheader("Brewing Methods for Selected Bean")
                st.dataframe(brewing_methods)
                selected_brewing_detail_id = st.selectbox("Select Brewing Method", [method['id'] for method in brewing_methods])
                if selected_brewing_detail_id:
                    tasting_notes = fetch_tasting_notes(selected_bean_id, selected_brewing_detail_id)
                    st.subheader("Tasting Notes for Selected Bean and Brewing Method")
                    st.dataframe(tasting_notes)

if __name__ == '__main__':
    main()
