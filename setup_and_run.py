"""
Setup script for Churn Prediction Notebook
This script helps you:
1. Install required packages
2. Check if the dataset exists
3. Provide instructions for running the notebook
"""

import subprocess
import sys
import os

def install_packages():
    """Install required packages"""
    packages = [
        'scikit-learn',
        'pandas',
        'numpy',
        'matplotlib',
        'joblib'
    ]
    
    print("Installing required packages...")
    for package in packages:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '--user'])
            print(f"[OK] {package} installed successfully")
        except subprocess.CalledProcessError:
            print(f"[WARNING] Failed to install {package}. You may need to install it manually.")
            print(f"   Run: pip install {package} --user")

def check_dataset():
    """Check if the dataset exists"""
    possible_paths = [
        "telco_customer_churn.csv",
        os.path.join(os.path.expanduser("~"), "Downloads", "telco_customer_churn.csv"),
        os.path.join(os.path.dirname(__file__), "telco_customer_churn.csv")
    ]
    
    print("\nChecking for dataset...")
    for path in possible_paths:
        if os.path.exists(path):
            print(f"[OK] Dataset found at: {path}")
            return path
    
    print("[WARNING] Dataset not found!")
    print("\nPlease download the Telco Customer Churn dataset from:")
    print("   https://www.kaggle.com/datasets/blastchar/telco-customer-churn")
    print("\nOr use this direct link if available:")
    print("   https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv")
    print("\nSave it as 'telco_customer_churn.csv' in your Downloads folder or the same folder as this notebook.")
    return None

def main():
    print("=" * 60)
    print("Churn Prediction Notebook - Setup Script")
    print("=" * 60)
    
    # Install packages
    install_packages()
    
    # Check dataset
    dataset_path = check_dataset()
    
    print("\n" + "=" * 60)
    print("Setup Complete!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Open the notebook: Churn_Prediction_Colab.ipynb")
    print("2. Make sure Jupyter is installed: pip install jupyter notebook")
    print("3. Launch Jupyter: jupyter notebook")
    print("4. Open the notebook and run all cells")
    
    if dataset_path:
        print(f"\n[OK] Your dataset is at: {dataset_path}")
        print("   The notebook should automatically detect it.")
    else:
        print("\n[WARNING] Remember to download the dataset before running the notebook!")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()

