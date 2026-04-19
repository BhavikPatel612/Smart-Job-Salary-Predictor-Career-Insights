import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression

# Page config
st.set_page_config(page_title="Salary Predictor", layout="wide")

# Load data
df = pd.read_csv("data/salary_data.csv")

# Train model
X = df[["experience"]]
y = df["salary_lpa"]

model = LinearRegression()
model.fit(X, y)

# Options
SKILLS = ["Python", "SQL", "Machine Learning", "Java", "AWS"]
CITIES = ["Bangalore", "Mumbai", "Delhi", "Pune"]

# Title
st.markdown("## 💼 Salary Predictor")
st.markdown("---")
# Layout
col1, col2 = st.columns([1, 2])

# LEFT SIDE
with col1:
    st.markdown("### 📋 Your Details")
    
    experience = st.slider("Years of Experience", 0, 15, 0)
    city = st.selectbox("City", CITIES)
    skills = st.multiselect("Skills", SKILLS)

    predict = st.button("🔮 Predict Salary", use_container_width=True)

# 👉 Single prediction logic
salary = None

if predict:
    if len(skills) == 0:
        st.error("Please select at least one skill")
    else:
        salary = model.predict([[experience]])[0]

# RIGHT SIDE (GRAPH)
with col2:
    st.markdown("### 📊 Salary Insights")

    fig = px.scatter(
        df,
        x="experience",
        y="salary_lpa",
        color="salary_lpa",
        color_continuous_scale="blues",
        template="plotly_white"
    )

    # Graph styling
    fig.update_traces(marker=dict(size=8, opacity=0.6))
    fig.update_layout(height=300,margin=dict(l=5, r=10, t=40, b=10))

    # Show prediction point
    if salary is not None:
        fig.add_scatter(
            x=[experience],
            y=[salary],
            mode="markers",
            marker=dict(size=14, color="red"),
            name="Your Prediction"
        )

    st.plotly_chart(fig, use_container_width=True)

# RESULT
if salary is not None:
    st.markdown("### 💰 Result")
    st.metric("Estimated Salary", f"₹{salary:.2f} LPA")