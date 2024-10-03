import PIL
import os
from PIL import Image


# img = Image.open(r'static/images/Illustrations/animation_bg.jpg')
# filename = img.filename
# print(filename)


def compress_by_size():
    path = 'static/images/Illustrations/'

    for img in os.listdir(path):
        print(img)
        with Image.open(path + img) as image:
            image_height = image.height
            image_width = image.width
            h_w_ratio = image_height / image_width
            w_h_ratio = image_width / image_height
            # print(image_width)

            # If ratio is smaller than 1080x1920_____________________________
            if h_w_ratio >= 0.53125:  # If it is portrait
                if image_height > 980:
                    new_image_width = int(w_h_ratio * 980)
                    image = image.resize((new_image_width, 980))
                    image.save(path + img)
            else:
                if image.width > 1920:  # If it is landscape
                    new_image_height = int(h_w_ratio * 1920)
                    image = image.resize((1920, new_image_height))
                    image.save(path + img)

# compress_by_size()


def print_new_dimension():
    path = 'static/images/Illustrations/'
    for img in os.listdir(path):
        with Image.open(path + img) as image:
            image_height = image.height
            image_width = image.width
            print(img + ':')
            print(f'{image_width} x {image_height}')


def image_details(path):
    details = []
    if path[-1] != '/':
        path = path + '/'
    for f in os.listdir(path):
        new_path = path+f
        with Image.open(new_path, 'r') as img:
            img_height = img.height
            img_width = img.width
            h_w_ratio = img_height/img_width
            if h_w_ratio >= 0.53125:
                frame = 'portrait'
            else:
                frame = 'landscape'
            parameters = (new_path, img_width, img_height, frame)
            details.append(parameters)
    return details

# compress_by_size()
print_new_dimension()