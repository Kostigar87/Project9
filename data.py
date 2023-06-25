headers_kit = {
    "Content-Type": "application/json",
    "Authorization": "Bearer cb67719a-c83b-4275-82ae-091c10029f0f"
}

headers_us = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Анатолий",
    "phone": "+79995553322",
    "address": "г. Москва, ул. Пушкина, д. 10"
}

kit_body = { "name": "1"}
'''
import create_new_user
headers_kit = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + create_new_user.token
}'''
