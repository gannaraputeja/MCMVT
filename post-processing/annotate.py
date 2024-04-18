from PIL import Image, ImageDraw, ImageFont
import os
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(description='Draw bounding boxes on images.')
parser.add_argument('base_folder', type=str, help='Base folder path up to the test dataset.')
parser.add_argument('test_dataset', type=str, help='Test dataset name, e.g., S06.')
parser.add_argument('camera_id', type=str, help='Camera ID to filter the bounding boxes, e.g., c046.')
parser.add_argument('file_path', type=str, help='Path to the track1.txt file.')

args = parser.parse_args()

# Construct input and output folder paths based on arguments
input_folder = os.path.join(args.base_folder, args.test_dataset, args.camera_id, 'img1')
output_folder = os.path.join(args.base_folder, args.test_dataset, args.camera_id, 'output')

# Ensure the output directory exists
os.makedirs(output_folder, exist_ok=True)

# Function to draw bounding box on image
def draw_bounding_box(draw, xmin, ymin, width, height, object_id):
    xmax = xmin + width
    ymax = ymin + height
    draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=2)
    font = ImageFont.load_default()
    offset = 15  # Adjust offset as needed
    draw.text((xmin, ymin - offset), f"Object ID: {object_id}", fill="red", font=font)

# Read data from the text file
bounding_boxes = {}
with open(args.file_path, 'r') as file:
    for line in file:
        cam_id, obj_id, frame_id, xmin, ymin, width, height, xworld, yworld = map(int, line.split())
        if cam_id == int(args.camera_id.strip('c')):
            if frame_id not in bounding_boxes:
                bounding_boxes[frame_id] = []
            bounding_boxes[frame_id].append((xmin, ymin, width, height, obj_id))

# Iterate over all images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg"):
        image_path = os.path.join(input_folder, filename)
        frame_id = int(filename.split('_')[1].split('.')[0])  # Assumes filenames like img_000001.jpg

        image = Image.open(image_path)
        draw = ImageDraw.Draw(image)

        # Draw bounding boxes on the image if the frame_id exists in the bounding_boxes dictionary
        if frame_id in bounding_boxes:
            for bbox in bounding_boxes[frame_id]:
                draw_bounding_box(draw, *bbox)

        # Save the image with bounding boxes to the output folder
        output_path = os.path.join(output_folder, filename)
        image.save(output_path)
        print(f"Bounding boxes drawn on {image_path} and saved as {output_path}")
