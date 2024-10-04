from flask import Blueprint, render_template
from PIL import Image
import os
import operations as o

main = Blueprint('main', __name__, static_folder='static', template_folder='templates')


@main.route('/')
def home():
    # portraits = []
    # landscapes = []
    all_images = []

    path = 'static/images/Illustrations/'
    for f in os.listdir(path):
        full_path = path + f
        all_images.append(full_path)
    # details = o.image_details(path)
    # for d in details:
    #     orientation = d[3]
    #     if orientation == 'portrait':
    #         portraits.append(d[0])
    #     else:
    #         landscapes.append(d[0])
    #
    # for i in portraits:
    #     all_images.append(i)
    #
    # for j in landscapes:
    #     all_images.append(j)

    # details.sort()
    # print(details)

    return render_template('index.html', images=all_images)
