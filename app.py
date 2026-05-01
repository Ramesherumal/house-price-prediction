import streamlit as st

st.title("🏠 House Price Prediction")

area = st.number_input("Area (sqft)", min_value=100)
bedrooms = st.number_input("Bedrooms", min_value=1)
bathrooms = st.number_input("Bathrooms", min_value=1)

if st.button("Predict"):
    price = area * 150 + bedrooms * 10000 + bathrooms * 8000
    st.success(f"Estimated Price: ${price:,.2f}")
