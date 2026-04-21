import streamlit as st

rental = st.session_state.rental

st.title("🔄 Return Vehicle")

rented = [v for v in rental.vehicles if not v.is_available()]
options = {f"{v.get_name()} ({v.get_number()})": v.get_number() for v in rented}

if not options:
    st.info("No vehicles are currently rented.")
    st.stop()

selected = st.selectbox("Select Vehicle", list(options.keys()))
vehicle_no = options[selected]

if st.button("Return Vehicle"):
    success, message = rental.return_vehicle(vehicle_no)

    if success:
        st.success(message)
    else:
        st.error(message)