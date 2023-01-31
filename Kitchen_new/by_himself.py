from translation import selection_translation
from opening import read_json_file


def category_selection_1(json_name, json_name_1):
    titles = int(input(f'\nВведите номер блюда начиная с 0 >>> '))
    print(titles)
    composition = list(read_json_file(json_name).values())[titles]
    print(",".join(composition))  #
    recipe_selection = input('Вывести рецепт введите да или нет >>> ').lower()
    if selection_translation(recipe_selection) == 'да':  #
        recipe = list(read_json_file(json_name_1).values())[titles]
        recipe = ", ".join(recipe)
        return recipe  #


def random_dish_1(user_input):
    if user_input == 'суп':
        file_selection = category_selection_1("Kitchen_new/soup/soup_composition.json",
                                              "Kitchen_new/soup/soup_recipe.json")
    elif user_input == 'второе блюдо':
        file_selection = category_selection_1("Kitchen_new/second/second_course_composition.json",
                                              "Kitchen_new/second/second_course_recipe.json")
    else:
        file_selection = category_selection_1("Kitchen_new/salad/salad_composition.json",
                                              "Kitchen_new/salad/salad_recipe.json")
    return file_selection
