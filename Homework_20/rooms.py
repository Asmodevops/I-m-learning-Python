import json



def get_rooms():
    with open('rooms.json', encoding='utf-8') as rooms:
        rooms = json.load(rooms)
        return rooms['rooms']
    

def is_valid_room(rooms, choice):
    if choice in rooms:
        return rooms[choice]
    else:
        return False
    

def choice_room(rooms):
    for key, value in rooms.items():
        print(f'{key} - {value}')
    
    choice = input('Ваш выбор: ')
    room_type = is_valid_room(rooms, choice)
    if room_type == False:
        return False
    else:
        return room_type