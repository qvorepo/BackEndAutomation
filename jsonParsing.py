import json

courses = '{"name": "Rahul Shetty", "languages": ["Java", "Python"]}'

#Loads method parses string and return dictionary
dict_courses=json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses["name"])
print(type(dict_courses["languages"]))
#list_languages = dict_courses["languages"]
#print(list_languages[0])
#print(list_languages[1])
print(dict_courses["languages"][1])

#Parse content present in json file
with open('C:\\Users\\Mamga\\PycharmProjects\\BackEndAutomation\\course.json') as f:
    data=json.load(f)
    print(data)
    print(type(data))
    print(data["courses"][0]["title"])
    print(type(data["courses"]))
    for course in data["courses"]:
        print(course)
        if course["title"] == 'RPA':
            print(course["price"])
            assert course["price"] == 45

with open('C:\\Users\\Mamga\\PycharmProjects\\BackEndAutomation\\course1.json') as f1:
    data1=json.load(f1)
    print(data == data1) # Compare contents of course with course1.  The result is false.
    assert data == data1

