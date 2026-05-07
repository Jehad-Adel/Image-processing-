# Coin Counter using Image Processing

A Python tool that uses OpenCV to detect and count coins in an image.

## How it works:
1. **Grayscale Conversion**: Simplifies the image data.
2. **Gaussian Blur**: Reduces high-frequency noise.
3. **Canny Edge Detection**: Highlights the boundaries of the coins.
4. **Contour Detection**: Identifies closed shapes and counts them.

## Usage:
1. Install dependencies: `pip install -r requirements.txt`
2. Place your image in `images/input/`
3. Run: `python main.py`
  
