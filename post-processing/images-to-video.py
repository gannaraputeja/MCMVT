import cv2
import os
import argparse

def images_to_video(image_folder, video_name, fps=12):
    # Get all image files from the folder
    images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
    images.sort()  # Sort the images by name

    # Check if images list is empty
    if not images:
        print("No images found in the folder.")
        return

    # Print the images found
    print(f"Found images: {images}")

    # Retrieve the dimensions of the first image
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    if frame is None:
        print(f"Failed to read the first image at {first_image_path}")
        return

    height, width, layers = frame.shape
    print(f"Image dimensions (Width x Height): {width} x {height}")

    # Define the codec and create VideoWriter object
    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # Check if video writer has been successfully initialized
    if not video.isOpened():
        print("Could not open the video for writing.")
        return

    # Add images to the video
    for image in images:
        img_path = os.path.join(image_folder, image)
        img = cv2.imread(img_path)
        if img is None:
            print(f"Failed to read image {img_path}")
            continue
        video.write(img)

    # Release the video writer handler
    video.release()
    print("Video processing complete.")

def main():
    parser = argparse.ArgumentParser(description="Convert a folder of images into a video.")
    parser.add_argument("image_folder", type=str, help="Path to the folder containing images.")
    parser.add_argument("video_name", type=str, help="Output video file path.")

    args = parser.parse_args()

    # Call the function with arguments
    images_to_video(args.image_folder, args.video_name)

if __name__ == "__main__":
    main()
