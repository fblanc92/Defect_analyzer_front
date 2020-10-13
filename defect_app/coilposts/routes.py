from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from Defect_analyzer_front.defect_app import db
from Defect_analyzer_front.defect_app.models import Coil_post
from flask import Flask, render_template, Response
from random import randint
import time
import json

coilposts_blueprint = Blueprint('coilposts_blueprint', __name__)


# @coilposts_blueprint.route("/data")
# def chart_data(data=None):
#     data_set = []
#
#     for x in range(0, 12):
#         y = randint(1, 12)
#         data_set.append(y)
#
#     data = {}
#
#     data['set'] = data_set
#
#     js = json.dumps(data)
#
#     resp = Response(js, status=200, mimetype='application/json')
#
#     return resp
#
#
# @coilposts_blueprint.route("/post/<int:post_id>")
# def post(post_id, data=None):
#     data = {}
#
#     data['title'] = 'Chart'
#
#     return render_template('index.html', data=data)



@coilposts_blueprint.route("/post/<int:post_id>")
def post(post_id):
    post = Coil_post.query.get_or_404(post_id)
    areas_dict = eval(post.areas)
    return render_template('coilpost.html', title=post.coil_id, post=post, **areas_dict)

