import os
import nbformat

# Define the root directory where your notebooks are located
root_dir = "/docs"

# Walk through the directory tree
for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".ipynb"):
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
                    cell.metadata["tags"].append("hide-output")

            # Save the modified notebook
            with open(notebook_path, "w") as f:
                nbformat.write(nb, f)

print("All notebooks processed.")
