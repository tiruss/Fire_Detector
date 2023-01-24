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
```bash
python train.py
```

## 5. Test Trained Network
* Run test.py
```bash
python test.py
```