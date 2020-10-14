#!/usr/bin/env python3

import cv2
import numpy as np

from pathlib import Path


class Image:

    def __init__(self, filepath):
        self._filepath = Path(filepath)
        if not self._filepath.exists():
            raise ValueError(f"Input image '{filepath}' does not exist")
        self._image = cv2.imread(str(self._filepath))

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"Image({self.filepath})"

    @property
    def filepath(self):
        return self._filepath

    @property
    def filename(self):
        return self._filepath.name

    @property
    def parentname(self):
        return self._filepath.parent.name

    @property
    def image(self):
        return self._image.copy()

    @property
    def resolution(self):
        return self._image.shape[:-1]

    @property
    def height(self):
        return self.resolution[0]

    @property
    def width(self):
        return self.resolution[1]

    @property
    def area(self):
        return self.height * self.width
