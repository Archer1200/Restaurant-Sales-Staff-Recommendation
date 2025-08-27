import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import math


st.title("🍽 Restaurant Sales & Staff Recommendation")

uploaded_file = st.file_uploader("Upload restaurant sales CSV", type=["csv"])

if uploaded_file:
    
    df = pd.read_csv(uploaded_file)
    df['Date'] = pd.to_datetime(df['Date'])
    df['DayOfWeek'] = df['Date'].dt.dayofweek

    df['Weather'] = df['Weather'].astype('category').cat.codes
    df['Holiday'] = df['Holiday'].map({'Yes': 1, 'No': 0})

    X = df[['DayOfWeek', 'Weather', 'Holiday', 'Customers']]
    y = df['Sales']

    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    
    preds = model.predict(X_test)
    rmse = math.sqrt(mean_squared_error(y_test, preds))
    st.success(f"✅ Model trained successfully! RMSE: {rmse:.2f}")

    
    st.subheader(" Future Predictions")
    n_days = st.slider("Select number of future days to predict", 7, 60, 30)

    future_dates = pd.date_range(start=df['Date'].max() + pd.Timedelta(days=1), periods=n_days)
    future_data = pd.DataFrame({
        'Date': future_dates,
        'DayOfWeek': future_dates.dayofweek,
        'Weather': np.random.randint(0, 4, size=n_days),  
        'Holiday': np.random.randint(0, 2, size=n_days),  
        'Customers': np.random.randint(80, 200, size=n_days)  
    })

    future_sales = model.predict(future_data[['DayOfWeek', 'Weather', 'Holiday', 'Customers']])
    future_data['PredictedSales'] = future_sales

   
    avg_customers_per_staff = st.number_input("Average customers per staff", min_value=10, max_value=100, value=30)
    future_data['StaffNeeded'] = future_data['Customers'].apply(lambda x: math.ceil(x / avg_customers_per_staff))

    
    st.dataframe(future_data.head())

    csv = future_data.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Staff Plan CSV", data=csv, file_name="staff_plan.csv", mime="text/csv")
else:
    st.info("Please upload a CSV file to begin.")
