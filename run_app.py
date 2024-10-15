import cv2
from ultralytics import YOLO


video_path = 'video.mp4'
output_path = 'output_video.mp4'

model = YOLO('best.pt')

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Video dosyası açılamadı!")
    exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

person_class_id = 3

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    filtered_boxes = []
    for box in results[0].boxes:
        if int(box.cls[0]) != person_class_id:
            filtered_boxes.append(box)

    if filtered_boxes:
        result_img = results[0].plot(filtered_boxes)
        out.write(result_img)

cap.release()
out.release()

print(f"Tespit edilen video '{output_path}' olarak kaydedildi.")
