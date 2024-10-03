from flask import Blueprint, render_template
from PIL import Image
import os
import operations as o

main = Blueprint('main', __name__, static_folder='static', template_folder='templates')


@main.route('/')
def home():
    portraits = []
    landscapes = []

    path = 'static/images/Illustrations/'
    details = o.image_details(path)
    for d in details:
        orientation = d[3]
        if orientation == 'portrait':
            portraits.append(d[0])
        else:
            landscapes.append(d[0])
    # details.sort()
    # print(details)

    return render_template('index.html', portraits=portraits, landscapes=landscapes)
