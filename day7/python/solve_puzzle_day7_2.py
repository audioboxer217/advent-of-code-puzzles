''' Sort program tower '''

import re

APP_DICT = {}
UNBALANCED = {}

def add_to_dict(item):
    ''' Add one item to a dictionary '''

    regex = re.compile(r'(\w*) (\((\d*)\))(.*)')
    matches = regex.match(item)

    app_name = matches.group(1)
    app_weight = matches.group(3)
    sub_apps = matches.group(4)

    if app_name not in APP_DICT:
        APP_DICT[app_name] = {'parent': '',
                              'weight': 0,
                              'sub_apps': []}
    APP_DICT[app_name]["weight"] = app_weight

    if sub_apps:
        sub_regex = re.compile(r'( -> )(\w.*)')
        sub_apps = sub_regex.match(sub_apps).group(2).split(', ')
        for sub_app in sub_apps:
            if sub_app not in APP_DICT:
                APP_DICT[sub_app] = {'parent': '',
                                     'weight': 0,
                                     'sub_apps': []}
            APP_DICT[sub_app]['parent'] = app_name
            APP_DICT[app_name]["sub_apps"].append(sub_app)

def find_bottom():
    ''' Find the bottom of the app tree '''

    bottom = ''
    for key, value in APP_DICT.items():
        if value["parent"] == "":
            bottom = key
            return bottom

def calculate_tree_weight(app_name):
    ''' Calculates the total tree weight '''
    weight = int(APP_DICT[app_name]["weight"])
    for sub_app in  APP_DICT[app_name]["sub_apps"]:
        weight += calculate_tree_weight(sub_app)
    return weight

def find_imbalance(app_name):
    ''' Iterates through the dictionary to find the imbalance '''
    global UNBALANCED

    sub_app_weights = []
    for sub_app in APP_DICT[app_name]["sub_apps"]:
        sub_app_weights.append(calculate_tree_weight(sub_app))
    occurrences = []
    if len(sub_app_weights) > 0:
        for sub_app_weight in sub_app_weights:
            occurrences.append(sub_app_weights.count(sub_app_weight))
        if min(occurrences) != max(occurrences):
            unbalanced_app = APP_DICT[app_name]["sub_apps"][occurrences.index(min(occurrences))]
            UNBALANCED = [unbalanced_app, sub_app_weights]
            find_imbalance(unbalanced_app)

def main():
    ''' Sort program tower '''

    with open("../puzzle_input.txt") as file:
        for line in file:
            add_to_dict(line)
    bottom = find_bottom()

    find_imbalance(bottom)

    unbalanced_app_weight = int(APP_DICT[UNBALANCED[0]]["weight"])
    unbalanced_weights = list(map(int, UNBALANCED[1]))
    top_weight = max(unbalanced_weights)
    bottom_weight = min(unbalanced_weights)

    answer = unbalanced_app_weight - (top_weight - bottom_weight)

    print(answer)

if __name__ == '__main__':
    main()
    