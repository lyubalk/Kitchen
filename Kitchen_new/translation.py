def selection_translation(user_input):  # функция для перевода выбора
    selection_dict = {'yes': 'да',  # словарь переводов
                      'да': 'да',
                      'no': 'нет',
                      'нет': 'нет'}
    key_selection = selection_dict.get(user_input)  # выбор по ключу
    return key_selection


def digit_translation(user_input):  # функция для перевода выбора
    selection_dict = {1: 'суп',  # словарь переводов
                      2: 'второе блюдо',
                      3: 'салат'}
    key_selection = selection_dict.get(user_input)  # выбор по ключу
    return key_selection
