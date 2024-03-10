import json
# import premierliga.json as json_table

with open('premierliga.json', 'r', encoding='utf-8') as json_table:
    print(json_table)
    rpl_table = json.load(json_table)
    print(rpl_table)
