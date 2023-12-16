import vk_api
import os
from dotenv import load_dotenv

# 1) Берешь API  Вконтакта, и с помощью него и языка программирования python, надо автоматизировать поиск по имени и фамилии ID странички и выгрузку даты рождения если указан.
# 2) Загрузка списка друзей и групп указанного ID.


load_dotenv()

TOKEN = os.getenv('TOKEN')
session = vk_api.VkApi(token=TOKEN)


def get_user_friends(user_id):
    friends = session.method('friends.get', {'user_id': user_id, 'order': 'name'})
    with open('friends_list.txt', 'w', encoding='utf-8') as f:
        counter = 1
        for friend in friends['items']:
            user = session.method('users.get', {'user_ids': friend, 'fields': 'bdate'})
            if 'bdate' not in user[0]:
                f.write(f'{counter}. {user[0]["first_name"]} {user[0]["last_name"]}\n')
            else:
                f.write(f'{counter}. {user[0]["first_name"]} {user[0]["last_name"]} {user[0]["bdate"]}\n')
            counter += 1
    print('Список друзей успешно загружен.')


def get_user_groups(user_id):
    groups = session.method('groups.get', {'user_id': user_id, 'extended': 1})
    with open('groups_list.txt', 'w', encoding='utf-8') as f:
        counter = 1
        for group in groups['items']:
            f.write(f'{counter}. ID: {group["id"]}; NAME: {group["name"]}\n')
            counter += 1
    print('Список групп успешно загружен.')

    
def get_search_users(first_name, last_name):
    users = session.method('search.getHints', {'q': f'{first_name} {last_name}', 'search_global': '1'})
    with open('users_list.txt', 'w', encoding='utf-8') as f:
        counter = 1
        for user in users['items']:
            if user['type'] == 'profile':
                user_id = user["profile"]["id"]
                user = session.method('users.get', {'user_ids': user_id, 'fields': 'bdate'})
                if 'bdate' not in user[0]:
                    f.write(f'{counter}. {user_id} {user[0]["first_name"]} {user[0]["last_name"]}\n')
                else:
                    f.write(f'{counter}. {user_id} {user[0]["first_name"]} {user[0]["last_name"]} {user[0]["bdate"]}\n')
                counter += 1


get_search_users('Рустам', 'Насибулин')
get_user_friends(278293127)  # Указываем выбранный нами ID
get_user_groups(278293127)   # Указываем выбранный нами ID