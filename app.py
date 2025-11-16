import streamlit as st

st.set_page_config(layout="wide")

st.title("Steel Plant Logistics Optimization 🚢")

st.header("Project Overview")
st.write("""
This project demonstrates an end-to-end data engineering pipeline.
- **Processing:** PySpark running in a Google Colab notebook.
- **Database:** Live PostgreSQL database hosted on Neon.
- **UI:** This dashboard, built with Streamlit.
""")

st.header("What-If Analysis (Coming Soon...)")
st.write("This section will allow planners to simulate different scenarios.")

st.header("Raw Data (Coming Soon...)")
st.write("This section will show the final, clean data from the database.")
