import cv2
import os
import glob
from PIL import Image

def resize_and_create_label(image_path, label_path, target_size=(640, 640)):
    """Ridimensiona l'immagine e crea un file di etichetta se manca."""
    
    # Ridimensiona l'immagine
    img = cv2.imread(image_path)
    if img is None:
        print(f"Errore nel leggere {image_path}")
        return
    
    original_height, original_width = img.shape[:2]
    
    # Se l'immagine non è già della dimensione target, la ridimensiona
    if (original_width, original_height) != target_size:
        resized_img = cv2.resize(img, target_size, interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(image_path, resized_img)  # Sovrascrive l'immagine ridimensionata
        print(f"✅ Immagine ridimensionata: {image_path}")
    
    # Creazione della label se manca
    if not os.path.exists(label_path):
        # Calcola le coordinate della bounding box (normalizzate)
        x_center = 0.5
        y_center = 0.5
        width = 0.99
        height = 0.99
        
        with open(label_path, 'w') as f:
            f.write(f"0 {x_center} {y_center} {width} {height}\n")
        
        print(f"Creata label per {image_path} con bounding box completa (classe 0)")

def check_and_resize_images(dataset_path, target_size=(640, 640)):
    """Controlla e ridimensiona le immagini nel dataset."""
    
    folders = ["train", "val"]
    
    for folder in folders:
        images_path = os.path.join(dataset_path, folder, "images")
        labels_path = os.path.join(dataset_path, folder, "labels")
        
        # Controlla tutte le immagini nella cartella
        for img_name in os.listdir(images_path):
            img_path = os.path.join(images_path, img_name)
            label_path = os.path.join(labels_path, os.path.splitext(img_name)[0] + ".txt")
            
            # Verifica se il file esiste e gestisce il ridimensionamento + creazione label
            resize_and_create_label(img_path, label_path, target_size)

    print("Controllo e ridimensionamento completato per tutte le immagini!")

# Percorso principale del dataset
dataset_path = "C:/Users/morga/OneDrive/Desktop/MODELLO MIO/dataset"

# Controlla e ridimensiona tutte le immagini
check_and_resize_images(dataset_path)
