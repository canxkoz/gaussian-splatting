import cv2
import numpy as np
import ast

import os
import subprocess

model_name = "58819a86-a" # dummy
angles_txt = "/YOUR-HOME-PATH/gaussian-splatting/camera_center.txt"
views_path = f"/YOUR-HOME-PATH/gaussian-splatting/output/{model_name}/train/ours_30000/renders"
output_folder = "/YOUR-HOME-PATH/gaussian-splatting/output/truck"
view_name = "00230.png"

with open(angles_txt, "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    line = list(map(float, line.split()))

    subprocess.run(["python", "render.py", "-m", f"/YOUR-HOME-PATH/gaussian-splatting/output/{model_name}", "--light_position", str(line[0]), str(line[1]), str(line[2])])

    # move selected view to output folder
    subprocess.run(["mv", os.path.join(views_path, view_name), output_folder])

    # change the name of the selected view to the current iteration
    subprocess.run(["mv", os.path.join(output_folder, view_name), os.path.join(output_folder, f"{i}.png")])

