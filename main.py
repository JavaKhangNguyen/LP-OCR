import os
import subprocess

HOME = os.getcwd() 
print(HOME)
os.chdir(HOME)

"""## Train model"""
subprocess.run(['yolo','task=detect', 'mode=train', 'model=Model/yolov10b.pt','data=home/ldtan/ldtan/LP-OCR/data.yaml','epochs=300', 'batch=16', 'imgsz=640', 'save=True', 'save_period=10'])

"""## Validating model"""

os.chdir(HOME)

with open('valid.txt', 'w') as f:
    result = subprocess.run(['yolo', 'task=detect', 'mode=val', 'model=runs/detect/train/weights/best.pt', 'imgsz=640', 'data=home/ldtan/ldtan/LP-OCR/data.yaml'], capture_output=True, text=True)
    f.write(result.stdout)
    f.write(result.stderr)
