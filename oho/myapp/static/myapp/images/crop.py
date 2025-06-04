from PIL import Image
import os

# Folder containing images including BC.jpg
folder_path = '/home/arshathad/Desktop/Django/oho/myapp/static/myapp/images/random-index'
output_folder = '/home/arshathad/Desktop/Django/oho/myapp/static/myapp/images/cropped-images'
reference_image_name = 'BC.jpg'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get dimensions from the reference image
ref_path = os.path.join(folder_path, reference_image_name)
with Image.open(ref_path) as ref_img:
    target_width, target_height = ref_img.size

# Crop all images in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')) and filename != reference_image_name:
        img_path = os.path.join(folder_path, filename)
        with Image.open(img_path) as img:
            img_width, img_height = img.size

            # Calculate crop coordinates
            left = max((img_width - target_width) // 2, 0)
            top = max((img_height - target_height) // 2, 0)
            right = left + target_width
            bottom = top + target_height

            # Crop and save
            cropped = img.crop((left, top, right, bottom))
            cropped.save(os.path.join(output_folder, filename))

print("✅ All images cropped to BC.jpg's size!")
