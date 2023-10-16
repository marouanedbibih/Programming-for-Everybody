import json

data = """
    {
        "name" : "marouane",
        "phone" :{
            "type" : "intl",
            "number" : "+21267846237"
        },
        "email" : {
            "hide" : "yes"
        }
    }
"""

json_data = json.loads(data)

print("Name is :",json_data['name'])
print("Phone is :",json_data["phone"]["number"])
print("Email is ",json_data["email"]["hide"])