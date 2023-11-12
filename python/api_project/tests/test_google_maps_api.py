"""PyTest cheking (python -m pytest -s -v from console)"""

import json
from utils.api import Google_maps_api
from utils.cheking import Cheking

"""Create, change and delete new location"""

class Test_create_place():

    def test_create_new_place(self):
        print("POST method")
        result_post = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Cheking.check_status_code(result_post, result_post.status_code)
        token = json.loads(result_post.text)
        Cheking.check_json_token(result_post, list(token))
        Cheking.check_json_value(result_post, "status", "OK")

        print("GET method old")
        result_get = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, result_get.status_code)
        token = json.loads(result_get.text)
        Cheking.check_json_token(result_get, list(token))
        Cheking.check_json_value(result_get, "address", "29, side layout, cohen 09")

        print("PUT method")
        result_put = Google_maps_api.put_new_place(place_id)
        Cheking.check_status_code(result_put, result_put.status_code)
        token = json.loads(result_put.text)
        Cheking.check_json_token(result_put, list(token))
        Cheking.check_json_value(result_put, "msg", "Address successfully updated")

        print("GET method new")
        result_get = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, result_get.status_code)
        token = json.loads(result_get.text)
        Cheking.check_json_token(result_get, list(token))
        Cheking.check_json_value(result_get, "address", "100 Lenina street, RU")

        print("DELETE method")
        result_delete = Google_maps_api.delete_new_place(place_id)
        Cheking.check_status_code(result_delete, result_delete.status_code)
        token = json.loads(result_delete.text)
        Cheking.check_json_token(result_delete, list(token))
        Cheking.check_json_value(result_delete, "status", "OK")

        print("GET method after delete")
        result_get = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, result_get.status_code)
        token = json.loads(result_get.text)
        Cheking.check_json_token(result_get, list(token))
        Cheking.check_json_value(result_get, "msg", "Get operation failed, looks like place_id  doesn't exists")

        print("Create, change and delete new location successfuly")