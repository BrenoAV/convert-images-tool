import glob
import os
from pathlib import Path

from PIL import Image


def create_dir(path_dir: str) -> None:
    path_dir_obj = Path(path_dir)
    if not path_dir_obj.exists():
        path_dir_obj.mkdir(parents=True, exist_ok=True)


def convert_img(img_filepath: str, output_path_dir: str, new_ext: str) -> None:
    root, _ = os.path.splitext(img_filepath)
    with Image.open(img_filepath) as img:
        filename = root.split(os.sep)[-1]
        img.save(
            os.path.join(output_path_dir, filename + "." + new_ext), format=new_ext
        )


def convert_folder_img(input_folder: str, output_dir: str, format: str):
    folder_input_path = Path(input_folder)
    if not folder_input_path.exists():
        raise SystemError("The input directory `%s` doesn't exist!" % folder_input_path)

    create_dir(output_dir)
    patterns = (
        "*.[jJ][pP][gG]*",
        "*.[jJ][pP][eE][gG]*",
        "*.[pP][nN][gG]*",
        "*.[tT][iI][fF][fF]*",
        "*.[wW][eE][bB][pP]*",
    )
    files = []
    for p in patterns:
        files.extend(glob.glob(os.path.join(folder_input_path, p)))
    for file in files:
        convert_img(img_filepath=file, output_path_dir=output_dir, new_ext=format)
