import pickle
import os

# List of your model files
model_files = [
    "Dataset1_SSCA.xlsx_model.pkl",
    "Dataset1_SSCA_copy.xlsx_model.pkl",
    "Dataset2_BTF.xlsx_model.pkl"
]

for model_file in model_files:
    try:
        print(f"\n🔍 Checking model: {model_file}")
        with open(model_file, "rb") as f:
            model = pickle.load(f)

        # Print model type
        print("✅ Loaded successfully!")
        print("🔹 Type of model:", type(model))

        # If it's an LDA model, print topics
        if hasattr(model, "print_topics"):
            print("📌 LDA Topics Preview:")
            print(model.print_topics(num_words=5))

        print("-" * 50)

    except Exception as e:
        print(f"❌ Error loading {model_file}: {e}")
