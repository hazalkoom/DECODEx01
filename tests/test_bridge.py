# Import the C++ module we just compiled!
import codelens_core

print("Testing the C++ to Python Bridge...\n")

# Call the C++ function. Notice how we pass a Python string, 
# and it automatically becomes a C++ std::string behind the scenes!
files = codelens_core.get_mock_files("my_awesome_project")

print("Data received straight from C++:")
for f in files:
    print(f" 📄 {f}")