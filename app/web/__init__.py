# _*_ coding: utf-8 _*_
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import auth
