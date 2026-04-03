<div align="center">

# Python Data Visualization

**A collection of data visualization projects built with Python -- from interactive Streamlit dashboards to Jupyter notebook explorations.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Apps-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/github/license/Mazhar004/python-data-visualization?style=for-the-badge)](LICENSE)

[View on GitHub Pages](https://mazhar004.github.io/python-data-visualization/)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Streamlit Web Apps](#streamlit-web-apps)
  - [COVID-19 Data Analysis](#covid-19-data-analysis)
  - [Call Log Analysis](#call-log-analysis)
  - [Bangladesh Bank Deposit Rates](#bangladesh-bank-deposit-rates)
- [Notebook Projects](#notebook-projects)
  - [Corona Affected Country (Plotly)](#corona-affected-country-plotly)
  - [Corona Affected Country (Matplotlib)](#corona-affected-country-matplotlib)
  - [SSC Scholarship 2022](#ssc-scholarship-2022)
  - [KUET Student Gender Ratio](#kuet-student-gender-ratio)
  - [Matplotlib 2D and 3D Plots](#matplotlib-2d-and-3d-plots)
  - [Geometric Shapes](#geometric-shapes)
  - [Progress Bar](#progress-bar)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [License](#license)
- [Links](#links)

---

## Overview

This repository is a growing collection of Python-based data visualization projects. It covers a range of techniques -- from static charts in Matplotlib to interactive plots in Plotly and full web dashboards built with Streamlit. Each sub-project lives in its own directory with dedicated data, notebooks, and output images.

The projects span real-world datasets (COVID-19 statistics, bank interest rates, scholarship results) as well as mathematical and algorithmic visualizations (geometric shapes, prime number patterns, 3D surfaces).

---

## Project Structure

```
python-data-visualization/
|
|-- CoronaAffectedCountry/
|   |-- MatPlot/             # COVID-19 analysis using Matplotlib
|   +-- Plotly/              # COVID-19 analysis using Plotly
|
|-- Streamlit/
|   |-- CovidDataAnalysis/   # Streamlit dashboard for COVID-19 data
|   |-- CallLogAnalysis/     # Streamlit dashboard for call log insights
|   +-- BangladeshBankDeposit/ # Streamlit dashboard for bank deposit rates
|
|-- SSCScholarship/          # SSC 2022 scholarship PDF extraction and viz
|-- KuetStudentGenderRatio/  # Web-scraped gender ratio analysis (KUET)
|-- Matplot2D3D/             # 2D and 3D mathematical plots
|-- GeometricShape/          # CLI and graphical geometric shapes
+-- ProgressBar/             # Terminal progress bar utility
```

---

## Streamlit Web Apps

Three interactive dashboards deployed on Streamlit Cloud.

### COVID-19 Data Analysis

[![Streamlit App](https://img.shields.io/badge/Live_Demo-visualcovid.streamlit.app-FF4B4B?style=flat-square&logo=streamlit)](https://visualcovid.streamlit.app/)
![Plotly](https://img.shields.io/badge/Plotly-239120?style=flat-square&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

Visual representation of COVID-19 confirmed, recovered, and death cases -- filterable by country with line and bar chart views. Data sourced from the [Humanitarian Data Exchange](https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases).

<img src="Streamlit/CovidDataAnalysis/images/covid_line.png" alt="COVID-19 Streamlit Dashboard" width="700">

> [Project folder](Streamlit/CovidDataAnalysis/) -- [Live demo](https://visualcovid.streamlit.app/)

---

### Call Log Analysis

[![Streamlit App](https://img.shields.io/badge/Live_Demo-calllog.streamlit.app-FF4B4B?style=flat-square&logo=streamlit)](https://calllog.streamlit.app/)
![Plotly](https://img.shields.io/badge/Plotly-239120?style=flat-square&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

Analyzes call logs to uncover communication patterns: call frequency, duration, missed calls, rejected calls, and hourly call schedules. Supports both aggregate and per-person breakdowns. Uses artificially generated sample data.

<img src="Streamlit/CallLogAnalysis/images/Person_Wise_Analysis.png" alt="Call Log Analysis" width="700">

> [Project folder](Streamlit/CallLogAnalysis/) -- [Live demo](https://calllog.streamlit.app/)

---

### Bangladesh Bank Deposit Rates

[![Streamlit App](https://img.shields.io/badge/Live_Demo-bdbankanalysis.streamlit.app-FF4B4B?style=flat-square&logo=streamlit)](https://bdbankanalysis.streamlit.app/)
![Plotly](https://img.shields.io/badge/Plotly-239120?style=flat-square&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![lxml](https://img.shields.io/badge/lxml-Web_Scraping-blue?style=flat-square)

Interest rate comparison across scheduled banks in Bangladesh. Provides bank-wise and deposit-scheme-wise visual comparisons. Data sourced from [Bangladesh Bank](https://www.bb.org.bd/en/index.php/financialactivity/interestdeposit).

<img src="Streamlit/BangladeshBankDeposit/images/bank_wise.png" alt="Bangladesh Bank Deposit Analysis" width="700">

> [Project folder](Streamlit/BangladeshBankDeposit/) -- [Live demo](https://bdbankanalysis.streamlit.app/)

---

## Notebook Projects

Standalone Jupyter notebook explorations covering diverse datasets and techniques.

### Corona Affected Country (Plotly)

![Plotly](https://img.shields.io/badge/Plotly-239120?style=flat-square&logo=plotly&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

Interactive COVID-19 visualizations using Plotly -- word clouds, country comparisons, per-country statistics, and top-10 rankings. Covers 185 countries with real-time data.

<img src="CoronaAffectedCountry/MatPlot/images/COVID%20death%20casees%20as%20a%20WordCloud.png" alt="COVID Word Cloud (Plotly)" width="700">

> [Project folder](CoronaAffectedCountry/Plotly/)

---

### Corona Affected Country (Matplotlib)

![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

The same COVID-19 dataset visualized with Matplotlib -- bar charts, line graphs, word clouds, and worldwide statistics.

<img src="CoronaAffectedCountry/MatPlot/images/Corona%20Stats%20Country%20wise.png" alt="COVID Word Cloud (Matplotlib)" width="700">

> [Project folder](CoronaAffectedCountry/MatPlot/)

---

### SSC Scholarship 2022

![Plotly](https://img.shields.io/badge/Plotly-239120?style=flat-square&logo=plotly&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![PDF](https://img.shields.io/badge/PDF_Extraction-red?style=flat-square)

Extracts scholarship data from a publicly available PDF (Dinajpur Education Board), cleans and structures it into a DataFrame, then visualizes results using Plotly with various grouping strategies.

<img src="SSCScholarship/images/top%20200.png" alt="SSC Scholarship Top 200" width="700">

> [Project folder](SSCScholarship/)

---

### KUET Student Gender Ratio

![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Web Scraping](https://img.shields.io/badge/Web_Scraping-blue?style=flat-square)

Scrapes real-time student enrollment data from the KUET official portal and visualizes department-wise gender ratios.

<img src="KuetStudentGenderRatio/images/Percentage%20of%20Boys%20%26%20Girls%20Department%20wise%20in%20KUET%20(27%20October%202019).png" alt="KUET Gender Ratio" width="700">

> [Project folder](KuetStudentGenderRatio/)

---

### Matplotlib 2D and 3D Plots

![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

Mathematical art with Matplotlib: heart curves, 3D normal distribution surfaces, prime number spiral patterns, and random sine compositions.

<img src="Matplot2D3D/images/Heart.png" alt="Heart Shape Plot" width="400">

> [Project folder](Matplot2D3D/)

---

### Geometric Shapes

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat-square)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

Generates geometric shapes both as terminal text output (triangle, right triangle, square, rectangle, crown) and as graphical plots (rectangle, circle). The input parameter `n` controls the number of lines or size.

<img src="GeometricShape/images/Crown.png" alt="Crown Shape" width="400">

> [Project folder](GeometricShape/)

---

### Progress Bar

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

A simple terminal progress bar function. Takes a `value` and `maximum`, rescales to percentage, and prints a visual bar to the console.

<img src="ProgressBar/images/progress%20bar.png" alt="Progress Bar" width="500">

> [Project folder](ProgressBar/)

---

## Tech Stack

| Category | Technologies |
|---|---|
| **Language** | Python 3.8+ |
| **Visualization** | Matplotlib, Plotly, WordCloud |
| **Web Framework** | Streamlit |
| **Data Processing** | Pandas, NumPy |
| **Web Scraping** | lxml, Requests |
| **PDF Processing** | PDF extraction (tabula / custom) |
| **Notebooks** | Jupyter Notebook |
| **Containerization** | Docker, Docker Compose |
| **Deployment** | Streamlit Cloud, GitHub Pages |

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Clone the repository

```bash
git clone https://github.com/Mazhar004/python-data-visualization.git
cd python-data-visualization
```

### Option 1: Docker (Recommended)

Run all projects at once using Docker:

```bash
# Build and start all services
make up-build

# Or using docker-compose directly
docker compose up -d --build
```

| Service | URL | Description |
|---|---|---|
| Call Log Analysis | [localhost:8501](http://localhost:8501) | Call log dashboard |
| COVID-19 Analysis | [localhost:8502](http://localhost:8502) | COVID-19 dashboard |
| Bank Deposit Analysis | [localhost:8503](http://localhost:8503) | Bank deposit rates |
| Jupyter Notebooks | [localhost:8888](http://localhost:8888) | All notebooks |

```bash
# Stop all services
make down

# View logs
make logs

# Check service health
make status
```

### Option 2: Run individually

Each Streamlit app has its own `requirements.txt`. For example, to run the Call Log Analysis dashboard:

```bash
cd Streamlit/CallLogAnalysis
pip install -r requirements.txt
streamlit run app.py
```

### Option 3: Jupyter notebooks

```bash
pip install -r requirements.txt
jupyter notebook
```

Then navigate to any `.ipynb` file in the project directories.

---

## License

This project is open source. See the repository for license details.

---

## Links

| Resource | URL |
|---|---|
| GitHub Repository | [github.com/Mazhar004/python-data-visualization](https://github.com/Mazhar004/python-data-visualization) |
| GitHub Pages | [mazhar004.github.io/python-data-visualization](https://mazhar004.github.io/python-data-visualization/) |
| COVID-19 Dashboard | [visualcovid.streamlit.app](https://visualcovid.streamlit.app/) |
| Call Log Dashboard | [calllog.streamlit.app](https://calllog.streamlit.app/) |
| Bank Analysis Dashboard | [bdbankanalysis.streamlit.app](https://bdbankanalysis.streamlit.app/) |
