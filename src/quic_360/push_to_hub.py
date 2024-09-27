from datasets import load_dataset, DatasetDict
from dotenv import load_dotenv
from pathlib import Path
import os
import pandas as pd

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_dir = os.path.join(root_dir, "dataset", "raw")
dotenv_path = os.path.join(root_dir, ".env")
print("root_dir: ", root_dir)
print("data_dir: ", data_dir)
print("dotenv_path: ", dotenv_path)

load_dotenv(dotenv_path)
token = os.environ.get("HF_TOKEN")
data_files = {
    "train": "train.tsv",
    "valid": "valid.tsv",
    "test": "test.tsv",
    "test_refer": "test-refer.tsv",
}
data_files = {split: os.path.join(data_dir, file) for split, file in data_files.items()}

print(data_files)

# Dataset の読み込み
dataset = load_dataset("csv", data_files=data_files, delimiter="\t") 

# データセットの確認 (オプションだけど、確認しておくと安心だよ！)
print(dataset)

# Hugging Face Hub への push
dataset.push_to_hub("Silviase/QuIC-360", token=token)