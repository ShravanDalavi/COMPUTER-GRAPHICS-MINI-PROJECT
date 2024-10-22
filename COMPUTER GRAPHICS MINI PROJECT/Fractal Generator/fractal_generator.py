import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    """Computes the number of iterations before the escape for a given complex number."""
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
    """Generates the fractal image for the Mandelbrot set."""
    # Create an array to hold the pixel data
    image = np.zeros((height, width))

    for i, y in enumerate(np.linspace(ymin, ymax, height)):
        for j, x in enumerate(np.linspace(xmin, xmax, width)):
            # Convert pixel coordinate to complex number
            c = complex(x, y)
            # Compute the number of iterations
            m = mandelbrot(c, max_iter)
            # Set the color based on the number of iterations
            image[i, j] = m

    return image

def plot_fractal(image):
    """Displays the fractal image."""
    plt.imshow(image, cmap='hot', extent=(-2, 2, -2, 2))
    plt.colorbar()
    plt.title("Mandelbrot Set")
    plt.show()

# Parameters for the fractal generation
xmin, xmax, ymin, ymax = -2.0, 2.0, -2.0, 2.0
width, height = 800, 800
max_iter = 100

# Generate and plot the fractal
fractal_image = generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter)
plot_fractal(fractal_image)
