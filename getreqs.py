import sys
import pkgutil
import libfinder

file_main = sys.argv[1]

def get_preinstalled_libraries():
    preinstalled = set()
    
    # Get all modules from sys.builtin_module_names
    preinstalled.update(sys.builtin_module_names)
    
    # Get all modules from sys.stdlib_module_names (Python 3.10+)
    if hasattr(sys, 'stdlib_module_names'):
        preinstalled.update(sys.stdlib_module_names)
    
    # Get all modules from pkgutil.iter_modules
    for module in pkgutil.iter_modules():
        preinstalled.add(module.name)
    return preinstalled

listof = libfinder.get_modules(file_main)
print( "\n List of imports", listof)

def read_libraries_from_file(filename):
    with open(filename, 'r') as f:
        return set(line.strip() for line in f if line.strip())

# Get pre-installed libraries
preinstalled_libs = get_preinstalled_libraries()

sorted_preinstalled_libs = sorted(preinstalled_libs)
# Read libraries from the text file

# Remove common libraries (pre-installed ones)
libraries_to_install = [lib for lib in listof if lib not in sorted_preinstalled_libs]

print(libraries_to_install)
# Sort the list alphabetically


print("Libraries to install:")
f = open('requirements.txt', 'w')
for lib in libraries_to_install:
    f.write(lib + "\n")
    print(lib)
print(f"\nTotal number of libraries to install: {len(libraries_to_install)}")