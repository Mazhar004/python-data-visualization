# COVID-19 Data Analysis

This section contains data analysis and visualization of global COVID-19 statistics, including confirmed cases, recoveries, and deaths across 185 countries. The analysis is implemented using two distinct approaches -- Matplotlib for static charts and Plotly for interactive visualizations -- each offering its own strengths for exploring pandemic data.

---

## Approaches

### [Matplotlib (Static Charts)](MatPlot/)

Uses Matplotlib to generate static visualizations exported as PNG images. Ideal for reports, presentations, and offline use. Includes bar charts, line graphs, word clouds, and country-level comparison plots.

**Notebooks:**
- `Bar.ipynb` -- Bar charts for top affected countries and comparative analysis
- `Graph.ipynb` -- Line graphs for country-level trend tracking over time

### [Plotly (Interactive Charts)](Plotly/)

Uses Plotly to generate interactive, browser-based visualizations with hover tooltips, zoom, and pan controls. Best suited for exploratory data analysis and web-based dashboards.

**Notebooks:**
- `Bar Chart.ipynb` -- Interactive bar charts with dynamic filtering
- `Graph Chart.ipynb` -- Interactive line charts for multi-country comparisons

---

## Sample Visualizations

### Word Cloud of COVID-19 Death Cases

![Word Cloud](MatPlot/images/COVID%20death%20casees%20as%20a%20WordCloud.png)

### Top 10 Countries by Confirmed Cases

![Top 10 Confirmed](MatPlot/images/Top%2010%20Country%20by%20COVID%20confirmation%20case.png)

### Country-wise Comparison (Matplotlib)

![Country Comparison](MatPlot/images/COVID-19%20Confirmed%20Cases%20Comparision%20Graph%20in%20Czechia%20Netherlands%20Bangladesh%20Turkey.png)

### US COVID-19 Trend Analysis (Plotly)

![US COVID Stats](MatPlot/images/US%20COVID%20stats%20analyze%20by%20line%20chart.png)

---

## Data Sources

| Source | Description |
|--------|-------------|
| [Humanitarian Data Exchange](https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases) | COVID-19 confirmed, recovered, and death case data by country |

The dataset covers 185 countries. A full list of included countries is available in the [Plotly README](Plotly/README.md).

### Data Files

**Matplotlib (`MatPlot/data/`):**
- `Confirmed.csv` -- Confirmed cases by country and date
- `Death.csv` -- Death cases by country and date
- `Recovered.csv` -- Recovery cases by country and date
- `Stat_updated.csv` -- Aggregated country-level statistics

**Plotly (`Plotly/data/`):**
- `full_stats.csv` -- Combined dataset with all metrics

---

## Project Structure

```
CoronaAffectedCountry/
├── MatPlot/
│   ├── Bar.ipynb
│   ├── Graph.ipynb
│   ├── data/
│   ├── images/
│   └── utils/
├── Plotly/
│   ├── Bar Chart.ipynb
│   ├── Graph Chart.ipynb
│   ├── data/
│   ├── images/
│   └── utils/
└── README.md
```
