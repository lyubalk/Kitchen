import random
from translation import selection_translation
from opening import read_json_file, read_file


def category_selection(file_name, json_name, json_name_1):  #
    titles = random.choice(read_file(file_name)).replace('\n', '')  #
    composition = read_json_file(json_name)
    composition_key = composition[titles]
    print(f'{titles}, \n{", ".join(composition_key)}')  #
    recipe_selection = input('Вывести рецепт введите да или нет >>> ').lower()
    if selection_translation(recipe_selection) == 'да':  #
        recipe = read_json_file(json_name_1)  #
        recipe_key = recipe[titles]
        return ", ".join(recipe_key)  #


def random_dish(user_input):
    if user_input == 'суп':
        file_selection = category_selection("Kitchen_new/soup/soup_titles.txt",
                                            "Kitchen_new/soup/soup_composition.json",
                                            "Kitchen_new/soup/soup_recipe.json")
    elif user_input == 'второе блюдо':
        file_selection = category_selection('Kitchen_new/second/second_course_titles.txt',
                                            "Kitchen_new/second/second_course_composition.json",
                                            "Kitchen_new/second/second_course_recipe.json")
    else:
        file_selection = category_selection('Kitchen_new/salad/salad_titles.txt',
                                            "Kitchen_new/salad/salad_composition.json",
                                            "Kitchen_new/salad/salad_recipe.json")
    return file_selection
