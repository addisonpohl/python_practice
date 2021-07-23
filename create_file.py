import os
import sys

filename=sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("File has been created")

else:
    print(f"The file '{filename}' already exists.")