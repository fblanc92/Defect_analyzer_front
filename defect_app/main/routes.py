from flask import render_template, request, Blueprint
from Defect_analyzer_front.defect_app.models import Post
from Defect_analyzer_back.resources.config.configs_utils import get_current_config_json
from Defect_analyzer_front.defect_app.models import Coil_post

from flask import Flask, render_template, Response
from random import randint

import json

main = Blueprint('main', __name__)


@main.route("/data")
def chart_data(data=None):
    data_set = []
    for x in range(0, 12):
        y = randint(1, 12)
        data_set.append(y)
    data = {}
    data['set'] = data_set
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    # {"set": [9, 9, 12, 6, 9, 8, 7, 10, 2, 5, 2, 7]}
    return resp


@main.route("/")
@main.route("/home")
def home(data=None):
    page = request.args.get('page', 1, type=int)
    post_per_page = get_current_config_json()['config']['post_per_page']
    posts = Coil_post.query.order_by(Coil_post.date_posted.desc()).paginate(page=page, per_page=3)
    data = {}
    data['title'] = 'Chart'
    return render_template('home.html', data=data, posts=posts, title='Defect Analyzer')


@main.route('/about')
def about():
    return render_template('about.html', title='About')
