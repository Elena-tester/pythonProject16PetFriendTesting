from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в тезультате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets' либо '' """

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age='4', pet_photo='images/cat1.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_successful_update_type_self_pet_info(name='Мурзик', animal_type='TYUIO', age=5):
    # записывает новый тип животных

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['animal_type'] == animal_type
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_successful_update_age_self_pet_info(name='Мурзик', animal_type='Котэ', age=0):
     # записывет с возрастом 0

     # Получаем ключ auth_key и список своих питомцев
     _, auth_key = pf.get_api_key(valid_email, valid_password)
     _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

     # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
     if len(my_pets['pets']) > 0:
         status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

         # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
         assert status == 200
         assert result['age'] == str(age)
     else:
         # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
         raise Exception("There is no my pets")

def test_successful_update_animal_type_large_self_pet_info(name='Мурзик', animal_type='gjkvnrkjjgnrjfjnbjfnbijNBRDNBJRJDNRGJJDNGVPJOJOERDNMVOMRSRGIURHGUIREHGIUTEHJGIURJgoijogijreoihijreuihjapjhrikjngjgRMGROIRMGOMFOIPIMHBOFGMNBOIGFMONITHMGTFOIMTHIOHGMBOIGFMBOISGMHBOI,HB,HB,FH,HBH,GOHB,TMHOITMHITMHIMSHIOMTIOHMAOBOIIFMHBFOIMBIOARMGIORJGRFNAGUIEFYEHGYVEBVABeyGRGEYGFBYEUDBFDHYBFHEJ12ппы45egjn59girnb5hw958ghirhngh85gh', age=5):
    # ошибка, в колличестве введенных символов
    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['animal_type'] == animal_type
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

def test_successful_update_age_letters_self_pet_info(name='Мурзик', animal_type='Котэ', age='неизвестный возраст'):
    # ошибка, в возрасте не может быть букв, символов

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['age'] == age
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

# #_negative_update
#
def test_negative_update_name_self_pet_info(name="", animal_type='Котэ', age=5):
   # ошибка, не может быть пустого имени

   # Получаем ключ auth_key и список своих питомцев
   _, auth_key = pf.get_api_key(valid_email, valid_password)
   _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

   # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
   if len(my_pets['pets']) > 0:
       status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

       # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
       assert status == 200
       assert result['name'] != name
   else:
       # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
       raise Exception("There is no my pets")
#
def test_negative_update_age_large_self_pet_info(name='Мурзик', animal_type='Котэ', age=100000):
     # ошибка, большое значение в возрасте
     # Получаем ключ auth_key и список своих питомцев
     _, auth_key = pf.get_api_key(valid_email, valid_password)
     _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

     # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
     if len(my_pets['pets']) > 0:
         status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

         # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
         assert status == 200
         assert result['age'] != age
     else:
         # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
         raise Exception("There is no my pets")
# #
def test_negative_update_name_digit_self_pet_info(name=1234, animal_type='Котэ', age=5):
    # ошибка, в имени не может быть цифр

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] != name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")
#
#
def test_negative_update_self_empty_pet_info(name="" , animal_type="" , age="" ):
    # ошибка, не может быть пустых значений
#  # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] != name
        assert result['animal_type'] != animal_type
        assert result['age'] != age
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

#
# def test_negative_update_age_minus_self_pet_info(name='Мурзик', animal_type='Котэ', age=-1):
#     #ошибка, возраст не может быть со знаком "-"
#     # Получаем ключ auth_key и список своих питомцев
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
#
#     # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
#     if len(my_pets['pets']) > 0:
#         status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
#
#         # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
#         assert status == 200
#         assert result['age'] != str(age)
#     else:
#         # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
#         raise Exception("There is no my pets")
#
def test_negative_update_age_float_self_pet_info(name='Мурзик', animal_type='Котэ', age=2.45):
    # ошибка, возраст может быть только целое число

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Еслди список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['age'] != age
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("There is no my pets")

#update_self_pet_photo
# def test_successful_update_self_pet_photo(pet_photo='images/cat2.jpg'):
#     # ошибка обновления фото
#     # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
#     pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
#
#     # Запрашиваем ключ api и сохраняем в переменую auth_key
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#     _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
#
#     if len(my_pets['pets']) > 0:
#
#         status, result = pf.update_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)
#
#         # Проверяем что статус ответа = 200 и фото питомца соответствует заданному
#         assert status == 200 #но получаем статус 503
#         assert result['photo'] == pet_photo
#     else:
#         # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
#         raise Exception("There is no my pets")

# def test_negative_try_add_new_pet_with_invalid_data(name='', animal_type='', age=''):
#     """Проверяем что можно добавить питомца с корректными данными"""
#
#     # Запрашиваем ключ api и сохраняем в переменую auth_key
#     _, auth_key = pf.get_api_key(valid_email, valid_password)
#
#     # Добавляем питомца
#     status, result = pf.add_new_simple_pet(auth_key, name, animal_type, age)
#
#     # Сверяем полученный ответ с ожидаемым результатом
#     assert status == 200 #404
#     assert result['name'] != name
#     assert result['animal_type'] != animal_type
#     assert result['age'] != age

def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()

def test_negative_get_api_key_for_invalid_user(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 и в результате не содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, "invalid " + password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200
    assert status == 403
    assert not ('key' in result)