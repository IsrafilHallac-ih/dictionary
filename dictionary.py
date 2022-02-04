platess={"key" : "value"}
plates={"artvin" : 8,"rize" : 53}
print(plates["rize"])

#yeni değer ekleme değiştirme yapılabiliyor.
plates["yozgat"]=66
print(plates)

user={
    "israfil":{
        "age":35,
        "roles":["admin"],
        "email":"i@gmail.com",
        "address":"bursa",
        "phone":"1234566"
        },
    "sezgin":{
        "age":33,
        "roles":["admin","users"],
        "email":"s@gmail.com",
        "address":"samsun",
        "phone":"1234566"
        }
}

print(user["sezgin"]["roles"][1])