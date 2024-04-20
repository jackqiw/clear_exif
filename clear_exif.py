import sys

from PIL import Image


def clearExifInfo(photoAddress):
    print(photoAddress)
    image = Image.open(photoAddress)
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    image_without_exif.save(photoAddress)
    print(image.size)
    return


# 命令行用法 python clear_exif.py E:\SB_PHOTO\xx.jpg
if __name__ == '__main__':
    photoDir = sys.argv[1]
    clearExifInfo(photoDir)

