# Customer Churn Prediction Notebook

This notebook predicts customer churn using machine learning models (Logistic Regression and Decision Tree).

## Setup Instructions

### 1. Install Required Packages
All required packages have been installed via the setup script. If you need to reinstall:
```bash
pip install scikit-learn pandas numpy matplotlib joblib jupyter notebook --user
```

### 2. Download the Dataset
You need to download the Telco Customer Churn dataset:

**Option A: From Kaggle (requires account)**
1. Visit: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
2. Download the dataset
3. Save it as `telco_customer_churn.csv` in your Downloads folder

**Option B: Direct Download (if available)**
Run the download script:
```bash
python download_dataset.py
```

**Option C: Manual Download**
1. Download from: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
2. Extract the CSV file
3. Save it as `telco_customer_churn.csv` in the same folder as this notebook or in your Downloads folder

### 3. Run the Notebook
1. Make sure Jupyter is installed: `pip install jupyter notebook --user`
2. Launch Jupyter: `jupyter notebook`
3. Open `Churn_Prediction_Colab.ipynb`
4. Run all cells (Cell > Run All)

## What the Notebook Does

1. **Data Loading**: Loads and preprocesses the Telco Customer Churn dataset
2. **EDA**: Exploratory Data Analysis with visualizations
3. **Model Training**: Trains two models:
   - Logistic Regression
   - Decision Tree (CHAID-like with entropy)
4. **Evaluation**: 
   - ROC-AUC curves
   - Lift/Gain charts
   - Confusion matrices
5. **Rule Extraction**: Extracts readable rules from the Decision Tree
6. **Model Saving**: Saves the best model for deployment

## Output Files

The notebook creates:
- `charts/` - Visualization files (PNG images)
- `models/` - Saved model files (best_model.pkl)
- `reports/` - Decision tree rules and reports

## Troubleshooting

- **Dataset not found**: Make sure the CSV file is named `telco_customer_churn.csv` and is in your Downloads folder or the same folder as the notebook
- **Import errors**: Run `pip install <package_name> --user` for the missing package
- **Permission errors**: Use `--user` flag when installing packages

## Notes

- This notebook has been modified to work locally (removed Google Colab dependencies)
- The notebook will automatically detect the dataset if it's in the Downloads folder
- All visualizations are saved to the `charts/` directory

