import os

print("🔍 Checking model and dictionary file paths...\n")

model_files = [
    "models/Dataset1_SSCA.xlsx_model.pkl",
    "models/Dataset1_SSCA_copy.xlsx_model.pkl",
    "models/Dataset2_BTF.xlsx_model.pkl",
    "models/dictionary.pkl"
]

for file in model_files:
    exists = os.path.exists(file)
    print(f"{file} - Exists? {'✅ Yes' if exists else '❌ No'}")

print("\n🔍 Checking absolute paths...")
for file in model_files:
    abs_path = os.path.abspath(file)
    print(f"{file} -> {abs_path} (Exists? {'✅ Yes' if os.path.exists(abs_path) else '❌ No'})")
