import unittest
from unittest.mock import patch
from unittest import mock
from parameterized import parameterized
from work_with_docs import check_document_existance, get_doc_owner_name, get_all_doc_owners_names, show_all_docs_info,\
    get_doc_shelf, add_new_doc, delete_doc, add_new_shelf, documents
from YandexDisk import YandexDisk, token_disk

YandexDisk = YandexDisk(token_disk)

class TestFunctions(unittest.TestCase):


    """Тест команды, которая проверяет есть ли такой номер документа в каталоге"""
    def test_check_document_existance(self):
        result = check_document_existance('11-2')
        self.assertTrue(result)


    """Тест команды, которая спросит номер документа и выведет имя человека, которому он принадлежит"""
    @patch('builtins.input', return_value="2207 876234")
    def test_get_doc_owner_name(self, number):
        result = get_doc_owner_name()
        self.assertEqual(result, "Василий Гупкин")


    '''  Тест команды, которая выводит список всех владельцев документов'''
    def test_get_all_doc_owners_names(self):
        result = get_all_doc_owners_names()
        self.assertEqual(result, {'Геннадий Покемонов', 'Василий Гупкин', 'Аристарх Павлов'})


    '''  Тест команды, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"'''
    def test_show_all_docs_info(self):
        result = show_all_docs_info()
        self.assertEqual(result, ['passport "2207 876234" "Василий Гупкин"',
                                  'invoice "11-2" "Геннадий Покемонов"', 'insurance "10006" "Аристарх Павлов"'])


    '''Тест команды, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
    имя владельца и номер полки, на котором он будет храниться.'''
    def test_add_new_doc(self):
        shelf_number = 1000
        with mock.patch('builtins.input', side_effect=['777', 'Passport', 'Александр', 1000]):
            result = add_new_doc()
        self.assertEqual(shelf_number, result)

    '''Тест команды, которая спросит номер документа и удалит его из каталога и из перечня полок.'''
    @patch('builtins.input', return_value='11-2')
    def test_delete_doc(self, value):
        result = delete_doc()
        self.assertEqual(('11-2', True), result)


class test_yandex(unittest.TestCase):

    '''Тест функции, которая добавляет новую папку на Диск.'''
    def test_create_new_folder(self):
        result = YandexDisk.create_new_folder('Test folder')
        self.assertEqual(201, result)

    '''Тест функции, которая удаляет папку с Диска.'''
    def test_delete_folder(self):
        result = YandexDisk.delete_folder('Test folder')
        self.assertEqual(204, result)
