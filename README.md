
# Image to PDF Catalog Creator

## Description
A Python script that converts a folder of images into a neatly arranged PDF catalog. Each page of the PDF contains a 2x2 grid of images, resized and positioned to maintain their aspect ratios. This tool is ideal for creating visual portfolios, product catalogs, or any document requiring a structured image layout.

## Features
- Converts multiple images into a single PDF file.
- Arranges images in a 2x2 grid per page.
- Maintains image aspect ratios.
- User-friendly prompts for specifying input and output paths.

## Requirements
- Python 3.x
- Pillow (PIL Fork)
- ReportLab

## Installation
Ensure Python 3.x is installed on your system.
Install required packages using pip:
```
pip install Pillow reportlab
```

## Usage
1. Save the script to a local file, e.g., `image_to_pdf.py`.
2. Run the script from a terminal or command prompt:
```
python image_to_pdf.py
```
3. Follow the prompts to enter the path to your images folder and the desired output PDF file path.
