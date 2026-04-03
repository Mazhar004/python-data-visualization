# Progress Bar

A simple terminal progress bar implementation in Python that displays a loading animation with percentage status using Unicode block characters.

## Features

- Animated progress bar rendered in the terminal using Unicode characters
- Accepts a `value` and `maximum` parameter, automatically rescales to percentage
- Displays real-time loading status (e.g., "20% Loading" or "20% Loaded")
- Available as both a standalone Python script and a Jupyter notebook

## Sample Output

![Progress Bar](images/progress%20bar.png)

## Tech Stack

- **Python 3**
- **time** (standard library) -- used for the animation delay between increments

## How to Run

### As a Python script

```bash
python progress_bar.py
```

When prompted, enter the value and maximum separated by a space:

```
Input value & maximum = 40 200
```

This will display a progress bar filling up to 20% (40 out of 200).

### As a Jupyter notebook

```bash
jupyter notebook "Progress Bar Printing.ipynb"
```

Run all cells and enter the value and maximum when prompted.

## Project Structure

```
ProgressBar/
  progress_bar.py                 # Standalone script
  Progress Bar Printing.ipynb     # Jupyter notebook version
  README.md
  images/
    progress bar.png
```
