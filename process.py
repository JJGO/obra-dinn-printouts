#!/usr/bin/env python
from pathlib import Path
from typing import List
import os

from PIL import Image
import typer

import numpy as np


def process(images: List[str], alpha: float = 0.5):

    for img in images:
        img2 = img.replace(".png", "-post.png")
        cmd = f"convert '{img}' -set colorspace Gray -separate -average -auto-level '{img2}'"
        # os.system(cmd)
        x = np.array(Image.open(img2))
        y = x.astype(np.float64) * alpha + (1-alpha) * 255
        img3 = img.replace(".png", "-post-alpha.png")
        Image.fromarray((y).astype(np.uint8)).save(img3)


if __name__ == "__main__":
    typer.run(process)
