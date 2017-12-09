''' Sort program tower '''

import re
import json

def add_to_dict(item, dictionary):
    ''' Add one item to a dictionary '''

    regex = re.compile(r'(\w*) (\((\d*)\))(.*)')
    matches = regex.match(item)

    app_name = matches.group(1)
    app_weight = matches.group(3)
    sub_apps = matches.group(4)

    if sub_apps:
        sub_regex = re.compile(r'( -> )(\w.*)')
        sub_apps = sub_regex.match(sub_apps).group(2).split(', ')
        dictionary[app_name] = {'name': app_name, 'weight': int(app_weight), 'sub_apps': sub_apps}
    else:
        dictionary[app_name] = {'name': app_name, 'weight': int(app_weight)}

    return dictionary

def order_dict(dictionary):
    ''' Order the dictionary '''
    remove_list = []
    for app_name in iter(dictionary):
        if 'sub_apps' in dictionary[app_name]:
            app = dictionary.get(app_name)
            sub_apps = app.get('sub_apps')
            index = 0
            for sub_app in sub_apps:
                app['sub_apps'][index] = dictionary[sub_app]
                app['sub_apps'][index]['parent'] = app_name
                if 'total_weight' in app:
                    app['total_weight'] += int(app['sub_apps'][index]['weight'])
                else:
                    app['total_weight'] = int(app['weight']) + int(app['sub_apps'][index]['weight'])
                remove_list.append(dictionary[sub_app]['name'])
                index += 1
            #del app["sub_apps"]
            dictionary[app_name] = app
    # Figure out how to add 'total_weight' to parent branches

    for sub_app in remove_list:
        del dictionary[sub_app]

    return dictionary

def find_imbalance(dictionary):
    ''' Iterates through the dictionary to find the imbalance '''

    weights = {}
    stack = []
    app_details = dictionary.items()
    while app_details:
        for key, val in app_details:
            if isinstance(val, dict):
                if val.get('parent'):
                    parent = val.get('parent')
                else:
                    parent = "Bottom"
                stack.append(val.items())
                continue
            elif isinstance(val, list):
                for sub_app in val:
                    if isinstance(sub_app, dict):
                        parent = sub_app.get('parent')
                        stack.append(sub_app.items())
                        continue
            elif key == 'weight':
                if parent in weights:
                    weights[parent]['total'] += int(val)
                    weights[parent]['weights'].append(val)
                else:
                    new_item = {'total': int(val), 'weights': [val]}
                    weights[parent] = new_item
                continue

        if len(stack) > 0:
            app_details = stack.pop()
        else: break

    return weights

def main():
    ''' Sort program tower '''
    app_dict = {}
    with open("../puzzle_input.txt") as file:
        for line in file:
            app_dict = add_to_dict(line, app_dict)

    app_dict = order_dict(app_dict)

    # weights = find_imbalance(app_dict)
    # print(weights)
    print(json.dumps(app_dict, indent=4, sort_keys=True))

if __name__ == '__main__':
    main()
    