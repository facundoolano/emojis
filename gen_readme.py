#!/usr/bin/env python3
import os

def image_files():
    return [image for image in sorted(os.listdir("emojis"))]

def build_markdown():
    output = "# emojis\n"
    output += "very important emojis\n\n"
    output += "| image | code |\n"
    output += "|:----:|:-----:|\n"

    for image in image_files():
        path = "./emojis/" + image
        name = image.split('.')[0]
        output += "| <img src=\"{}\" height=\"32\"> |`:{}:` |\n".format(path, name)

    return output


print(build_markdown())
