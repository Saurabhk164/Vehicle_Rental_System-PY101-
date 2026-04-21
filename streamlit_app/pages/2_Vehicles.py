import streamlit as st
import pandas as pd

rental = st.session_state.rental

st.title("🚗 All Vehicles")

vehicles = rental.vehicles
vehicle_data = []

for v in vehicles:
    vehicle_data.append({
        "Name": v.get_name(),
        "Number": v.get_number(),
        "Type": "Car" if v.get_rate() > 900 else "Bike",
        "Availability": "Available" if v.is_available() else "Rented",
        "Rate/Day": v.get_rate(),
        "Fuel": v.get_fuel(),
        "Year": v.get_year()
    })

df = pd.DataFrame(vehicle_data)

# Filters
type_filter = st.selectbox("Filter by Type", ["All", "Car", "Bike"])
availability_filter = st.selectbox("Availability", ["All", "Available", "Rented"])
search = st.text_input("Search Name / Number")

filtered_df = df.copy()

if type_filter != "All":
    filtered_df = filtered_df[filtered_df["Type"] == type_filter]

if availability_filter != "All":
    filtered_df = filtered_df[filtered_df["Availability"] == availability_filter]

if search:
    filtered_df = filtered_df[
        filtered_df.apply(
            lambda row: search.lower() in row.astype(str).str.lower().to_string(),
            axis=1
        )
    ]

st.dataframe(filtered_df, use_container_width=True)