# **Weapon Recognition Model**

**EN:**  
Weapon recognition model for a personal project based on **YOLOv8** and a **Python toolkit** to manage, apply, and label collected images.

**IT:**  
Modello di riconoscimento armi per progetto personale basato su **YOLOv8** e un **toolkit scritto in Python** per gestire, ampliare ed etichettare le immagini raccolte.

---

## 👥 **Contributors**

**EN:**
This project was developed collaboratively by a small team, with contributions in software development, dataset management, and documentation:

**IT:**
Questo progetto è stato realizzato in collaborazione da un piccolo team, con contributi in sviluppo software, gestione dataset e documentazione:

- **Morgan Scollo** – Project Lead & Developer (`@Morgan12003`)
- **Manfredi Coppola** – Developer Facial recognition and geolocation (`@manfredicoppola`)
- **Nicolò Di Marco** – Developer Alert system and text to speech
- **Matteo Fraello** – Developer Virtual drone

---

## 📌 **Elenco Utilizzo Toolkit Python**

- **`amplia_dataset`**: Prende una cartella contenente immagini in ingresso e ne crea una nuova con le immagini originali + 5 (numero variabile) modificate. Le modifiche consistono nella **rotazione delle immagini** e nella **variazione della luminosità**.
- **`estrai_frame`**: Questo programma prende in ingresso un video in formato **`.mp4`**, crea (se non esiste) una cartella **"frames"** e vi inserisce al suo interno tutti i **frame catturati dal video** (con la possibilità di specificare quanti frame catturare).
- **`etichette_automatiche`**: Permette di **etichettare automaticamente** le immagini già ritagliate e normalizzate.
- **`scarica_immagini`**: Questo programma **cerca immagini online** utilizzando una chiave di ricerca e le scarica automaticamente sul computer.
- **`verifica_img`**: Controlla le **dimensioni delle immagini**, ridimensionandole a **640px**, e verifica la **presenza dell'etichetta corrispondente** per ogni immagine. Se l'etichetta è assente, ne inserisce una normalizzata.

---

## 📁 **Organizzazione delle cartelle**

