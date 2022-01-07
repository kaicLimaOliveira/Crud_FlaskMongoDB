from flask import Blueprint, request
from controllers.PagesControllers import Pages

pages = Blueprint('pages', __name__, url_prefix='/')

@pages.route('', methods=['GET'])
def index():
    return Pages().index(request)

@pages.route('new_user', methods=['GET', 'POST'])
def new_user():
    return Pages().new_user(request)

@pages.route('edit_user', methods=['GET', 'POST'])
def edit_user():
    return Pages().edit_user(request)

@pages.route('delete_user/<idx>', methods=['GET'])
def delete_user(idx):
    return Pages().delete_user(request, idx)