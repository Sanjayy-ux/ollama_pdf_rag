from pdf2image import convert_from_path

# Replace 'sample.pdf' with the path to your PDF file
images = convert_from_path('sample.pdf')

# Print number of pages converted to images
print(f"Number of pages converted: {len(images)}")
