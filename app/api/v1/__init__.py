from app.api.v1 import campaign, user, editorial_topic, tag, article
from app.libs.blueprint import Blueprint

redprint_list = [campaign, user, editorial_topic, tag, article]
blueprint_v1 = Blueprint('v1', __name__, redprint_list).register_redprint()
