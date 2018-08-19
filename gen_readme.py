#!/usr/bin/env python3
import os

IMAGE_FORMATS = ['jpg', 'png', 'gif']

def is_image_file(filename):
    suffix = filename.split('.')[-1]
    return suffix in IMAGE_FORMATS

def image_files():
    return [image for image in sorted(os.listdir()) if is_image_file(image)]

def build_markdown():
    output = "# emojis\nvery important emojis\n"

    for image in image_files():
        path = "./" + image
        name = image.split('.')[0]
        output += "\n**:{}:** <img src=\"{}\" height=\"32\">\n".format(name, path)

    return output


print(build_markdown())
