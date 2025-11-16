# --- APP LAYOUT (Replace the old layout with this) ---

st.header("Project Overview")
st.write("""
This project demonstrates an end-to-end data engineering pipeline.
- **Processing:** PySpark, PuLP (Optimization), and Scikit-learn (AI) in a Google Colab notebook.
- **Database:** Live PostgreSQL database hosted on Neon.
- **UI:** This dashboard, built with Streamlit.
""")

st.header("What-If Analysis")
st.write("This table reads the optimized plan from the database. Use the selector to compare the 'Optimal Plan' with a 'What-If' scenario.")

# --- DISPLAY DATABASE DATA ---

plan_type = st.selectbox(
    "Select Plan to View:",
    ("Optimal Plan", "What-If Scenario 1")
)

# This is the new logic to show different plans
if plan_type == "Optimal Plan":
    # This query finds the plan we created in the roadmap
    query = "SELECT * FROM optimal_dispatch_plan WHERE plan_id LIKE 'PLAN_%'"
    st.info("Showing the AI-driven, least-cost plan.")
else:
    # This query finds the "what-if" plan
    query = "SELECT * FROM optimal_dispatch_plan WHERE plan_id LIKE 'WHAT_IF_%'"
    st.warning("Showing the What-If Scenario: 'Railway freight from Haldia doubled.'")

try:
    df = run_query(query)
    
    if df.empty:
        st.warning("No data found. Please run the processing notebook in Google Colab.")
        st.dataframe(df)
    else:
        st.success("Successfully fetched data!")
        st.dataframe(df)
        
        # Show a summary
        total_cost = df['total_cost_usd'].sum()
        total_tons = df['quantity_tonnes'].sum()
        st.subheader(f"Total Cost for this Plan: ${total_cost:,.2f}")
        st.subheader(f"Total Tons Shipped: {total_tons:,.0f} T")

except Exception as e:
    st.error(f"An error occurred. The table 'optimal_dispatch_plan' might not exist yet. {e}")
