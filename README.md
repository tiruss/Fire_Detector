# YOLOv5 based Simple Fire Detector

## 1. Clone the Code

* Create anaconda environment
```
conda create -n fire_detector python=3.8
conda activate fire_detector
```
* Clone the code
```bash
git clone https://github.com/tiruss/Fire_Detector.git
cd Fire_Detector
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
pip install pytube # for downloading youtube video
```

## 2. Download Dataset

* Download Fire Dataset [[Download]](https://drive.google.com/drive/folders/15fuHCUKZIUmEXrBdnE-E8W3DHREoDI5e?usp=share_link)

## 3. Convert XML format to TEXT format

* Run xml2yolo_text.py
```bash
python xml2yolo_text.py
```

## 4. Train the YOLOv5 Model
* Run train.py with proper dataset path 
* You can change the hyperparameters in train.py [[YOLOv5]](https://github.com/ultralytics/yolov5)
```bash
python train.py --data fire.yaml --cfg yolov5s.yaml --weights '' --batch-size 16 --epochs 100
```
* Track your training process on the tensorboard
```bash
tensorboard --logdir runs/train
```

## 5. Test Trained Network
* Download youtube video
```
python youtube_download.py
```
* Run detect.py
```bash
python detect.py --source [YOUR VIDEO] --weights [YOUR WEIGHT] --conf 0.4
```