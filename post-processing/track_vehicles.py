def get_object_detection_info(filepath, object_id):
    detection_info = []
    with open(filepath, 'r') as file:
        for line in file:
            data = line.split()
            if len(data) == 9:
                current_object_id = int(data[1])
                if current_object_id == object_id:
                    camera_id = int(data[0])
                    frame_id = int(data[2])
                    detection_info.append((camera_id, frame_id))
    return detection_info

# Example usage
filepath = 'track1.txt'  # Replace 'track1.txt' with the path to your file
object_id = 2  # Replace 123 with the desired object ID
object_detection_info = get_object_detection_info(filepath, object_id)
if object_detection_info:
    print(f"Object {object_id} detected in the following cameras and frames:")
    for camera_id, frame_id in object_detection_info:
        print(f"Camera ID: {camera_id}, Frame ID: {frame_id}")
else:
    print(f"No detection information found for object {object_id}.")

