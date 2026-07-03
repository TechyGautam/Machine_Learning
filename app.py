import streamlit as st
import joblib

model = joblib.load("house_price_model_rf.pkl")
scaler = joblib.load("house_price_scaler.pkl")

#  making UI
st.title("🏠:blue[Predict] :red[House] :blue[Price]")
st.divider()

overall_qual = st.slider(
    "Overall Quality (1-10)",
    1, 10, 5
)

gr_liv_area = st.number_input(
    "Living Area (sq ft)",
    min_value=0,
    value = None
)

garage_cars = st.number_input(
    "Garage Capacity (cars)",
    min_value=0,
    value = None
)

garage_area = st.number_input(
    "Garage Area (sq ft)",
    min_value=0,
    value = None
)

total_bsmt_sf = st.number_input(
    "Basement Area (sq ft)",
    min_value=0,
    value = None
)

first_flr_sf = st.number_input(
    "1st Floor Area (sq ft)",
    min_value=0,
    value = None
)

full_bath = st.number_input(
    "Number of Full Bathrooms",
    min_value=0,
    value = None
)

tot_rooms = st.number_input(
    "Total Rooms Above Ground",
    min_value=0,
    value = None
)

year_built = st.number_input(
    "Year Built",
    min_value=1800,
    max_value=2026
)

year_remod = st.number_input(
    "Year Remodeled",
    min_value=1800,
    max_value=2026
)
if st.button("Predict Price"):
    input_data = [[
        overall_qual,
        gr_liv_area,
        garage_cars,
        garage_area,
        total_bsmt_sf,
        first_flr_sf,
        full_bath,
        tot_rooms,
        year_built,
        year_remod
    ]]
    input_scaled = scaler.transform(input_data)
    # predicted_price = model.predict(input_scaled)
    # st.success(f"Estimated House Price: ${predicted_price[0]:,.2f}")
    predicted_price2 = model.predict(input_scaled)
    st.success(f"Estimated House Price: ${predicted_price2[0]:,.2f}")