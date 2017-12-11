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

    image = Image.open(args.img_in).convert('LA')
    width, height = image.size

    total_width = width * 3
    max_height = height * 3

    #Creating the image
    new_im = Image.new('RGB', (total_width, max_height))
    
    #Pasting original image
    new_im.paste(image, (width, height))

    #Pasting vert flips
    vert_flip = ImageOps.flip(image)
    new_im.paste(vert_flip, (width, 0))
    new_im.paste(vert_flip, (width, 2*height))

    #Pasting horiz flip
    hor_flip = ImageOps.mirror(image)
    new_im.paste(hor_flip, (0, height))
    new_im.paste(hor_flip, (2*width, height))

    #pasting double flip
    doub_flip = ImageOps.mirror(vert_flip)
    new_im.paste(doub_flip, (0,0))
    new_im.paste(doub_flip, (2*width, 0))
    new_im.paste(doub_flip, (0, 2*height))
    new_im.paste(doub_flip, (2*width, 2*height))

    image.save(args.img_out + 'bw.png')
    new_im.save(args.img_out + 'tess.png')
