import re
import requests


class Api:
    def __init__(self):
        self.base_url = "https://api.stage.onevillage.io"
        self.headers = None

    def login(self, email, passwd):
        url = self.base_url + "/user/sign-in/"
        valid_data = {
            "email": email,
            "password": passwd
        }
        response = requests.post(url, json=valid_data)
        assert response.status_code == 200, f"received status code {response.status_code} is not 200"
        json_response = response.json()
        token = json_response["access_token"]
        self.headers = {
            "Authorization": "Token %s" % token
        }

    def check_user_exist(self, email):
        url = self.base_url + "/user/"
        response = requests.get(url, headers=self.headers)
        json_response = response.json()
        result = re.sub(r'\+.+@', '@', json_response["email"])
        email = re.sub(r'\+.+@', '@', email)
        assert result == email

    def reset_password(self, email):
        url = self.base_url + "/user/password/reset/"
        valid_data = {
            "email": email
        }
        response = requests.post(url, json=valid_data)
        assert response.status_code == 200, f"received status code {response.status_code} is not 200"

    def logout(self):
        url = self.base_url + "/user/sign-out/"
        response = requests.delete(url, headers=self.headers)
        assert response.status_code == 204, f"received status code {response.status_code} is not 204"


# usr = Api()
# usr.login("dina@onevillage.io", "1234567890_OV")
# usr.check_user_exist("dina@onevillage.io")
# usr.reset_password("dina@onevillage.io")
# usr.logout()
