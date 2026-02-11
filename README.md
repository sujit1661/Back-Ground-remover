# Background Remover

A simple Python script that removes the background from any image using the rembg library.

## Requirements

- Python 3.7+
- rembg
- Pillow

## Installation

1. Clone this repository:

   git clone https://github.com/yourusername/background-remover.git
   cd background-remover

2. Install the required dependencies:

   pip install rembg pillow

## Usage

1. Run the script:

   python main.py

2. Enter the path to your image when prompted:

   Enter the image file path: photo.jpg

3. The output image with background removed will be saved
   in the same directory with _no_bg.png appended to the name.

## Example

Input:  photo.jpg
Output: photo_no_bg.png

$ python main.py
Enter the image file path: photo.jpg
Background removed successfully!
Image saved as: photo_no_bg.png

## Supported Formats

- JPG / JPEG
- PNG
- BMP
- WEBP

## License

This project is licensed under the MIT License.
