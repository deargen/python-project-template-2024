import doctest
import importlib
import os

# run doctest for all modules in src/

# find all modules in src/
modules = []
for root, dirs, files in os.walk("src"):
    for file in files:
        if file.endswith(".py"):
            # convert path to module name
            root = root.replace("src/", "")
            root = root.replace("/", ".")
            modules.append(root + "." + os.path.splitext(file)[0])

# run doctest for all modules
for module_name in modules:
    module = importlib.import_module(module_name)
    result = doctest.testmod(module, verbose=True)
    if result.failed > 0:
        print("doctest failed for module: " + module_name)
        print(f"{result.failed} failed out of {result.attempted} tests")
        exit(1)
