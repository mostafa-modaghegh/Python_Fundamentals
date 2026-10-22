#tuple

numbers = (3 , 5 , 8 , 17)
#تغییر ناپذیر
print(type(numbers))
print(numbers[2])

#set 

classmates = {"Shadan", "Mirza", "Abdollah","Abdollah"}
classmates.add("Hasan")
classmates.remove("Shadan")
print(type(classmates))
print(classmates)

#frozenset

cordinates = frozenset([3.4, 5.8 , 2.4, 2.4])
#cordinates.add(47)
print(type(cordinates))
print(cordinates)


#dict

edris = {  "name":"Edris",
         "age": 23,
         "city":"kapisa",
         "studentID":140411,
         "gender":"male"}

print(type(edris))
print(edris.items())
print(edris.keys())
print(edris.values())
print(edris["age"])

edris["score"] = 20
print(edris.items())


scores = {
    "math":90,
    "programming":70,
    "sport":80,
     "saghafat":100
}

#حذف کردن
del scores["programming"]
scores.pop("math")
scores.popitem()
print(scores.items())
scores.clear()
print(scores.items())