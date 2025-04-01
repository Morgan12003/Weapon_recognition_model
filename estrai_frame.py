import os
import cv2
from datetime import timedelta

def extract_frames_every_025s(video_path, output_folder='frames'):
    """
    Estrae un frame ogni 0.25 secondi dal video.
    :param video_path: percorso del video MP4
    :param output_folder: cartella di output per i frame
    """
    if not os.path.exists(video_path):
        print(f"ERRORE: File video {video_path} non trovato!")
        return
    
    os.makedirs(output_folder, exist_ok=True)
    
    # Ottieni il nome del file senza estensione
    video_name = os.path.basename(video_path)
    if video_name.lower().endswith('.mp4'):
        video_name = video_name[:-4]
    
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("ERRORE: Impossibile aprire il video")
        return
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps
    frame_interval = int(fps * 0.1)  # Calcola ogni quanti frame estrarre (0.1 secondi)
    
    print(f"Video: {video_path}")
    print(f"FPS: {fps:.2f}")
    print(f"Durata: {timedelta(seconds=duration)}")
    print(f"Frame totali: {total_frames}")
    print("Estraendo un frame ogni 0.25 secondi...")
    
    frame_count = 0
    saved_count = 0
    
    while cap.isOpened():
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count)
        ret, frame = cap.read()
        if not ret:
            break
        
        # Crea il nome del file con il nome del video e il numero del frame
        output_file = os.path.join(output_folder, f"{video_name}_frame{frame_count:06d}.jpg")
        cv2.imwrite(output_file, frame)
        saved_count += 1
        
        if saved_count % 10 == 0:
            time_in_seconds = frame_count / fps
            time_str = str(timedelta(seconds=time_in_seconds)).replace(':', '-').split('.')[0]
            print(f"Salvato frame {saved_count} ({output_file}) al tempo {time_str}")
        
        frame_count += frame_interval
    
    cap.release()
    print(f"\nEstrazione completata!")
    print(f"Frame totali nel video: {total_frames}")
    print(f"Frame salvati: {saved_count}")
    print(f"Cartella di output: {os.path.abspath(output_folder)}")

if __name__ == "__main__":
    video_path = input("Inserisci il percorso del video MP4: ").strip('"')
    extract_frames_every_025s(video_path)