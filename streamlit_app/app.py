import streamlit as st
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.rental_system import RentalSystem

st.set_page_config(
    page_title="Vehicle Rental System",
    layout="wide"
)


if "rental" not in st.session_state:
    st.session_state.rental = RentalSystem(
        vehicles_file="data/vehicles_100.json",
        customers_file="data/customers.json",
        log_file="data/logs.txt"
    )

st.title("🚗 Vehicle Rental Management Dashboard")
st.write("Use the left sidebar to navigate between pages.")