import json

data= {'name':'Vinay','age':'31'}

json_string = json.dumps(data)

print json_string

#its string not dictionary
print type(json_string)