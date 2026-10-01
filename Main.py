from PIL import Image
import os

def resize(input, output, size=(800, 800)):
    """
    Resize all supported images in the input directory and save them to the output directory.

    Args:
        input (str): Path to the folder containing original images.
        output (str): Path to the folder where resized images will be saved.
        size (tuple): Target size as (width, height). Defaults to (800, 800).
    """

    # Create the output directory if it does not already exist
    if not os.path.exists(output):
        os.makedirs(output)
        print(f"Created output folder: {output}")

    # Iterate through every file in the input directory
    for filename in os.listdir(input):

        # Only process common image formats
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            input_path = os.path.join(input, filename)
            output_path = os.path.join(output, filename)

            try:
                # Open the image, resize it using high-quality LANCZOS resampling, and save
                with Image.open(input_path) as img:
                    resized_image = img.resize(size, Image.Resampling.LANCZOS)
                    resized_image.save(output_path)
                    print(f"[+] Resized and saved: {filename}")

            except Exception as e:
                # Catch and report any errors that occur while processing an individual image
                print(f"[-] Error processing {filename}: {e}")


if __name__ == "__main__":
    # Define source and destination folders
    input = 'original_images'
    output = 'resized_images'

    print("Starting....")
    resize(input, output)
    print('Done')
