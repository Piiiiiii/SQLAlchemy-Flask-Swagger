from flask import request

from app.api_docs.v1 import campaign as api_doc
from app.libs.error_code import Success
from app.libs.redprint import RedPrint
from app.models.campaign import Campaign
from app.validators.forms import PaginateValidator

api = RedPrint(name='campaign', description='广告Campaign', api_doc=api_doc)


@api.route('/get_campaigns', methods=['GET'])
@api.doc()
def get_campaigns():
    # user_id = request.values.get('user_id')
    # token = request.values.get('token')
    validator = PaginateValidator().validate_for_api()
    page_number = validator.page.data
    items_per_page = validator.size.data
    paging_orders = Campaign.get_campaigns(
        page=page_number,
        size=items_per_page
    )

    return Success(paging_orders)


@api.route('/create_campaign', methods=['POST'])
@api.doc()
def create_campaign():
    request_body = request.get_json()
    user_id = request_body['user_id']
    campaign_id = request_body['campaign_id']
    campaign_name = request_body['campaign_name']
    campaign_obj_type = request_body['campaign_obj_type']
    campaign_time_start = request_body['campaign_time_start']
    campaign_time_end = request_body['campaign_time_end']
    linked_user = Campaign.create_campaign(
        user_id=user_id,
        campaign_id=campaign_id,
        campaign_name=campaign_name,
        campaign_obj_type=campaign_obj_type,
        campaign_time_start=campaign_time_start,
        campaign_time_end=campaign_time_end)
    return Success(linked_user)


@api.route('/test')
@api.doc()
def test():
    page_number = int(request.values.get('page_number'))
    # return 'test'
    return str(page_number)

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
