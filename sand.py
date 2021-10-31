import json

with open('sht_number.txt','r') as shot_file:
    sht_num = shot_file.read()

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

ds_dw = []

print(len(config['chord_%d' %1]['peaces']))
