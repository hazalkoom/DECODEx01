#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <string>

namespace py = pybind11;

// Using std:: explicitly is the best practice for scalable C++ code
std::vector<std::string> get_mock_files(const std::string& folder_name) {
    
    std::vector<std::string> my_files;
    
    my_files.push_back(folder_name + "/main.py");
    my_files.push_back(folder_name + "/database.db");
    
    return my_files;
}

PYBIND11_MODULE(codelens_core, m) {
    m.def("get_mock_files", &get_mock_files, "Returns a fake list of files for testing");
}