import streamlit as st

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction App")
st.write("Enter house details below to estimate the house price.")

st.markdown("---")

area = st.number_input("📐 Area in square feet", min_value=100, max_value=10000, value=1500)
bedrooms = st.slider("🛏️ Number of bedrooms", 1, 10, 3)
bathrooms = st.slider("🛁 Number of bathrooms", 1, 10, 2)

st.markdown("---")

if st.button("Predict House Price"):
    predicted_price = area * 150 + bedrooms * 10000 + bathrooms * 8000

    st.success(f"Estimated House Price: ${predicted_price:,.2f}")

    st.info(
        "Note: This is a demo version. The next upgrade is connecting the trained machine learning model."
    )

st.markdown("---")
st.caption("Developed by Ramesh | House Price Prediction using Machine Learning")
