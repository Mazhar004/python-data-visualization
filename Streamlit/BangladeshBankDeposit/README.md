# Bangladesh Bank Deposit Rate Analysis

An interactive dashboard for visualizing and comparing interest rates on deposit schemes offered by scheduled banks in Bangladesh. Built with Streamlit and Plotly, it transforms publicly available data from Bangladesh Bank into clear, comparative line charts spanning 2013 to 2023.

**[Live Demo](https://bdbankanalysis.streamlit.app/)**

---

## Features

- **Bank Wise Comparison** -- Select multiple banks and a deposit scheme to compare their interest rates side by side over time.
- **Deposit Wise Comparison** -- Pick a single bank and overlay multiple deposit tenures or amount tiers to see how its rates differ across schemes.
- **Three Deposit Categories** -- Supports Savings Deposit, Special Notice Deposit (SND) with five amount tiers, and Fixed Deposit with five tenure brackets.
- **60+ Banks Covered** -- Includes state-owned, private commercial, foreign, and specialized development banks.
- **Interactive Charts** -- Hover for exact rates, zoom into date ranges, and toggle traces on or off via the legend.
- **Automated Data Scraping** -- A standalone scraper pulls the latest data directly from the Bangladesh Bank website and processes it into analysis-ready CSV files.

## Screenshots

### Bank Wise Comparison

![Bank Wise Comparison](images/bank_wise.png)

### Deposit Wise Comparison

![Deposit Wise Comparison](images/deposit_wise.png)

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend / App Framework | Streamlit |
| Charting | Plotly |
| Data Processing | pandas |
| Data Scraping | requests, lxml, pandas.read_html |
| Language | Python 3.8+ |

## How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/Mazhar004/python-data-visualization.git
   cd python-data-visualization/Streamlit/BangladeshBankDeposit
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

4. **Launch the app**

   ```bash
   streamlit run app.py
   ```

   The dashboard will open in your browser at `http://localhost:8501`.

### Refreshing the Data

To pull the latest deposit rates from Bangladesh Bank and regenerate the CSV files, run:

```bash
python data_scrap.py
```

This scrapes all available monthly data from 2013 onward and writes both raw and processed CSV files into the `data/` directory.

## Project Structure

```
BangladeshBankDeposit/
├── app.py              # Streamlit application entry point
├── fig_generate.py     # Plotly chart generation
├── map_keys.py         # Bank abbreviation mappings, deposit types, and tenure definitions
├── data_scrap.py       # Web scraper for Bangladesh Bank deposit rate data
├── requirements.txt    # Python dependencies
├── data/               # Processed CSV data files
├── images/             # Screenshot assets for documentation
└── notebook/           # Jupyter notebook for exploratory analysis
```

## Data Source

All deposit rate data is sourced from the [Bangladesh Bank](https://www.bb.org.bd/en/index.php/financialactivity/interestdeposit) public portal.
