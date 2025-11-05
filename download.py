"""
Script to download and prepare data from Kaggle
"""
import os
import sys
# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import numpy as np
import kagglehub

def download_datasets():
    """Download datasets from Kaggle"""
    print("Downloading RNA and mutations dataset...")
    rna_path = kagglehub.dataset_download('martininf1n1ty/dna-methylation-adnotated')
    print(f"RNA dataset downloaded to: {rna_path}")
    print("Downloading VAE dataset...")

if __name__ == "__main__":
    download_datasets()