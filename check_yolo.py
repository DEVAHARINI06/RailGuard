from ultralytics import YOLO

model = YOLO("models/best.pt")

print("YOLO Classes:")
print(model.names)