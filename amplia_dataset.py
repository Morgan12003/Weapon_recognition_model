import cv2
import os
import numpy as np
import random

def adjust_brightness_contrast(image, alpha=1.0, beta=0):
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, matrix, (w, h))

def flip_image(image, flip_code):
    return cv2.flip(image, flip_code)

def add_blur(image, ksize=5):
    return cv2.GaussianBlur(image, (ksize, ksize), 0)

def scale_image(image, scale):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    return cv2.resize(image, (width, height))

def augment_image(image):
    transformations = []
    if random.choice([True, False]):
        angle = random.randint(-30, 30)
        transformations.append(f"Rotated {angle} degrees")
        image = rotate_image(image, angle)
    if random.choice([True, False]):
        alpha = random.uniform(0.7, 1.3)
        beta = random.randint(-50, 50)
        transformations.append(f"Brightness/Contrast ({alpha}, {beta})")
        image = adjust_brightness_contrast(image, alpha, beta)
    if random.choice([True, False]):
        flip_code = random.choice([-1, 0, 1])
        transformations.append(f"Flipped {flip_code}")
        image = flip_image(image, flip_code)
    if random.choice([True, False]):
        ksize = random.choice([3, 5, 7])
        transformations.append(f"Blurred with ksize {ksize}")
        image = add_blur(image, ksize)
    if random.choice([True, False]):
        scale = random.uniform(0.8, 1.2)
        transformations.append(f"Scaled {scale}")
        image = scale_image(image, scale)
    return image, transformations

def augment_dataset(input_folder, output_folder, num_copies=5):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            image = cv2.imread(image_path)
            
            # Save original image
            original_path = os.path.join(output_folder, filename)
            cv2.imwrite(original_path, image)
            print(f"Saved original {filename}")
            
            for i in range(num_copies):
                augmented_image, transformations = augment_image(image.copy())
                new_filename = f"{os.path.splitext(filename)[0]}_aug{i}.jpg"
                cv2.imwrite(os.path.join(output_folder, new_filename), augmented_image)
                print(f"Saved {new_filename} with {transformations}")

if __name__ == "__main__":
    input_folder = "weapon/pistol"
    output_folder = "weapon/pistol_augmented"
    augment_dataset(input_folder, output_folder, num_copies=5)