# COVID-19 Global Data Visualization

Interactive visualizations of worldwide COVID-19 statistics -- confirmed cases, recoveries, and deaths -- built with Plotly and Pandas. The project provides multiple chart types to explore and compare pandemic data across 185+ countries.

## Features

- **Top-N Bar Charts** -- Rank countries by confirmed, recovered, or death counts with color-coded bars.
- **Stacked Bar Charts** -- Compare confirmed, recovered, and death figures side by side for the most affected countries.
- **Time-Series Line Charts** -- Track how case counts evolved over time for individual countries or multi-country comparisons.
- **Word Clouds** -- Visualize relative case magnitude across countries at a glance.
- **Flexible Data Fetching** -- Pull live data from the CSSE COVID-19 time-series repository or work offline with a local CSV cache.

## Sample Visualizations

### Stacked Bar Chart -- Cases by Country

![Stacked Bar Chart](../MatPlot/images/Country%20wise%20COVID%20Case%20study.png)

### Top 10 Countries by Confirmed Cases

![Top 10 Confirmed](../MatPlot/images/Top%2010%20Country%20by%20COVID%20confirmation%20case.png)

### US COVID-19 Stats Over Time

![US Stats Line Chart](../MatPlot/images/US%20COVID%20stats%20analyze%20by%20line%20chart.png)

### Death Cases as a Word Cloud

![Word Cloud](../MatPlot/images/COVID%20death%20casees%20as%20a%20WordCloud.png)

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| Plotly | Interactive charts (bar, line, image traces) |
| Plotly Express | High-level stacked bar charts |
| Pandas | Data loading, aggregation, and transformation |
| WordCloud | Word cloud generation from frequency data |
| Jupyter Notebook | Exploratory analysis and visualization |

## Data Sources

COVID-19 time-series data is sourced from the **CSSE COVID-19 Dataset** (Johns Hopkins University), accessed through the Humanitarian Data Exchange:

- Confirmed cases -- `time_series_covid19_confirmed_global.csv`
- Recovered cases -- `time_series_covid19_recovered_global.csv`
- Deaths -- `time_series_covid19_deaths_global.csv`

The dataset covers 185+ countries and territories from early 2020 onward.

## How to Run

1. **Install dependencies**

   ```bash
   pip install plotly pandas wordcloud notebook
   ```

2. **Launch Jupyter Notebook**

   ```bash
   cd CoronaAffectedCountry/Plotly
   jupyter notebook
   ```

3. **Open a notebook**

   - `Bar Chart.ipynb` -- bar charts, stacked bars, and word clouds.
   - `Graph Chart.ipynb` -- time-series line charts with country comparisons.

4. **Choose your data source**

   Each notebook calls `get_data()` from `utils/fetch_data.py`. Pass `online=True` to fetch the latest data from the remote repository, or `online=False` to use the local CSV cache in `data/`.

## Project Structure

```
Plotly/
├── Bar Chart.ipynb        # Bar charts, stacked bars, and word clouds
├── Graph Chart.ipynb      # Time-series line charts
├── README.md
├── data/
│   └── full_stats.csv     # Local CSV cache of COVID-19 data
└── utils/
    ├── bar_chart.py       # DataFrame formatting and color helpers
    └── fetch_data.py      # Data fetching (online/offline) and parsing
```
