# This Python script runs through all .ipynb files in "docs" and its sub-folders
# and adds "hide-output" tags to all code cells.
# It needs to be run manually.

import os
import nbformat

# Define the root directory where your notebooks are located
root_dir = "docs"

# Walk through the directory tree
notebooks_found = False
for subdir, _, files in os.walk(root_dir):
    print(f"Checking directory: {subdir}")
    for file in files:
        if file.endswith(".ipynb"):
            notebooks_found = True
            notebook_path = os.path.join(subdir, file)
            print(f"Processing notebook: {notebook_path}")

            # Load the notebook
            with open(notebook_path, "r") as f:
                nb = nbformat.read(f, as_version=4)

            # Apply 'hide-output' tag to all code cells
            for cell in nb.cells:
                if cell.cell_type == "code":
                    if "tags" not in cell.metadata:
                        cell.metadata["tags"] = []
                    if "hide-output" not in cell.metadata["tags"]:
                        cell.metadata["tags"].append("hide-output")
                        print(f"Tag applied to cell in notebook: {notebook_path}")

            # Save the modified notebook
            with open(notebook_path, "w") as f:
                nbformat.write(nb, f)

if not notebooks_found:
    print("No notebooks found in the specified directory.")
else:
    print("All notebooks processed.")
