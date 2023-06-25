import data
import configuration
import requests

def create_user_for_test(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json=body,
                        headers=data.headers_us)
response = create_user_for_test(data.user_body);
print(response.json())