# KUET Student Gender Ratio

A data visualization project that scrapes real-time student enrollment data from the official KUET (Khulna University of Engineering and Technology) web portal and visualizes the male-to-female student ratio across all departments.

## Features

- Scrapes live student data from the official KUET website using BeautifulSoup
- Caches scraped data locally as CSV for offline use
- Generates two types of bar chart visualizations:
  - **Department-wise breakdown** -- stacked bar chart showing the percentage of male and female students in each department
  - **University-wide distribution** -- bar chart showing how female students are distributed across departments
- Automatic labeling with percentage values and timestamps from the data source

## Sample Output

**Department-wise Gender Percentage**

![Percentage of Boys and Girls Department wise in KUET](images/Percentage%20of%20Boys%20&%20Girls%20Department%20wise%20in%20KUET%20(27%20October%202019).png)

**Female Student Distribution Across Departments**

![Girls in KUET](images/Girls%20in%20KUET%20(27%20October%202019).png)

## Tech Stack

- **Python 3**
- **requests** -- HTTP requests for web scraping
- **BeautifulSoup4** -- HTML parsing and data extraction
- **pandas** -- data manipulation and CSV handling
- **matplotlib** -- chart generation

## How to Run

1. Install dependencies:

   ```bash
   pip install requests beautifulsoup4 pandas matplotlib
   ```

2. Open and run the Jupyter notebook:

   ```bash
   jupyter notebook "Kuet Student Gender Ratio.ipynb"
   ```

   The notebook will attempt to fetch live data from the KUET portal. If the request fails, it falls back to the cached CSV in the `data/` directory.

## Project Structure

```
KuetStudentGenderRatio/
  Kuet Student Gender Ratio.ipynb   # Main notebook
  README.md
  data/
    Last Updated.csv                # Cached student data
  images/
    Girls in KUET (27 October 2019).png
    Percentage of Boys & Girls Department wise in KUET (27 October 2019).png
```

## Data Source

Student data is publicly available from the [KUET official portal](http://www.kuet.ac.bd/).
