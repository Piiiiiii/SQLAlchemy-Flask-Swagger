from flask import request

from app.api_docs.v1 import campaign as api_doc
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.user import User
from app.validators.forms import PaginateValidator

api = RedPrint(name='user', description='User', api_doc=api_doc)


@api.route('/create_user', methods=['GET'])
@api.doc()
def create_user():
    user_id = request.values.get('user_id')
    message = User.create_user(user_id=user_id)
    return message

    #
    # try:
    #     cur.execute(
    #         "SELECT campaign_name, campaign_obj_type, campaign_timeline, campaign_core_metric FROM "
    #         + new_table_name
    #         + " WHERE user_id = %s AND token = %s LIMIT %s;",
    #         (user_id, token, items_per_page * page_number),
    #     )
    #     # conn.commit()
    #     select_list = cur.fetchall()
    #     response_list = []
    #     for i in range(len(select_list)):
    #         temp_tuple = select_list[i]
    #         temp_dict = {
    #             "campaign_name": temp_tuple[0],
    #             "campaign_obj_type": temp_tuple[1],
    #             # Uncomment when these data are not None
    #             # "campaign_time_start": temp_tuple[2][0],
    #             # "campaign_time_end": temp_tuple[2][1],
    #             # "campaign_core_metric": {
    #             #     "type": temp_tuple[3][0],
    #             #     "value": temp_tuple[3][1]
    #             # }
    #         }
    #         response_list.append(temp_dict)
    #     res_dict = {"response_body": response_list}
    #     return jsonify(res_dict)
    #
    # except psycopg2.Error as error:
    #     # conn.rollback()
    #     return "error: {}".format(str(error))
    # except AttributeError as error:
    #     return "error: no connection"
    # except TypeError as error:
    #     return "error: {}".format(str(error))
