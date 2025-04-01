import os
import cv2

def create_yolo_labels(image_folder, label_folder, class_id=0):
    if not os.path.exists(label_folder):
        os.makedirs(label_folder)
    
    for filename in os.listdir(image_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, filename)
            image = cv2.imread(image_path)
            h, w, _ = image.shape
            
            # YOLO format: class_id, x_center, y_center, width, height (normalizzato)
            label_data = f"{class_id} 0.5 0.5 0.99 0.99"
            
            label_filename = os.path.splitext(filename)[0] + ".txt"
            label_path = os.path.join(label_folder, label_filename)
            
            with open(label_path, "w") as label_file:
                label_file.write(label_data)
            
            print(f"Label creata: {label_filename}")

if __name__ == "__main__":
    datasets = [
        ("dataset/train/images", "dataset/train/labels"),
        ("dataset/val/images", "dataset/val/labels")
    ]
    
    for image_folder, label_folder in datasets:
        create_yolo_labels(image_folder, label_folder)
