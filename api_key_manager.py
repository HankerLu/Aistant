
from enum import Enum

class API_KEY_DECIDE_OWNER(Enum):
    API_OWNER_USER_SET = 0
    API_OWNER_ENV_PATH = 1
    API_OWNER_FILE_SAVE = 2
    API_OWNER_NOT_EXIST = 3
    API_OWNER_MAX_NUM = 4

class ApiKeyManager:
    def __init__(self):
        print("Init key manager.")
        self.api_key_owner = API_KEY_DECIDE_OWNER.API_OWNER_NOT_EXIST
    
    def api_key_display(self):
        print("api_key_display: ", self.api_key_owner)
    
    def api_key_update(self, new_owner_req):
        if new_owner_req <= self.api_key_owner:
            print("Update new api key: ", new_owner_req)
            self.api_key_owner = new_owner_req

    