"""
Download the Telco Customer Churn dataset
"""

import urllib.request
import os

def download_dataset():
    """Download the dataset from a public URL"""
    url = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
    filename = "telco_customer_churn.csv"
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads", filename)
    local_path = filename
    
    print("Attempting to download dataset...")
    print(f"URL: {url}")
    
    try:
        # Try downloading to current directory first
        print(f"\nDownloading to: {local_path}")
        urllib.request.urlretrieve(url, local_path)
        print(f"[OK] Dataset downloaded successfully to: {os.path.abspath(local_path)}")
        
        # Also copy to Downloads if different
        if os.path.abspath(local_path) != downloads_path:
            import shutil
            shutil.copy(local_path, downloads_path)
            print(f"[OK] Also saved to: {downloads_path}")
        
        return True
    except Exception as e:
        print(f"[ERROR] Failed to download dataset: {e}")
        print("\nPlease download manually from:")
        print("   https://www.kaggle.com/datasets/blastchar/telco-customer-churn")
        print("\nSave it as 'telco_customer_churn.csv' in your Downloads folder.")
        return False

if __name__ == "__main__":
    download_dataset()

