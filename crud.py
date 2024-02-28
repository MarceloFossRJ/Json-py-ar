# json format:
# {
#   "<table name>" : [
#     { "id": integer, - a unique id as an integer
#       "field_name_1": "a name",
#       "field_name_2": "a name",
# ...
#       "field_name_n": "a name"
#      },
#      { ....
# file name format should be: tableNmae + "_db.json"
import json

product1 = {'type': 'mobile phone', 'brand': 'Apple', 'model': 'IPhone14'}
product2 = {'type': 'mobile phone', 'brand': 'Samsung', 'model': 'Galaxy 20'}
product3 = {'type': 'mobile phone', 'brand': 'Google', 'model': 'Pixel 7'}


def getDataFromJsonFile(_tableName):
    with open(_tableName + "_db.json", "r") as connect:
        return json.load(connect)
    # do error handling


def setDataTomJsonFile(_tableName, _data):
    with open(_tableName + "_db.json", "w") as connect:
        json.dump(_data, connect)
        return True
    # do error handling


def getMaxId(_tableName):
    data = getDataFormJsonFile(_tableName)
    _id = 0
    for d in data[_tableName]:
        if d['id'] > _id:
            _id = _id

    _id = _id + 1
    return _id
    # do error handling


def create(_tableName, _dictionaryFields ):
    _dictionaryFields['id'] = getMaxId(_tableName)
    # add check to see if id field is present

    data = getDataFromJsonFile(_tableName)
    data[_tableName].append(_dictionaryFields)

    if setDataTomJsonFile(_tableName, data):
        print("Cool!")
        return True
    else:
        print("Ihhhhhhh :(")
        return False

