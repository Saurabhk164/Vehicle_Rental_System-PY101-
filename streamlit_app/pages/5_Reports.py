import streamlit as st
import pandas as pd
import plotly.express as px

rental = st.session_state.rental

st.title("📈 Reports & Analytics")

vehicles = rental.vehicles
data = {
    "Type": [],
    "Availability": [],
    "Rate": []
}

for v in vehicles:
    data["Type"].append("Car" if v.get_rate() > 900 else "Bike")
    data["Availability"].append("Available" if v.is_available() else "Rented")
    data["Rate"].append(v.get_rate())

df = pd.DataFrame(data)

# Availability Pie
st.subheader("Vehicle Availability")
fig1 = px.pie(df, names="Availability")
st.plotly_chart(fig1, use_container_width=True)

# Rate Comparison Bar Chart
st.subheader("Rate Comparison")
fig2 = px.bar(df, x="Type", y="Rate", color="Availability")
st.plotly_chart(fig2, use_container_width=True)

# Logs
st.subheader("Rental Logs")
try:
    with open("data/logs.txt", "r") as f:
        logs = f.read()
        st.text(logs)
except:
    st.info("No logs found.")
