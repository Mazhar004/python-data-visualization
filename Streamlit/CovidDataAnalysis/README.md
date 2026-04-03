# COVID-19 Data Visualization

An interactive web dashboard for exploring COVID-19 statistics across countries and time periods. Built with Streamlit and Plotly, it provides line charts for country-level trend comparisons and bar charts highlighting the most affected nations worldwide.

**[Live Demo](https://visualcovid.streamlit.app/)**

---

## Features

- **Country Comparison Line Charts** -- Select multiple countries and data types (Confirmed, Recovered, Death) to visualize trends over a customizable date range.
- **Top Affected Countries Bar Charts** -- Rank the most impacted countries by a selected metric, with configurable top-K filtering (10 to 30).
- **Interactive Date Range Slider** -- Narrow down the analysis window using an intuitive slider control.
- **Dynamic Filtering** -- Choose data types and countries on the fly; charts update instantly.

## Screenshots

### Country-wise Trend Comparison

![Country-wise line chart comparison](images/covid_line.png)

### Top Affected Countries

![Bar chart of top affected countries](images/covid_bar.png)

## Tech Stack

| Layer          | Technology              |
|----------------|-------------------------|
| Frontend / UI  | Streamlit 1.22          |
| Charting       | Plotly 5.14             |
| Data Handling  | Pandas                  |
| Language       | Python 3.8+             |

## How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/Mazhar004/python-data-visualization.git
   cd python-data-visualization/Streamlit/CovidDataAnalysis
   ```

2. **Create a virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

   The app will open in your default browser at `http://localhost:8501`.

## Project Structure

```
CovidDataAnalysis/
├── app.py                    # Application entry point and data loading
├── covid_streamlit_view.py   # Streamlit layout and widget definitions
├── covid_fig.py              # Plotly figure builders (line and bar charts)
├── utils.py                  # Helper functions (date filtering, color mapping)
├── requirements.txt          # Python dependencies
├── images/                   # Screenshot assets
│   ├── covid_line.png
│   └── covid_bar.png
└── README.md
```

## Data Source

COVID-19 case data sourced from the [Humanitarian Data Exchange](https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases).
