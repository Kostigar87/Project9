import data
import configuration
import requests

def create_user_for_test(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json=body,
                        headers=data.headers_us)
response = create_user_for_test(data.user_body);



token = response.json()['authToken']
print(token)

def kit_create(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers={"Content-Type": "application/json", "Authorization": "Bearer " + "token"})
response_kit_create = kit_create(data.kit_body)
print(response_kit_create.status_code)
print(response_kit_create.json())