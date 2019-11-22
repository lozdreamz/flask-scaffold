from flask import Blueprint, render_template

from newapp.ext import db
from .models import User

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.pug')
