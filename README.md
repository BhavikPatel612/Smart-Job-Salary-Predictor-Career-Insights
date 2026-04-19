# 💼 Smart Job Salary Predictor + Career Insights

An ML-powered Streamlit web app that predicts your salary in the Indian IT job market based on your skills, experience, and city — and tells you exactly which skill will boost your pay the most.

---

## Features

- Salary prediction using **Linear Regression** and **Random Forest**
- Interactive **salary gauge** (Entry / Mid / Senior / Expert levels)
- **Feature importance chart** — what actually drives salaries
- **Skill-Up "What-If" analysis** — "If I learn Python, my salary goes up by ₹X LPA"
- No external dataset needed — generates 6,000 realistic synthetic samples on first run

---

## Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the app

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`

---

## Deploy on Streamlit Community Cloud (Free — Custom Domain Supported)

This is the easiest way to get the app live on your domain.

### Step 1 — Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/salary-predictor.git
git push -u origin main
```

### Step 2 — Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
2. Click **"New app"** → select your repo → set `app.py` as the main file
3. Click **"Deploy"** — your app goes live at `https://your-app.streamlit.app`

### Step 3 — Connect Your Own Domain

1. In your Streamlit Cloud dashboard → open your app settings
2. Go to **"Custom domain"** and enter your domain (e.g. `salary.yourdomain.com`)
3. Add a CNAME record in your domain registrar's DNS settings:
   - **Type:** CNAME
   - **Name:** `salary` (or `@` for root domain)
   - **Value:** `your-app.streamlit.app`
4. Wait 5–15 minutes for DNS propagation — done!

---

## Project Structure

```
ML Project/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

---

## Tech Stack

| Component        | Technology                  |
|------------------|-----------------------------|
| UI Framework     | Streamlit                   |
| ML Models        | scikit-learn (LR + RF)      |
| Charts           | Plotly                      |
| Data             | Synthetic (NumPy generated) |
| Language         | Python 3.9+                 |
