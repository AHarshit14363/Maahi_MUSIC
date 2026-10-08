import os
import importlib


def __list_all_modules():
    work_dir = os.path.dirname(__file__)
    all_modules = []

    for root, dirs, files in os.walk(work_dir):
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, work_dir)
                module = relative_path[:-3].replace(os.sep, ".")
                all_modules.append(module)

    return all_modules


ALL_MODULES = sorted(__list_all_modules())

__all__ = ALL_MODULES + ["ALL_MODULES"]
