# Steel Logistics Optimization Dashboard 🚢

**[Click Here to View the Live Streamlit App]**(http://your-app-url.streamlit.app) 
*(Replace with your actual Streamlit app URL)*

This project is an end-to-end data engineering and data science solution that builds an optimization and decision-support tool for a steel plant's logistics team, as defined in the original problem statement.

## 🏛️ Project Architecture

This project uses a 100% free, cloud-native stack:

* **Processing (ETL):** **Google Colab (PySpark & PuLP)**
    * Runs a PySpark script to handle data transformation.
    * Runs a **PuLP (Python Linear Programming)** script to solve the "least-cost" optimization problem.
    * Runs a simple **Scikit-learn** model to predict and factor in demurrage (delay) costs.
* **Data Warehouse:** **Neon (Serverless PostgreSQL)**
    * Stores the final, clean output tables (`optimal_dispatch_plan`).
* **Frontend (UI):** **Streamlit Community Cloud**
    * Provides a live, public-facing dashboard for planners to view the optimal plan and "What-If" scenarios.



## 👨‍🍳 The "Chef" Logic: How It Works

This project goes beyond a simple ETL pipeline by implementing the core business logic.

1.  **AI-Powered Cost Prediction:** A simple regression model (Scikit-learn) is trained on historical data to predict potential port delays. This prediction is used to calculate a "risk-adjusted" demurrage cost.
2.  **Least-Cost Optimization (PuLP):** The system uses a linear programming model to find the cheapest way to get materials from ports to plants. It solves for the main objective:
    * **Minimize:** `Total_Transportation_Cost + Total_AI-Predicted_Demurrage_Cost`
3.  **Constraints:** The model must obey all business rules, such as:
    * Each plant must receive its required demand.
    * No port can ship more than its capacity.
4.  **"What-If" Analysis:** The script also runs a "What-If" scenario (e.g., "What if railway freight from Haldia doubles?") and saves *both* plans to the database, allowing planners to compare outcomes.

## 🚀 How to Run the Pipeline

1.  **Run the ETL Notebook:** Open the `Steel_Logistics_ETL.ipynb` notebook in Google Colab.
2.  **Add Secrets:** Add your Neon database connection string as a Colab secret named `NEON_CONN_STRING`.
3.  **Run All Cells:** Running the notebook will execute the full AI, Optimization, and ETL process, writing the final plan to the Neon database.
4.  **View the App:** The live Streamlit app will automatically show the updated data.
