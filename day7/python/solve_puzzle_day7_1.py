''' Sort program tower '''

import re

def add_to_dict(item, dictionary):
    ''' Add one item to a dictionary '''

    regex = re.compile(r'(\w*) (\((\d*)\))(.*)')
    matches = regex.match(item)

    app_name = matches.group(1)
    app_weight = matches.group(3)
    sub_apps = matches.group(4)

    if sub_apps:
        sub_regex = re.compile(r'( -> )(\w.*)')
        sub_apps = sub_regex.match(sub_apps).group(2)
        dictionary[app_name] = {'name': app_name, 'weight': app_weight, 'sub_apps': sub_apps}
    else:
        dictionary[app_name] = {'name': app_name, 'weight': app_weight}

    return dictionary

def order_dict(dictionary):
    ''' Order the dictionary '''
    remove_list = []
    for app_name in iter(dictionary):
        if 'sub_apps' in dictionary[app_name]:
            app = dictionary.get(app_name)
            sub_apps = app.get('sub_apps')
            for sub_app in sub_apps.split(", "):
                app[sub_app] = dictionary[sub_app]
                remove_list.append(dictionary[sub_app]['name'])
            del app["sub_apps"]
            dictionary[app_name] = app

    for sub_app in remove_list:
        del dictionary[sub_app]

    return dictionary

def main():
    ''' Sort program tower '''
    app_dict = {}
    with open("../puzzle_input.txt") as file:
        for line in file:
            app_dict = add_to_dict(line, app_dict)

    app_dict = order_dict(app_dict)
    app_keys = app_dict.keys()
    print("Bottom Program: %s" % next(iter(app_keys)))

if __name__ == '__main__':
    main()
    