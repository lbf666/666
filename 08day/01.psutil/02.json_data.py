import json


# json数据由列表和字典组成, 不能含有其他数据结构
data = {
    'cpu': [23.1, 0, 65.3, 11.6],
    'memory': {'usage': (74, 34), 'idle': 26}
}
print(data, type(data))
try:
    data_json = json.dumps(data)
except Exception as error:
    print(error)
print(data_json, type(data_json))
print(str(data))

with open(file='json_data.json', mode='w') as file:
    json.dump(data, file)

with open(file='json_data.json', mode='r') as file:
    data01 = json.load(file)
    print(data01, type(data01))
