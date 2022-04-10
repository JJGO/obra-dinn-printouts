#!/usr/bin/env python
from pathlib import Path
import os

from PIL import Image
import typer

import numpy as np


# def process(images: List[str], alpha: float = 0.5):
def process(folder_name: str = "original", alpha: float = 0.5):

    folder = Path(folder_name)
    grayscale_folder = folder.parent / "grayscale"
    light_grayscale_folder = folder.parent / "light_grayscale"
    grayscale_folder.mkdir(exist_ok=True)
    light_grayscale_folder.mkdir(exist_ok=True)

    for img in folder.iterdir():
        img_grayscale = grayscale_folder / img.name
        cmd = f"convert '{img}' -set colorspace Gray -separate -average -auto-level '{img_grayscale}'"
        # subprocess.run(cmd.split(' '), check=True)
        os.system(cmd)
        x = np.array(Image.open(img_grayscale))
        y = x.astype(np.float64) * alpha + (1 - alpha) * 255
        img_light_grayscale = light_grayscale_folder / img.name
        Image.fromarray((y).astype(np.uint8)).save(img_light_grayscale)


if __name__ == "__main__":
    typer.run(process)
