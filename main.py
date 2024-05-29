import os
import sys

from sheet_generator import parse_images

if __name__ == '__main__':
    if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
        directory = sys.argv[1]
        print(directory)
        print(os.listdir(directory))
        res = input('Is this the correct order? For best results name the files 0001, 0002, etc. using a program like '
                    'Bulk Rename Utility.\nType y or n: ')
        if res == 'y':
            parse_images(directory)
