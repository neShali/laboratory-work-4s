import json
import yaml

def convert_file (json_file, yaml_file):    

    with open(json_file,'r', encoding='utf-8') as f:
       s = f.readlines()
       data = json.loads("".join(s))

    with open(yaml_file, 'w', encoding='utf-8') as yfile:
            yaml.dump(data, yfile, allow_unicode = True)


convert_file('people.json', 'people.yaml')
