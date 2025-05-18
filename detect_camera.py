import torch
import cv2
import time

# YOLOv5 modelini yükle
model = torch.hub.load('yolov5', 'custom', path='yolov5/runs/train/exp2/weights/best.pt', source='local')

# Kamera başlat (0: laptop kamerası, 1: harici kamera olabilir)
cap = cv2.VideoCapture(0)

# Kamera çözünürlüğünü ayarla
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Kamera çalışıyor mu kontrolü
if not cap.isOpened():
    print("Kamera açılamadı!")
    exit()

print("Kedi tespiti başlatıldı. 'q' ile çık.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Görüntü alınamadı!")
        break

    # YOLOv5 ile tahmin yap
    results = model(frame)

    # Tahmin sonuçlarını görselleştir
    results.render()  # Sonuçları çizer

    # Görüntüyü göster
    cv2.imshow('Kedi Tespiti', results.ims[0])

    # q tuşuna basılırsa çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Temizle
cap.release()
cv2.destroyAllWindows()
