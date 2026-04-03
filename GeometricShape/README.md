# Geometric Shapes in Python

A collection of programs that render geometric shapes in two ways: ASCII art printed to the terminal and graphical plots drawn with matplotlib.

## Features

### Command-Line ASCII Shapes (Shape.ipynb)

Prints shapes to the console using `*` characters. Each function takes a parameter `n` controlling the number of lines:

- Triangle
- Right Triangle
- Square
- Rectangle
- Crown

### Graphical Plots (Advanced Shape.ipynb)

Draws shapes on a matplotlib coordinate plane with configurable dimensions and positions:

- Rectangle -- defined by width, height, and bottom-left corner
- Circle -- defined by radius and center coordinates

## Sample Output

**Crown (n=5)**

![Crown](images/Crown.png)

## Tech Stack

- **Python 3**
- **numpy** -- coordinate computation for graphical shapes
- **matplotlib** -- plotting for advanced shapes

## How to Run

1. Install dependencies:

   ```bash
   pip install numpy matplotlib
   ```

2. Open either notebook:

   ```bash
   jupyter notebook "Shape.ipynb"              # ASCII art shapes
   jupyter notebook "Advanced Shape.ipynb"      # Graphical plot shapes
   ```

3. Run all cells. For the ASCII shapes, adjust the `n` parameter passed to each function to change the size.

## Project Structure

```
GeometricShape/
  Shape.ipynb            # ASCII art shapes (triangle, square, crown, etc.)
  Advanced Shape.ipynb   # Matplotlib-drawn rectangle and circle
  README.md
  images/
    Crown.png
```
