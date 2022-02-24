from unicodedata import name


class Room():
    def __init__(self, room_name, room_description):
        self.room_name = room_name 
        self.description = room_description

    def get_name(self): 
        return self.room_name
        
    def get_description(self):
        return self.description
        