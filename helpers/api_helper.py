# import requests
#
#
# class HelperApi:
#
#     def login(self, email, passwd):
#         url = "https://api.onevillage.io/user/sign-in/"
#         valid_data = {
#             "email": email,
#             "password": passwd
#         }
#         response = requests.post(url, json=valid_data)
#         assert response.status_code == 200, f"received status code {response.status_code} is not 200"
#         json_response = response.json()
#         token = json_response["access_token"]
#         headers = {
#             "Authorization": "Token %s" % token
#         }
#         return headers
