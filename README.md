# Image Resizer

A simple Python script to batch-resize images (JPG, JPEG, PNG) using the Pillow library.

## Features

- Resizes all supported images in a folder
- Creates the output folder automatically if it doesn't exist
- Uses high-quality LANCZOS resampling
- Default size: 800 × 800 pixels

## Requirements

- Python 3.x
- Pillow

Install Pillow with:

```bash
pip install Pillow
```

## Usage

1. Place your original images in a folder named `original_images` (or change the path in the script).
2. Run the script:

```bash
python Main.py
```

3. Resized images will be saved in the `resized_images` folder.

### Customization

You can modify the input/output folders and target size in `Main.py`:

```python
input = 'original_images'
output = 'resized_images'
resize(input, output, size=(800, 800))  # Change size as needed
```

## License

This project is open source and available for personal or educational use.
