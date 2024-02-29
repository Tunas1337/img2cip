# Img2CIP - Image to CIP converter
## Description
Img2CIP is a simple tool to convert images to CIP format. The CIP format is a proprietary format that Cisco uses for its IP phones, namely the CiscoIPPhoneImageFile. The 7940 and 7960 phones use this format to display images on their screens.
It is a simple format that uses 2 bits per pixel (or more, but this script focuses on supporting the 7940 and 7960 phones) and the image is stored in a raw format. Each byte is 4 pixels, in reverse order: the first pixel is the least significant bit of the first byte, and the last pixel is the most significant bit of the last byte.

## Usage
```bash
python img2cip.py <input_image> <output_cip> [width] [height]
```

## Example
```bash
python img2cip.py image.png image.cip 133 65
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
CIP is a proprietary format of Cisco Systems, Inc. and this project is not affiliated with Cisco Systems, Inc.
