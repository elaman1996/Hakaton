import requests
import json

# requests.get('asdfghjk')

HOST = 'http://3.67.196.232/'

def get_all_todos(url) -> str:
    response = requests.get(url + 'todo/all')
    if response.status_code == 200:
        return json.loads(response.text)
    raise Exception('Сервер упал')

# print(get_all_todos(HOST))
def create_todo(url, data: dict) -> None:
    response = requests.post(url + 'todo/create', data=json.dumps(data))
    if response.status_code == 200:
        return 1
    return 0





todo = {
    'title': 'Эламан',
    'is_done': False
}
# print(create_todo(HOST, todo))
# print(get_all_todos(HOST))

def retrieve_todo(url, id_: int) -> None:
    response = requests.get(url + f'todo/{id_}')
    if response.status_code == 200:
        print(dir(requests))
        return json.loads(response.text)
    elif response.status_code == 404:
        raise Exception('Нет такой записи')
    raise Exception('Непредвиденная ошибка')

# print(retrieve_todo(HOST, 10)) # {'id': 10, 'title': 'Тима', 'is_done': False, 'date_posted': '2023-02-14'}

def delete_todo(url, id_: int) -> None:
    response = requests.delete(url + f'todo/{id_}/delete')
    if response.status_code == 200:
        return json.loads(response.text)
    elif response.status_code == 404:
        raise Exception('Нет токой записи')
    raise Exception('Непредвиденная ошибка')


# print(delete_todo(HOST, 19))
# print(retrieve_todo(HOST, 19))

def update_todo(url, id_: int) -> None:
    response = requests.get(url + f'todo/{id_}')
    if response.status_code == 200:
        dict_= json.loads(response.text)
        dict_['title'] = input('New title: ')
        dict_['is_done'] = input('Input True or False: ').lower().strip()
        if dict_['is_done'] == 'true':
                boolValue = True
        elif dict_['is_done'] == 'false':
                boolValue = False
        else:
            print('Error: Input must be True or False')
        json_obj = json.dumps(dict_)
        requests.put(url + f'todo/{id_}/update', json_obj)
        return requests.get(url + f'todo/{id_}').text
    elif response.status_code == 404:
        raise Exception('Не найдена')
    raise Exception('Непредвиденная ошибка')

# print(update_todo(HOST, 34))
# print(retrieve_todo(HOST, 9))

# TODO: Написать функция для обновления todo и удаления todo
# TODO: переписать на классы

while True: 
    action = input( 'Что вы хотите сделать? ')
    if action == 'read':
        print(get_all_todos(HOST))
    elif action =='delete':
        delete_todo(HOST, input('Введите id товара: '))
        print('Успешно удалено')
    elif action == 'update':
        update_todo(HOST, int(input('Введит id товара: ')))
        print('Успешно обновлено')
    elif action == 'create':
        create_todo(HOST, input('Введит название : '))
        print('Успешно создано')
    elif action == '':
            break
    else:
        print('Нет такого действия!')