import streamlit as st
import pandas as pd

rental = st.session_state.rental

st.title("📊 Dashboard Overview")

vehicles = rental.vehicles
vehicle_data = []

for v in vehicles:
    vehicle_data.append({
        "Name": v.get_name(),
        "Number": v.get_number(),
        "Type": "Car" if v.get_rate() > 900 else "Bike",
        "Availability": "Available" if v.is_available() else "Rented",
        "Rate": v.get_rate()
    })

df = pd.DataFrame(vehicle_data)

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Vehicles", len(df))
col2.metric("Available", len(df[df["Availability"] == "Available"]))
col3.metric("Rented", len(df[df["Availability"] == "Rented"]))

st.divider()
st.subheader("Live Rentals")
st.dataframe(df[df["Availability"] == "Rented"], use_container_width=True)