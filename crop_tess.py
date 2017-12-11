import sys
from PIL import Image, ImageOps
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Reflective Padded Image')
    parser.add_argument('-img_in',dest='img_in',help='grayscale image to read in', type=str)
    parser.add_argument('-img_out',dest='img_out',help='colorized image to save off', type=str)


    args = parser.parse_args()
    return args

if __name__ == '__main__':

    args = parse_args()

    image = Image.open(args.img_in)
    width, height = image.size

    width = width/3
    height = height/3

    #Creating the image
    new_im = image.crop((width, height, 2*width, 2*height))

    new_im.save(args.img_out)

