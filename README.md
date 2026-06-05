🍾 Beverage Label Compliance Checker

A Streamlit‑powered web application that analyzes beverage label images for regulatory compliance, using OCR (EasyOCR) + fuzzy rule matching to detect required warnings, alcohol content statements, volume declarations, and producer information.
This tool is designed for distillers, bottlers, compliance teams, and developers who need fast, automated label verification.
🚀 Features
Bulk Upload — process multiple label images at once
Camera Capture — take a photo directly from your device
OCR Extraction — EasyOCR with preprocessing for high accuracy
Rule Evaluation — checks for required words, phrases, and patterns
Fuzzy Matching — detects text even when imperfect or distorted
Detailed Results — PASS / WARNING / FAIL with issue breakdown
CSV Export — download all results for auditing
Multi‑Page Streamlit App — clean navigation and UI
Fast Performance — caching + parallel processing
📁 Project Structure
Code
beverage-checker/
│
├── app.py
├── ocr.py
├── rules.py
├── requirements.txt
├── packages.txt
├── .gitignore
│
├── configs/
│   └── beverage_rules.json
│
└── pages/
    ├── 1_📤_Upload_Labels.py
    ├── 2_📸_Camera_Capture.py
    └── 3_📊_Results.py
🧠 How It Works
User uploads or captures a label image
Image is preprocessed (resize → grayscale → blur → threshold)
EasyOCR extracts text
Text is evaluated against compliance rules in beverage_rules.json
App returns:
PASS — all required elements found
WARNING — minor missing elements
FAIL — major compliance issues
Results can be exported as CSV
🛠️ Installation (Local Development)
1. Clone the repository
bash
git clone https://github.com/<your-username>/beverage-checker.git
cd beverage-checker
2. Create a virtual environment
bash
python3 -m venv torch_env
source torch_env/bin/activate
3. Install dependencies
bash
pip install -r requirements.txt
4. Run the app
bash
streamlit run app.py

📜 Compliance Rules (beverage_rules.json)
Rules include:
Required words
Required phrases
Volume indicators
Producer statements
Optional terms
Regex patterns
Fuzzy thresholds
These can be customized to match regulatory requirements.

🧪 Example Output

(EasyOCR)** + fuzzy rule matching to detect required warnings, alcohol content statements, volume declarations, and producer information.
This tool is designed for distillers, bottlers, compliance teams, and developers who need fast, automated label verification.
🚀 Features
Bulk Upload — process multiple label images at once
Camera Capture — take a photo directly from your device
OCR Extraction — EasyOCR with preprocessing for high accuracy
Rule Evaluation — checks for required words, phrases, and patterns
Fuzzy Matching — detects text even when imperfect or distorted
Detailed Results — PASS / WARNING / FAIL with issue breakdown
CSV Export — download all results for auditing
Multi‑Page Streamlit App — clean navigation and UI
Fast Performance — caching + parallel processing

🤝 Contributing
Pull requests are welcome!
If you’d like to add new rule categories, OCR engines, or analytics dashboards, feel free to open an issue.
📄 License
MIT License — free to use, modify, and distribute.
⭐ Support
If you find this project helpful, consider starring the repo!
It helps others discover the tool.