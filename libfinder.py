import os
import re

def get_modules(getpath):
    with open(getpath, 'r') as f:
        lines = f.readlines()
    
    import_pattern = re.compile(r'^(?:from\s+([\w.]+)\s+import\s+[\w,\s*]+|import\s+([\w.,\s]+))$')
    
    libraries = set()
    for line in lines:
        line = line.strip()
        match = import_pattern.match(line)
        if match:
            if match.group(1):  # 'from' import
                lib = match.group(1).split('.')[0]
                libraries.add(lib)
            else:  # 'import' statement
                imports = match.group(2).split(',')
                for imp in imports:
                    lib = imp.strip().split(' as ')[0].split('.')[0]
                    libraries.add(lib)
    
    sorted_libraries = sorted(libraries)
    print(sorted_libraries)
    return sorted_libraries

get_modules('C:\\Users\\Vaibhav\\Desktop\\screensaver.py')