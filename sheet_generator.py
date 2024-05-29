import math
import os

from PIL import Image


# grabs a directory full of images and returns them as a single sheet
def parse_images(directory):
    if len(os.listdir(directory)) == 0:
        print('No images found')
        exit(0)
    else:
        files = os.listdir(directory)
        for i, filename in enumerate(files):
            files[i] = directory + '/' + filename

        size = check_image_sizes(files)
        num_files = len(files)
        # files_left = num_files
        length = 6
        if num_files < length:
            length = num_files
        final_size = (length * size[0], math.ceil(num_files / 6) * size[1])
        print('Final image size:', final_size[0], 'x', final_size[1])
        final_image = Image.new('RGBA', final_size, (255, 255, 255, 0))

        x = 0
        y = 0
        for file in files:
            image = Image.open(file)
            final_image.paste(image, ((size[0] * x), y * size[1]))
            x += 1
            if x >= length:
                x = 0
                y += 1

        # final_image.show()
        final_image.save(directory + "/spritesheet.png", 'PNG')
        print('Spritesheet saved at ' + directory + "/spritesheet.png")
        print('\nSprite stats:\n' +
              '\tWidth: ' + str(size[0]) + '\n' +
              '\tHeight: ' + str(size[1]) + '\n' +
              '\tFrames: ' + str(num_files) + '\n')


def check_image_sizes(files):
    if len(files) == 0:
        print('No images found')
        exit(0)
    else:
        img_size = Image.open(files[0]).size
        for file in files:
            img = Image.open(file)
            if img.size != img_size:
                print('Image size mismatch')
                exit(0)
        print('Image size match')
        return img_size
