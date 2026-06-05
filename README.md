# 🍾 Beverage Label Compliance Checker

A Streamlit‑powered web application that analyzes beverage label images for **regulatory compliance**, using **OCR (EasyOCR)** + **fuzzy rule matching** to detect required warnings, alcohol content statements, volume declarations, and producer information.

This tool is designed for distillers, bottlers, compliance teams, and developers who need fast, automated label verification.

---

## 🚀 Features

- **Bulk Upload** — process multiple label images at once  
- **Camera Capture** — take a photo directly from your device  
- **OCR Extraction** — EasyOCR with preprocessing for high accuracy  
- **Rule Evaluation** — checks for required words, phrases, and patterns  
- **Fuzzy Matching** — detects text even when imperfect or distorted  
- **Detailed Results** — PASS / WARNING / FAIL with issue breakdown  
- **CSV Export** — download all results for auditing  
- **Multi‑Page Streamlit App** — clean navigation and UI  
- **Fast Performance** — caching + parallel processing  

---

## 🧠 How It Works

1. User uploads or captures a label image  
2. Image is preprocessed (resize → grayscale → blur → threshold)  
3. EasyOCR extracts text  
4. Text is evaluated against compliance rules in `beverage_rules.json`  
5. App returns:
   - **PASS** — all required elements found  
   - **WARNING** — minor missing elements  
   - **FAIL** — major compliance issues  
6. Results can be exported as CSV  

---

## 🛠️ Installation (Local Development)

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/beverage-checker.git
cd beverage-checker
```

### 2. Create a virtual environment
```bash
python3 -m venv torch_env
source torch_env/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. Run the app
```
streamlit run app.py
```
