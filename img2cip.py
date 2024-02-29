#!/usr/bin/env python

# img2cip - a utility to convert a PNG image to a 133x65 (max) CIP (CiscoIPPhoneImage) format hex string.
# This is useful for creating custom images for Cisco IP Phones.

# Usage: img2cip.py <input.png> <output.txt> [width] [height]
# Example: img2cip.py input.png output.txt 133 65

import sys
import os
from PIL import Image

# Argument check
if len(sys.argv) < 3 or len(sys.argv) > 5:
    print("Usage: img2cip.py <input.png> <output.txt> [width] [height]")
    sys.exit(1)

# Input and output files
input_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the input file exists
if not os.path.isfile(input_file):
    print("Input file does not exist.")
    sys.exit(1)

# Width and height
width = 133
height = 65

# If width and height are provided, update the default values
if len(sys.argv) == 5:
    try:
        width = int(sys.argv[3])
        height = int(sys.argv[4])
    except ValueError:
        print("Width and height must be integers.")
        sys.exit(1)

# Open the input image
try:
    image = Image.open(input_file)
except IOError:
    print("Failed to open input image.")
    sys.exit(1)

# Resize the image to a maximum size of width x height
image.thumbnail((width, height))

# Convert the image to grayscale
image = image.convert("L")

# Invert the image
image = image.point(lambda p: 255 - p)

# Convert the image to a hex string
hex_string = ""
pixels = list(image.getdata())
byte = 0
count = 0
for pixel in pixels:
    # Map grayscale values to 2bpp values
    pixel = pixel // 64
    # Accumulate 2-bit values into a byte
    byte = (byte >> 2) | (pixel << 6)
    count += 1
    # Once we have four 2-bit values, write the byte to the hex string
    if count == 4:
        hex_string += "{:02x}".format(byte)
        byte = 0
        count = 0
# If there are remaining 2-bit values that have not been written, write them now
if count > 0:
    byte = byte << (2 * (4 - count))
    hex_string += "{:02x}".format(byte)

# Write to the output file
with open(output_file, "w") as file:
    file.write(hex_string)

# Print the hex string
print("Conversion complete. Hex string written to", output_file + ".")
print("Hex string:")
print(hex_string.upper())
