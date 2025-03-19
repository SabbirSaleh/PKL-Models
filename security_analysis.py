import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATHS = {
    "Dataset1": os.path.join(BASE_DIR, "models/Dataset1_SSCA.xlsx_model.pkl"),
    "Dataset1_Copy": os.path.join(BASE_DIR, "models/Dataset1_SSCA_copy.xlsx_model.pkl"),
    "Dataset2": os.path.join(BASE_DIR, "models/Dataset2_BTF.xlsx_model.pkl")
}
DICTIONARY_PATH = os.path.join(BASE_DIR, "models/dictionary.pkl")

# Print paths for debugging
print("🔍 Debugging Paths:")
print(f"Model Path: {MODEL_PATHS['Dataset1']} (Exists? {'✅ Yes' if os.path.exists(MODEL_PATHS['Dataset1']) else '❌ No'})")
print(f"Dictionary Path: {DICTIONARY_PATH} (Exists? {'✅ Yes' if os.path.exists(DICTIONARY_PATH) else '❌ No'})")

# Load dictionary first
try:
    with open(DICTIONARY_PATH, "rb") as f:
        dictionary = pickle.load(f)
    print("✅ Dictionary loaded successfully!")
except Exception as e:
    print(f"❌ Failed to load dictionary.pkl: {e}")
    exit(1)

# Load model
try:
    with open(MODEL_PATHS["Dataset1"], "rb") as f:
        model = pickle.load(f)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Failed to load LDA model: {e}")
    exit(1)
