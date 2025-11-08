# Customer-Churn-Analysis-and-Prediction-Telco-Dataset-
Predict customer churn using machine learning with Logistic Regression and Decision Tree models on the Telco dataset. Includes data preprocessing, exploratory data analysis (EDA), model training, evaluation (ROC-AUC, accuracy), and visualizations — all in one interactive Jupyter Notebook.

# 📊 Telco Customer Churn Prediction

A machine learning project to predict **customer churn** using **Logistic Regression** and **Decision Tree Classifier** on the **Telco Customer Churn dataset**.  
This notebook performs data preprocessing, exploratory data analysis (EDA), model training, and evaluation — all in a single interactive environment.

---

## 🚀 Quick Start

### 🧰 1. Setup Environment
Create and activate a virtual environment (recommended):

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
📥 2. Download Dataset
Option A – Automatic Download

bash
Copy code
python download_dataset.py
Option B – Manual Download

Go to the Kaggle Telco Customer Churn Dataset

Download and extract the CSV file

Rename it to telco_customer_churn.csv

Place it in the same folder as the notebook (132.ipynb)

▶️ 3. Run the Notebook
Option 1 (Windows):

bash
Copy code
run_notebook.bat
Option 2 (macOS/Linux):

bash
Copy code
bash run_notebook.sh
or open it manually:

bash
Copy code
jupyter notebook 132.ipynb
Once Jupyter opens, click Cell → Run All.

📁 Project Structure
bash
Copy code
📦 Telco-Customer-Churn
├── 132.ipynb                # Main Notebook (Data prep, ML model, visualization)
├── download_dataset.py      # Script to auto-download dataset
├── run_notebook.bat         # Batch file for Windows
├── run_notebook.sh          # Shell script for macOS/Linux
├── telco_customer_churn.csv # Dataset (if downloaded manually)
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitignore               # Ignored files/folders
🧠 Notebook Workflow
Data Loading & Cleaning – Loads CSV, handles missing values

Exploratory Data Analysis (EDA) – Visualizations for churn insights

Feature Encoding & Scaling – Prepares data for ML algorithms

Model Training

Logistic Regression

Decision Tree (Entropy-based)

Evaluation Metrics

Accuracy, ROC–AUC, Confusion Matrix, Precision, Recall

Model Exporting – Saves best model to models/best_model.pkl

Reports & Charts – Automatically saved in reports/ and charts/

📊 Output Files
Folder	Description
charts/	Contains all generated graphs (PNG format)
models/	Trained models stored as .pkl
reports/	Decision rules and evaluation reports

🛠️ Troubleshooting
Dataset Not Found:
Ensure the file is named telco_customer_churn.csv and is in the repo or your Downloads folder.

Import Errors:
Run pip install -r requirements.txt again.

Permission Denied (Linux/macOS):
Run commands with --user or sudo.

🧾 Requirements
This project uses the following packages:

Python 3.8+

Jupyter Notebook

pandas

numpy

scikit-learn

matplotlib

joblib

To install all dependencies:

bash
Copy code
pip install -r requirements.txt
🧩 Notes
This project is fully local (no Google Colab required)

Compatible with Windows, macOS, and Linux

Automatically creates directories for models and reports

EDA and evaluation outputs are saved automatically

🏷️ License
This project is licensed under the MIT License — you’re free to use, modify, and distribute it.

👤 Author
Your Name
💻 Machine Learning | Data Science Enthusiast
📧 your-email@example.com
🔗 GitHub Profile

⭐ If you find this project useful, don’t forget to star the repo!

yaml
Copy code

---

Would you like me to:
- 🔹 Add **badges** (Python version, license, made with ❤️, etc.)  
- 🔹 Or generate a **release-ready ZIP** folder (GitHub upload format with all files & README includ
