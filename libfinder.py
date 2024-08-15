import os
import re
import importlib.util

def get_modules(folder_path):
    # Traverse the folder recursively
    libraries = set()
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)

                with open(file_path, 'r') as f:
                    lines = f.readlines()

                import_pattern = re.compile(r'^(?:from\s+([\w.]+)\s+import\s+[\w,\s*]+|import\s+([\w.,\s]+))$')

    
                for line in lines:
                    line = line.strip()
                    match = import_pattern.match(line)
                    if match:
                        if match.group(1):  # 'from' import
                            lib = match.group(1).split('.')[0]
                            if importlib.util.find_spec(lib) is not None:
                                libraries.add(lib)
                        else:  # 'import' statement
                            imports = match.group(2).split(',')
                            for imp in imports:
                                lib = imp.strip().split(' as ')[0].split('.')[0]
                                if importlib.util.find_spec(lib) is not None:
                                    libraries.add(lib)

    
    sorted_libraries = sorted(libraries)
    return sorted_libraries
