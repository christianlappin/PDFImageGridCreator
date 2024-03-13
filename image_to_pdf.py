
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from PIL import Image

def add_image_to_pdf(pdf, image_path, x, y, max_width, max_height):
    """Resize and add an image to the PDF at the specified position."""
    img = Image.open(image_path)
    img_width, img_height = img.size
    aspect_ratio = img_width / img_height

    # Calculate the new size to maintain aspect ratio
    scaled_width = min(max_width, img_width / 96, key=lambda x: abs(x - img_width / 96))
    scaled_height = scaled_width / aspect_ratio

    if scaled_height > max_height:
        scaled_height = max_height
        scaled_width = scaled_height * aspect_ratio

    # Adjust position to place images from top left corner
    pdf.drawInlineImage(image_path, x, y - scaled_height, width=scaled_width, height=scaled_height)

def create_pdf_catalog(images_folder, output_pdf):
    pdf = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter  # Default Letter size (8.5 x 11 inches)

    max_image_width = width / 2 - inch / 2  # Allow for some padding
    max_image_height = height / 2 - inch / 2

    images = [os.path.join(images_folder, img) for img in os.listdir(images_folder) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]

    for i, image_path in enumerate(images):
        if i % 4 == 0 and i != 0:
            pdf.showPage()  # Start a new page

        # Calculate position for each image
        x_position = inch / 4 + (i % 2) * (max_image_width + inch / 2)
        y_position = height - inch / 4 - ((i % 4) // 2) * (max_image_height + inch / 2)

        add_image_to_pdf(pdf, image_path, x_position, y_position, max_image_width, max_image_height)

    pdf.save()

if __name__ == "__main__":
    images_folder = input("Enter the path to your images folder: ").strip()
    output_pdf = input("Enter the desired output PDF file path and name: ").strip()

    create_pdf_catalog(images_folder, output_pdf)
    print("PDF catalog created successfully!")
