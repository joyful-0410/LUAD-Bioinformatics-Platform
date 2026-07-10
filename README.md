# 🫁 Lung Cancer Bioinformatics Platform

> **Machine Learning × SHAP × TCGA-LUAD × Precision Medicine**

An interactive bioinformatics platform for **lung adenocarcinoma (LUAD) prediction** using **Random Forest** and **10 SHAP-selected gene expression features**.

---

## 🌐 Live Demo

🚀 Streamlit

> https://joyful-luad-platform.streamlit.app/Model_Performance

GitHub Repository

> https://github.com/joyful-0410/LUAD生物資訊學平台

---

# 📖 Project Overview

Lung adenocarcinoma (LUAD) is one of the most common and deadly types of lung cancer worldwide.

This project aims to develop an interpretable machine learning platform that predicts LUAD risk using gene expression profiles.

Unlike a traditional prediction model, this platform integrates

- Machine Learning
- SHAP Explainability
- Gene Information
- Model Performance
- Interactive Visualization

into a single web application.

---

# ✨ Features

## 🤖 LUAD Prediction

- Random Forest classifier
- 10-gene expression input
- Probability prediction
- High / Low Risk classification
- AI interpretation

---

## 📊 Model Performance

- Accuracy
- Precision
- Recall
- F1-score
- ROC Curve
- Confusion Matrix

---

## 🧬 SHAP Analysis

Model explainability using SHAP.

Includes

- SHAP Feature Importance
- Top 10 Gene Ranking
- Biological interpretation

---

## 🔬 Gene Explorer

Detailed information for each selected gene.

Including

- Biological Function
- Cancer Association
- LUAD relevance
- Interpretation

---

## 📚 Dataset

Dataset Source

- TCGA-LUAD

Machine Learning Pipeline

```
Gene Expression

↓

Data Preprocessing

↓

Feature Selection

↓

Random Forest

↓

Prediction

↓

SHAP Interpretation
```

---

# 🧬 Selected Gene Panel

| Gene | Biological Function |
|------|----------------------|
| SLC34A2 | Lung epithelial differentiation |
| MUC16 | Tumor marker (CA125) |
| ANLN | Cell division |
| CDC20 | Cell cycle regulation |
| KIF20A | Mitosis |
| TOP2A | DNA replication |
| MKI67 | Cell proliferation |
| BIRC5 | Anti-apoptosis |
| TYMS | DNA synthesis |
| CCNA2 | Cell cycle progression |

---

# 🧠 Machine Learning

Algorithm

- Random Forest

Feature Selection

- SHAP

Input

- 10 Gene Expression Features

Output

- LUAD Risk Prediction

---

# 📂 Project Structure

```
LUAD_Bioinformatics_Platform

├── app.py
├── pages
│   ├── Prediction
│   ├── Model Performance
│   ├── SHAP Analysis
│   ├── Gene Explorer
│   ├── Dataset
│   └── About
│
├── data
├── assets
├── figures
├── utils.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

# 💻 Installation

Clone repository

```bash
git clone https://github.com/joyful-0410/LUAD生物資訊學平台.git
```

Install packages

```bash
pip install -r requirements.txt
```

Run

```bash
streamlit run app.py
```

---

# 📷 Platform Modules

- 🏠 Home
- 🤖 Prediction
- 📊 Model Performance
- 🧬 SHAP Analysis
- 🔬 Gene Explorer
- 📚 Dataset
- 👤 About

---

# 🔬 Research Background

This project was developed as an undergraduate bioinformatics project.

The objective is to combine

- Cancer Biology
- Machine Learning
- Explainable AI
- Bioinformatics

into an interactive platform for educational and research purposes.

---

# 🚀 Future Work

- Deep Learning models
- Multi-cancer prediction
- Survival analysis
- Drug response prediction
- TRBP2 module integration
- Clinical decision support

---

# 👨‍🔬 Author

**Kang-Sheng Liu (劉康聖)**

Department of Biotechnology

Chang Jung Christian University

Taiwan

---

# 📄 License

This project is intended for

- Academic research
- Educational purposes

Not for clinical diagnosis.

---

# ⭐ Acknowledgement

- TCGA
- Streamlit
- Scikit-learn
- SHAP
- Pandas
- NumPy
