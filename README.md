# 🐄 XAI-Based Breed Recognition for Indian Cattle

A deep learning-based system for fine-grained classification of 34 Indian cattle breeds using a hybrid architecture combining EfficientNet and Vision Transformer (ViT), enhanced with Explainable AI (Grad-CAM) for interpretability.

---

## 📌 Overview

This project solves a **fine-grained image classification problem** in the agriculture domain. It identifies Indian cattle breeds from images by integrating object detection, deep learning, and explainable AI.

---

## 🚀 Key Features

* End-to-end **deep learning pipeline**
* YOLOv8-based cattle detection and ROI extraction
* Hybrid architecture: EfficientNet + Vision Transformer (ViT)
* Data augmentation for class balancing
* Explainable AI using Grad-CAM
* Achieved **>90% validation accuracy**

---

## 🧠 Model Architecture

* **Backbone:** EfficientNet-B3 (feature extraction)
* **Transformer:** Vision Transformer (ViT) for global context
* **Explainability:** Grad-CAM for visual insights

---

## 🔄 Pipeline Workflow

Input Image
↓
YOLOv8 Detection
↓
ROI Cropping
↓
Image Preprocessing
↓
Hybrid Model (EfficientNet + ViT)
↓
Prediction (Breed Class)
↓
Grad-CAM Visualization

---

## 📂 Dataset

* ~15,000 images across 34 Indian cattle breeds
* Balanced using augmentation techniques
* Dataset not included due to size (available on request)

---

## 🛠️ Tech Stack

* Python
* PyTorch
* YOLOv8 (Ultralytics)
* EfficientNet
* Vision Transformer (ViT)
* Grad-CAM
* OpenCV

---

## 📊 Results

* Validation Accuracy: **>90%**
* Improved classification using ROI-based preprocessing
* Grad-CAM highlights meaningful regions influencing predictions

---

## 📸 Sample Outputs

> Add images here:

* Original Image
* Cropped ROI
* Prediction Output
* Grad-CAM Heatmap

---

## Project Structure
XAI-Cattle-Breed-Recognition/
│
├── notebooks/
│   └── cattle_breed_recognition.ipynb 
│
├── outputs/       
├── README.md
├── requirements.txt
└── .gitignore

---

## 👨‍💻 Author

* Group Project
* **Primary Contributor:** P Mukeswara Reddy (Led full pipeline development and implementation)

---

## 📌 Future Improvements

* Web app deployment (Streamlit/Flask)
* Real-time inference optimization
* Expand dataset with additional breeds

---

## ⭐ If you like this project, give it a star!
