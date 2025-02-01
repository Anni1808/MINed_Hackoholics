# 🔥 Malware Detection Using Machine Learning  

## 📌 Project Overview  
Malware is a growing threat in the cybersecurity landscape, making **automated malware detection** an essential task. This project presents a **machine learning-based malware classification system** that efficiently identifies malware types using extracted features from API function calls, DLL imports, and portable executable (PE) headers.  

Our approach utilizes **feature selection techniques** to refine dataset quality, applies multiple **classification models**, and achieves a **best accuracy of 97.52%** using **Support Vector Machine (SVM)**.  

---

## 🚀 Features & Workflow  

### 🔹 Feature Selection & Extraction  
The dataset is divided into three major feature groups:  
- **API Functions** → Logs API calls made by the malware  
- **DLL Imports** → Tracks imported DLLs for each malware type  
- **Portable Executable (PE) Features** → Extracts metadata from PE headers  

#### 🏆 Techniques Used:  
✔ **AdaBoost** → Applied separately to `DLLs_Imported.csv` & `portable_executable.csv`  
✔ **LightGBM** → Applied to `API_Functions.csv` for fast & scalable classification  
✔ **SHAP (SHapley Additive exPlanations)** → Determines feature importance  
✔ **Recursive Feature Elimination (RFE)** → Used for dimensionality reduction in API function analysis  

After feature extraction, all three datasets are **combined into a unified dataset** for model training.  

---

### 🔹 Model Training  
We trained multiple models to classify malware effectively:  

| **Model**              | **Performance** |
|------------------------|----------------|
| Support Vector Machine (SVM) ✅ | **97.52% (Best Model)** |
| Logistic Regression    | Moderate Accuracy |
| Naïve Bayes           | Fast but Lower Accuracy |
| Random Forest         | High Accuracy but Overfitting Risk |

#### 🔧 Optimization Techniques Used  
- **Hyperparameter tuning** using `GridSearchCV`  
- **K-Fold Cross Validation** to prevent overfitting  

---

### 🔹 Prediction & Model Evaluation  
The trained models were tested on a **separate test dataset**, and performance was evaluated using:  
✅ **Accuracy**: **97.52% (SVM)**  
✅ **Precision**: **97.97%**  
✅ **Recall**: **97.86%**  
✅ **F1 Score**: **97.86%**  

📊 The SVM model emerged as the best classifier with the highest accuracy and generalization capability.  

---

## 🔧 Preprocessing & Feature Engineering  

To ensure high efficiency, the following preprocessing steps were implemented:  

### 1️⃣ Data Cleaning  
✔ **Checked for missing/corrupted values** and handled them appropriately  
✔ **Converted categorical features** into numerical representations  
✔ **Standardized & normalized numerical features** for better model convergence  

### 2️⃣ Feature Selection  
✔ **SHAP** → Interpreted feature importance & removed redundant features  
✔ **RFE (Recursive Feature Elimination)** → Reduced less relevant API functions  
✔ **Selected only high-impact DLL & PE header features**  

### 3️⃣ Model-Specific Preprocessing  
✔ Applied **One-Hot Encoding & Label Encoding** where required  
✔ Data **split into training & testing sets**  
✔ **Hyperparameter tuning** using `GridSearchCV` for model performance optimization  

---

## ⚡ Challenges & Solutions  

| **Challenge** | **Solution Implemented** |
|--------------|--------------------------|
| **High-dimensional feature space** | Used **SHAP & RFE** to reduce unnecessary features |
| **Selecting the best model** | Trained multiple models, optimized using **GridSearchCV** & selected **SVM** |
| **Computational inefficiency** | Applied **LightGBM** for API functions & **AdaBoost** for DLL & PE features |
| **Resource constraints** | Divided tasks into smaller problems & used **parallel processing** |

---

## 🔮 Future Enhancements  

🚀 **Quantum Machine Learning (QML)**  
- Experimented with **PennyLane QML** but encountered accuracy issues due to high-dimensional feature space  
- Future improvements could leverage **advanced quantum hardware**  

🚀 **Deep Learning-Based Malware Detection**  
- Testing **LSTMs & CNNs** for sequence-based malware analysis  
- Implementing **Autoencoders** for anomaly detection  

---

## 📂 Code Repository & Usage  

🔗 **GitHub Repository**: [MINed_Hackoholics](https://github.com/Anni1808/MINed_Hackoholics.git)  

### 📜 Installation & Setup  

1️⃣ Clone the repository:  
```bash
git clone https://github.com/Anni1808/MINed_Hackoholics.git
cd MINed_Hackoholics
```
  
2️⃣ Install dependencies:  
```bash
pip install -r requirements.txt
```
  
3️⃣ Run the malware detection pipeline:  
```bash
python malware_detection.py
```

---


📧 **Contact**: If you have any questions or suggestions, feel free to open an issue on GitHub!  
