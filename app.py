import streamlit as st
import psycopg2
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(layout="wide")
st.title("Steel Plant Logistics Optimization 🚢")

# --- DATABASE CONNECTION ---

# Function to initialize the database connection
def init_connection():
    try:
        # Get the connection string from Streamlit's secrets
        conn_string = st.secrets["database"]["connection_string"]
        return psycopg2.connect(conn_string)
    except Exception as e:
        st.error(f"Error connecting to database: {e}")
        return None

# Function to run a query, with caching
@st.cache_data(ttl=60)  # Cache the data for 60 seconds
def run_query(query):
    try:
        conn = init_connection()
        if conn:
            with conn.cursor() as cur:
                cur.execute(query)
                # Fetch results into a pandas DataFrame
                df = pd.DataFrame(cur.fetchall(), columns=[desc[0] for desc in cur.description])
                return df
    except Exception as e:
        st.error(f"Error running query: {e}")
    return pd.DataFrame() # Return empty dataframe on error

# --- APP LAYOUT ---

st.header("Project Overview")
st.write("""
This project demonstrates an end-to-end data engineering pipeline.
- **Processing:** PySpark running in a Google Colab notebook.
- **Database:** Live PostgreSQL database hosted on Neon.
- **UI:** This dashboard, built with Streamlit.
""")

st.header("What-If Analysis (Coming Soon...)")
st.write("This section will allow planners to simulate different scenarios.")

# --- DISPLAY DATABASE DATA ---

st.header("Live Database View")
st.write("This table is reading *live* from the Neon database. It's empty now, but will populate after we run the processing script.")

# Try to fetch data from a table named 'optimal_dispatch_plan'
# This will show an error at first, which is 100% OK!
try:
    df = run_query("SELECT * FROM optimal_dispatch_plan")
    
    if df.empty:
        st.warning("No data found in 'optimal_dispatch_plan'. Please run the processing notebook.")
        st.dataframe(df)
    else:
        st.success("Successfully fetched data!")
        st.dataframe(df)
        
except Exception as e:
    st.error(f"An error occurred. The table 'optimal_dispatch_plan' might not exist yet. {e}")
