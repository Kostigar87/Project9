import data
import configuration
import requests

def kit_create(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=data.headers_kit)
response_kit_create = kit_create(data.kit_body)
print(response_kit_create.status_code)
