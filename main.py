"""
version: 17 jan 22
lestudio media tools
"""


def create_output():
    from os import mkdir
    global OUTPUT_PATH

    try:
        mkdir(OUTPUT_PATH)
    except FileExistsError:
        print('there is already output directory')


def get_img_files():
    from os import listdir
    img_ext = ['.png', '.jpg', '.bmp']

    return list(filter(lambda x: x[-4:] in img_ext, listdir()))


def get_new_height(original_width, original_height):
    global NEW_WIDTH
    return (NEW_WIDTH * original_height) / original_width


def get_img_width_and_height(img_path):
    import cv2
    img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

    height = img.shape[0]
    width = img.shape[1]

    return width, height


def img_processing(img_path):
    import os
    from PIL import Image
    global slug
    global OUTPUT_PATH
    global NEW_WIDTH

    w, h = get_img_width_and_height(img_path)
    new_h = get_new_height(w, h)

    try:
        img = Image.open(img_path)
        img_resize = img.resize((NEW_WIDTH, int(new_h)))
        title, ext = os.path.splitext(img_path)
        img_resize.save(f'{OUTPUT_PATH}/' + title + f' {slug}' + ext)
    except OSError as e:
        raise e
    else:
        print(f'complete file {img_path}')


NEW_WIDTH = 640
OUTPUT_PATH = './output'

slug = input('what is your slug: ')
create_output()
imgs = get_img_files()

for img in imgs:
    try:
        img_processing(img)
    except Exception as e:
        print(f'{img} has Except')
        print(e)
        break

print('Finish all of work')
