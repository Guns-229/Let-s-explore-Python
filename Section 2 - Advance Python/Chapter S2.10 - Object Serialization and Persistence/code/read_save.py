import pickle
 
users = [{
    "name": "Vijay",
    "age": 53,
    "section": "R&D",
    "keywords": ["test", "testing", "tested"]
},{
    "name": "Deenanath",
    "age": 29,
    "section": "HR",
    "keywords": ["test", "testing", "tested"]
}]

with open ('users.pickle','wb') as f:
    pickle.dump(users,f)

with open ('users.pickle', 'rb') as f:
    data = pickle.load(f)

print (data)
print(type(data))
