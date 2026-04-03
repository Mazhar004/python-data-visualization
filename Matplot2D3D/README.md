# Matplotlib 2D and 3D Plots

A collection of mathematical visualizations built with matplotlib, demonstrating 2D parametric curves, 3D scatter plots, and polar coordinate patterns.

## Features

- **Heart Shape** -- parametric heart curve rendered with alternating red and indigo layered lines
- **Normal Distribution (3D)** -- 3D scatter plot of a bivariate normal distribution using randomly generated data
- **Prime Number Pattern** -- polar coordinate plot comparing the visual pattern of all integers against prime numbers only
- **Random Sine Curves** -- overlapping sine waves with randomized amplitudes and color cycling

## Sample Output

![Heart](images/Heart.png)

![Normal Distribution](images/Normal%20Distribution.png)

![Prime Number Pattern](images/Prime%20Number%20Pattern.png)

![Random Sine](images/Random%20Sine.png)

## Tech Stack

- **Python 3**
- **numpy** -- mathematical functions and data generation
- **matplotlib** -- 2D and 3D plotting (including `mpl_toolkits.mplot3d`)

## How to Run

1. Install dependencies:

   ```bash
   pip install numpy matplotlib
   ```

2. Open any of the notebooks:

   ```bash
   jupyter notebook "Heart.ipynb"
   jupyter notebook "Normal distribution in 3d.ipynb"
   jupyter notebook "Prime Shape.ipynb"
   jupyter notebook "Random Sine Curve.ipynb"
   ```

3. Run all cells to generate the visualizations.

## Project Structure

```
Matplot2D3D/
  Heart.ipynb                      # Parametric heart curve
  Normal distribution in 3d.ipynb  # 3D normal distribution scatter
  Prime Shape.ipynb                # Prime vs all-number polar patterns
  Random Sine Curve.ipynb          # Layered random sine waves
  README.md
  images/
    Heart.png
    Normal Distribution.png
    Prime Number Pattern.png
    Random Sine.png
```
