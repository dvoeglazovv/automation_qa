"""Requests cheking methods"""
import json


class Cheking():

    """Status-code checking method"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print("Success! Status-code = " + str(result.status_code))

    """Checking tokens in response method"""
    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value
        print("Success token")

    """Checking token values in response method"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " true")