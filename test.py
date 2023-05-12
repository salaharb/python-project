import json
def getData() : 
    with open('example.json') as file :
    # Load the JSON data
        data = json.load(file)
        return data



user = {
    'user': getData(),
    'setUser': lambda data: user.update({'user': data})
}

user_list = user.get('user')
set_user_func = user.get('setUser')
print(user_list)

set_user_func([5])

print(user['user'])