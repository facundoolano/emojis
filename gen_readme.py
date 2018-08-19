#!/usr/bin/env python3
import os

def image_files():
    return [image for image in sorted(os.listdir("emojis"))]

def build_markdown():
    output = "# emojis\nvery important emojis\n"

    for image in image_files():
        path = "./emojis/" + image
        name = image.split('.')[0]
        output += "\n**:{}:** <img src=\"{}\" height=\"32\">\n".format(name, path)

    return output


print(build_markdown())
