import streamlit as st
from db_utils import fetch_unique_values, fetch_beans, fetch_brewing_methods, fetch_tasting_notes, fetch_tasting_note_details
import pandas as pd
import matplotlib.pyplot as plt

def display_tasting_note_card(tasting_note_id):
    details = fetch_tasting_note_details(tasting_note_id)
    if details:
        card_html = f"""
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); margin-top: 20px;">
            <h3>{details['bean_name']}</h3>
            <p><strong>Date:</strong> {details['tasting_date']}</p>
            <p><strong>Aroma:</strong> {details['aroma']}</p>
            <p><strong>Body:</strong> {details['body']}</p>
            <p><strong>Flavor Profile:</strong> {details['flavor_profile']}</p>
            <p><strong>Rating:</strong> {details['rating']}</p>
            <p><strong>Notes:</strong> {details['notes']}</p>
            <h4>Brewing Details</h4>
            <p><strong>Grind Size:</strong> {details['grind_size']}</p>
            <p><strong>Brew Time:</strong> {details['brew_time']}</p>
            <p><strong>Temperature:</strong> {details['temperature']}</p>
            <p><strong>Brewing Notes:</strong> {details['brewing_notes']}</p>
            <p><strong>Equipment Type:</strong> {details['equipment_type']}</p>
        </div>
        """
        st.markdown(card_html, unsafe_allow_html=True)
    else:
        st.write("No details available for this tasting note.")

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
                    selected_tasting_note_id = st.selectbox("Select Tasting Note", [note['id'] for note in tasting_notes])
                    if selected_tasting_note_id:
                        display_tasting_note_card(selected_tasting_note_id)

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
                    selected_tasting_note_id = st.selectbox("Select Tasting Note", [note['id'] for note in tasting_notes])
                    if selected_tasting_note_id:
                        display_tasting_note_card(selected_tasting_note_id)

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
                    selected_tasting_note_id = st.selectbox("Select Tasting Note", [note['id'] for note in tasting_notes])
                    if selected_tasting_note_id:
                        display_tasting_note_card(selected_tasting_note_id)

if __name__ == '__main__':
    main()
