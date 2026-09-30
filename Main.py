from PIL import Image
import os

def resize(input,output,size=(800,800)):

    if not os.path.exists(output):
        os.makedirs(output)
        print(f"Created output folder: {output}")

    for filename in os.listdir(input):

        if filename.lower().endswith(".jpg",".png",".jpeg"):
            input_path=os.path.join(input,filename)
            output_path=os.path.join(output,filename)

        try:
            with Image.open (input_path) as img:
                resized_image=img.resize(size,Image.Resampling.LANCZOS)
                resized_image.save(output_path)
                print(f"[+] Resized and saved: {filename}")
                
        except Exception as e:
            print(f"[-] Error processing {filename}: {e}")

if __name__=="__main__":
    input='original_images'
    output='resized_images'
    print("Starting....")
    resize(input,output)
    print('Done')
