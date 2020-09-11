#User
#The id is meant to be the unchangeable aspect of one's account that can permanently identify someone without error
#The name might change depending on the platform, it's a human-readable way to identify your userbase as you input information into the script & read any output
class User:
    def __init__(self, _id, _username):
        self.id = _id
        self.username = _username

#Content
class Content:
    def __init__(self, _source_url, _folder_name, _encryption_password = ''):
        self.source_url = _source_url
        self.folder_name = _folder_name
        self.encryption_password = _encryption_password

