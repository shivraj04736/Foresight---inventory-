import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title="FORESIGHT - NorthBay Living", layout="wide")
st.title("🔮 Project FORESIGHT")
st.subheader("AI-Powered Demand & Inventory Intelligence - NorthBay Living")
np.random.seed(42)
skus = [f"NB-SKU-{i:03d}" for i in range(1, 21)]
data = []
for sku in skus:
    price = np.random.randint(499, 4999)
    stock = np.random.randint(0, 500)
    avg_weekly = np.random.randint(10, 100)
    forecast_8w = int(avg_weekly * 8 * np.random.uniform(0.8, 1.3))
    sales_risk = max(0, forecast_8w - stock) * price
    if stock < forecast_8w * 0.5:
        risk, action = "🔴 Stockout Risk", "Reorder Urgently"
    elif stock > forecast_8w * 1.5:
        risk, action = "🟡 Overstock", "Discount / Clear Stock"
    else:
        risk, action = "🟢 Healthy", "No Action"
    data.append([sku, price, stock, avg_weekly, forecast_8w, risk, action, sales_risk])
df = pd.DataFrame(data, columns=["SKU","Price","Stock","Avg Weekly Sales","Forecast 8W","Risk","Action","Sales at Risk"])
c1,c2,c3,c4 = st.columns(4)
c1.metric("Total SKUs", len(df))
c2.metric("Stockout Risk", len(df[df['Risk'].str.contains('Stockout')]))
c3.metric("Overstock", len(df[df['Risk'].str.contains('Overstock')]))
c4.metric("Sales at Risk", f"Rs.{df['Sales at Risk'].sum():,}")
st.dataframe(df, use_container_width=True)
sel = st.selectbox("Select SKU", df["SKU"])
row = df[df["SKU"]==sel].iloc[0]
st.write(f"### {sel} - {row['Risk']}")
st.write(f"Action: **{row['Action']}**")
