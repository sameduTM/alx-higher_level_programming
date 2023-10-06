#!/usr/bin/python3
import builtins
import importlib.util

# load the compiled module
mod_name = "hidden_4"
spec = importlib.util.spec_from_file_location(mod_name, f"{mod_name}.pyc")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# get all defined names in the module
module_names = dir(module)

if __name__ == "__main__":
    for name in sorted(module_names):
        if not name.startswith("__"):
            print(name)
