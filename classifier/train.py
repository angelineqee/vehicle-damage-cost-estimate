from ultralytics import YOLO
# import torch
# torch.cuda.set_device(0)
# print("device count",torch.cuda.device_count())
# print(torch.cuda.get_device_name(0))
# print(torch.cuda.is_available())  # Should return True
# print(torch.version.cuda)   

if __name__ ==  '__main__':
    model = YOLO("yolov8s.pt")
    results = model.train(data="data.yaml", epochs=100, batch=32, patience=20)
