from app.api.v1 import campaign
from app.libs.blueprint import Blueprint

redprint_list = [campaign]
blueprint_v1 = Blueprint('v1', __name__, redprint_list).register_redprint()
