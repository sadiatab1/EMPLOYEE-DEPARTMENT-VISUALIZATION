"""
create_employee_viz.py
- Generates a synthetic employee dataset (100 rows).
- Produces: employee_visualization.html
Verification email included: 23f3004490@ds.study.iitm.ac.in
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio
from pathlib import Path
import random

HTML_OUT = Path("employee_viz.html")


def generate_data(n=100):
    departments = ["HR", "Marketing", "Finance", "Operations", "IT", "Sales"]
    regions = ["Latin America", "Middle East", "Africa", "Europe", "Asia"]

    data = []
    for i in range(1, n+1):
        emp_id = f"EMP{i:03d}"
        dept = random.choice(departments)
        region = random.choice(regions)
        perf = round(np.random.uniform(50, 100), 2)   # performance score
        exp = random.randint(1, 20)                   # years of experience
        sat = round(np.random.uniform(1, 5), 1)       # satisfaction rating
        data.append([emp_id, dept, region, perf, exp, sat])

    df = pd.DataFrame(data, columns=[
        "employee_id", "department", "region", "performance_score",
        "years_experience", "satisfaction_rating"
    ])
    return df

def count_finance(df):
    dept_norm = df['department'].astype(str).str.strip().str.lower()
    finance_count = (dept_norm == 'finance').sum()
    return int(finance_count)

def make_histogram(df):
    fig = px.histogram(
        df,
        x='department',
        title='Distribution of Employees by Department',
        labels={'department': 'Department', 'count': 'Number of Employees'}
    )
    fig.update_layout(xaxis={'categoryorder':'total descending'}, bargap=0.2)
    return fig

def save_html(fig, finance_count, html_path):
    plot_html = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')
    html_content = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>Employee Department Visualization</title>
  <meta name="author" content="Sadia - 23f3004490@ds.study.iitm.ac.in" />
  <style>
    body {{ font-family: Arial, sans-serif; margin: 24px; }}
    .badge {{ display:inline-block; padding:6px 10px; background:#efefef; border-radius:6px; }}
  </style>
</head>
<body>
  <h1>Employee Department Visualization</h1>
  <div class="badge"><strong>Finance department count:</strong> {finance_count}</div>
  {plot_html}
  <p>Verification email: 23f3004490@ds.study.iitm.ac.in</p>
</body>
</html>
"""
    html_path.write_text(html_content, encoding='utf-8')
    print(f"Saved HTML to: {html_path.resolve()}")

def main():
    print("Generating synthetic employee dataset...")
    df = generate_data()

    finance_count = count_finance(df)
    print(f"Finance department frequency count: {finance_count}")

    fig = make_histogram(df)
    save_html(fig, finance_count, HTML_OUT)

def main():
    print("Generating synthetic employee dataset...")
    df = generate_data()
    print(df.head())   # 👈 show first few rows

    finance_count = count_finance(df)
    print(f"Finance department frequency count: {finance_count}")

    fig = make_histogram(df)
    print("About to save HTML file...")   # 👈 debug print
    save_html(fig, finance_count, HTML_OUT)
    print("Done ✅")   # 👈 confirm finish

if __name__ == "__main__":
    main()

