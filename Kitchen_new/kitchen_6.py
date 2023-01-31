import random
from Kitchen_new.by_chance import random_dish
from Kitchen_new.by_himself import random_dish_1
from Kitchen_new.translation import digit_translation, selection_translation
from Kitchen_new.opening import json_key, read_json_file


def random_selection():
    selection = input('Вы хотите выбрать случайно введите да или нет >>> ').lower()

    if selection_translation(selection) == 'да':
        random_key = random.choice(json_key("Kitchen_new/titles.json"))
        dish_by_key = random_dish(random_key)
        print(dish_by_key)

    elif selection_translation(selection) == 'нет':
        random_key = json_key("Kitchen_new/titles.json")
        print(", ".join(random_key))
        new_selection = int(input(f'Введите номер категории >>> '))
        category = input('Вы хотите выбрать блюдо случайно или самостоятельно введите да или нет >>> ').lower()
        digit = digit_translation(new_selection)

        if selection_translation(category) == 'да':
            random_dish_name = random_dish(digit)
            print(random_dish_name)
        else:
            list_of_dishes = read_json_file("Kitchen_new/titles.json")[digit]
            print(", ".join(list_of_dishes))
            selected_dish = random_dish_1(digit)
            print(selected_dish)

    else:
        while True:
            again = input('Запустить заново введите да или нет >>> ').lower()
            if selection_translation(again) == 'да':  #
                random_selection()
            else:
                break


random_selection()
