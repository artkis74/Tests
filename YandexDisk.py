import requests

with open('token_yandex.txt', 'r') as file:
    token_disk = file.readline().strip()

class YandexDisk:
    def __init__(self, token=token_disk):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Accept': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def create_new_folder(self, disk_file_path='Новая папка'):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": disk_file_path}
        response = requests.put(url, headers=headers, params=params)
        response.raise_for_status()
        return response.status_code

    def delete_folder(self, disk_file_path='Новая папка'):
        url = f'https://cloud-api.yandex.net/v1/disk/resources'
        params = {'path': disk_file_path, 'permanently': True}
        headers = self.get_headers()
        response = requests.delete(url, headers=headers, params=params)
        return response.status_code
