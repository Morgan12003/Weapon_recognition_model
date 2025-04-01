#programma che scarica immagini da internet
from bing_image_downloader import downloader

downloader.download("rifles", limit=500, output_dir="weapon", adult_filter_off=True, force_replace=False, timeout=60)
