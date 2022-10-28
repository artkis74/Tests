from YandexDisk import YandexDisk, token_disk


if __name__ == '__main__':
    YandexDisk = YandexDisk(token_disk)
    print(YandexDisk.create_new_folder('Test folder'))
    print(YandexDisk.delete_folder('Test folder'))
