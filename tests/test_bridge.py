import codelens_core
import os

print("Testing the Real C++ File Walker...\n")

# Get the absolute path of the directory we are currently in (the DECODEx01 folder)
current_dir = os.path.abspath(".")

# Call our new C++ function!
files = codelens_core.walk_repository(current_dir)

print(f"Successfully scanned and found {len(files)} files!")
print("Here are the first 10 files discovered:\n")

# Print just the first 10 so we don't flood your terminal
for f in files[:10]:
    print(f" 📄 {f}")