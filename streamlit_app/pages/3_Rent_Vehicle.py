import streamlit as st

rental = st.session_state.rental

st.title("📝 Rent Vehicle")

available = [v for v in rental.vehicles if v.is_available()]
options = {f"{v.get_name()} ({v.get_number()})": v.get_number() for v in available}

if not options:
    st.warning("No vehicles available.")
    st.stop()

selected = st.selectbox("Select Vehicle", list(options.keys()))
vehicle_no = options[selected]

name = st.text_input("Customer Name")
phone = st.text_input("Phone Number")
days = st.number_input("Number of Days", min_value=1)

if st.button("Rent Vehicle"):
    success, message = rental.rent_vehicle(vehicle_no, name, phone, days)

    if success:
        st.success(f"Success! Total Cost: ₹{message}")
    else:
        st.error(message)