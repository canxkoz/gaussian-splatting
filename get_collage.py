import cv2
import numpy as np

import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Get collage from renders")

    parser.add_argument("--source_path", type=str, default="/home/canxk/3dgs/gaussian-splatting/output")
    parser.add_argument("--render_folders", type=str, nargs="+", default=["sh-degree-0", "sh-degree-1", "sh-degree-2", "sh-degree-3"])
    parser.add_argument("--wanted_png_file", type=str, default="00000.png")
    parser.add_argument("--iteration", type=int, default=7000)
    
    args = parser.parse_args()
    source_path = args.source_path
    render_folders = args.render_folders
    wanted_png_file = args.wanted_png_file
    iteration = args.iteration

    images = []

    # get ground truth image
    img = cv2.imread(f"{source_path}/{render_folders[0]}/train/ours_{str(iteration)}/gt/{wanted_png_file}")
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, 30)
    fontScale = 1
    fontColor = (255, 255, 255)
    lineType = 2
    cv2.putText(img, f"GT",
                bottomLeftCornerOfText, 
                font, 
                fontScale,
                fontColor,
                lineType)
    images.append(img)

    # get renders
    for folder in render_folders:
        img = cv2.imread(f"{source_path}/{folder}/train/ours_{str(iteration)}/renders/{wanted_png_file}")

        # write render degree top left corner of the image
        font = cv2.FONT_HERSHEY_SIMPLEX
        bottomLeftCornerOfText = (10, 30)
        fontScale = 1
        fontColor = (255, 255, 255)
        lineType = 2
        cv2.putText(img, f"SH Degree: {folder[-1].split('-')[-1]}",
                    bottomLeftCornerOfText, 
                    font, 
                    fontScale,
                    fontColor,
                    lineType)

        images.append(img)

    collage = np.concatenate(images, axis=1)
    cv2.imwrite(f"{source_path}/collage_{wanted_png_file.split('.')[0]}.png", collage)