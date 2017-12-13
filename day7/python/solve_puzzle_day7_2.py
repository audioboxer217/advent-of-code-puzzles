''' Sort program tower '''

import re

def add_to_dict(item, dictionary):
    ''' Add one item to a dictionary '''

    regex = re.compile(r'(\w*) (\((\d*)\))(.*)')
    matches = regex.match(item)

    app_name = matches.group(1)
    app_weight = matches.group(3)
    sub_apps = matches.group(4)

    if app_name not in dictionary:
        dictionary[app_name] = {'parent': '',
                                'weight': 0,
                                'sub_apps': []}
    dictionary[app_name]["weight"] = app_weight

    if sub_apps:
        sub_regex = re.compile(r'( -> )(\w.*)')
        sub_apps = sub_regex.match(sub_apps).group(2).split(', ')
        for sub_app in sub_apps:
            if sub_app not in dictionary:
                dictionary[sub_app] = {'parent': '',
                                       'weight': 0,
                                       'sub_apps': []}
            dictionary[sub_app]['parent'] = app_name
            dictionary[app_name]["sub_apps"].append(sub_app)

    return dictionary

def find_bottom(dictionary):
    ''' Find the bottom of the app tree '''

    bottom = ''
    for key, value in dictionary.items():
        if value["parent"] == "":
            bottom = key
            return bottom

def calculate_tree_weight(dictionary, app_name):
    ''' Calculates the total tree weight '''
    weight = int(dictionary[app_name]["weight"])
    for sub_app in  dictionary[app_name]["sub_apps"]:
        weight += calculate_tree_weight(dictionary, sub_app)
    return weight

def find_imbalance(dictionary, app_name):
    ''' Iterates through the dictionary to find the imbalance '''

    unbalanced = []
    sub_app_weights = []
    for sub_app in dictionary[app_name]["sub_apps"]:
        sub_app_weights.append(calculate_tree_weight(dictionary, sub_app))
    occurrences = []
    if len(sub_app_weights) > 0:
        for sub_app_weight in sub_app_weights:
            occurrences.append(sub_app_weights.count(sub_app_weight))
        if min(occurrences) != max(occurrences):
            unbalanced_app = dictionary[app_name]["sub_apps"][occurrences.index(min(occurrences))]
            unbalanced = [unbalanced_app, sub_app_weights]
            find_imbalance(dictionary, unbalanced_app)

    return unbalanced

def main():
    ''' Sort program tower '''

    app_dict = {}
    with open("../puzzle_input.txt") as file:
        for line in file:
            app_dict = add_to_dict(line, app_dict)

    bottom = find_bottom(app_dict)

    unbalanced = []
    while len(unbalanced) == 0:
        unbalanced = find_imbalance(app_dict, bottom)

    print(unbalanced)

    unbalanced_app_weight = int(app_dict[unbalanced[0]]["weight"])
    unbalanced_weights = list(map(int, unbalanced[1]))
    top_weight = max(unbalanced_weights)
    bottom_weight = min(unbalanced_weights)
    print(unbalanced_app_weight)
    print(top_weight)
    print(bottom_weight)
    answer = unbalanced_app_weight - (top_weight - bottom_weight)

    print(answer)

if __name__ == '__main__':
    main()
    