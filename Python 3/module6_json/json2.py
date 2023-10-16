import json

data = """
[
    {
        "id" : "01",
        "fisrt_name" : "marouane",
        "last_name" : "dbibih",
        "phone" : {
            "type" : "intl",
            "number" : "0948309"
        },
        "email" : {
            "hide" : "yes",
            "mail" : "marouane@gmail.com"
        }
    },
    {
        "id" : "02",
        "fisrt_name" : "abdessamade",
        "last_name" : "dbibih",
        "phone" : {
            "type" : "intl",
            "number" : "89579834"
        },
        "email" : {
            "hide" : "yes",
            "mail" : "abdessamade@gmail.com"
        }
    }
]
"""

# Parsing JSON data and retrun list and dictionnaire
infos = json.loads(data)

print("type of infos var :",type(infos))
print("Lenght",len(infos))
print(infos)

for item in infos:
    print("ID",item["id"])
    print("Fisrt name",item["fisrt_name"])
    print("Last name",item["last_name"])
    print("Phone",item["phone"]["number"])
    print("Email",item["email"]["mail"])
    