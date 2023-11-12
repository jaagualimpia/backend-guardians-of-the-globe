import datetime
from api.models import Weakness, Abilities, Villain

# {
#             "id": 1,
#             "name": "Magdalen",
#             "dateOfBirth": "12/6/2022",
#             "gender": "Female",
#             "origin": "Kazan State Finance and Economics Institute ",
#             "weaknesses": ["Shortness", "fire", "wind"],
#             "abilities": ["Fire breathing", "super strength", "x-ray vision"]
# }

def villainMapper(villainObject):
    return ({
        "id": villainObject["id"],
        "name": villainObject["name"],
        "dateOfBirth": datetime.datetime.strptime(str(villainObject["dateOfBirth"]), "%Y-%m-%d").strftime("%m/%d/%Y"),
        "gender": villainObject["gender"],
        "origin": villainObject["origin"],
        "weaknesses": villainObject["weaknesses"],
        "abilities": villainObject["abilities"]
    })


def getAllVillains():
    villainsObjectList = list(Villain.objects.all().values())

    for index in range(len(villainsObjectList)):

        villainsObjectList[index]["weaknesses"] = list(Weakness.objects.values_list(
            'weakness', flat=True)
            .filter(id_person=villainsObjectList[index]["id"], is_villain=True))

        villainsObjectList[index]["abilities"] = list(Abilities.objects.values_list(
            'ability', flat=True)
            .filter(id_person=villainsObjectList[index]["id"], is_villain=True))
        
        villainsObjectList[index] = villainMapper(villainsObjectList[index])

    return villainsObjectList

def getVillainById(id: int):
    villainObject = list(Villain.objects.all().values().filter(id=id))

    if len(villainObject) == 0:
        error = {}
        error["error"] = "Villain object with id " + str(id) + " not found"
        
        return error, 404  

    villainObject = villainObject[0]

    villainObject["weaknesses"] = list(Weakness.objects.values_list(
        'weakness', flat=True)
        .filter(id_person=villainObject["id"], is_villain=True))

    villainObject["abilities"] = list(Abilities.objects.values_list(
        'ability', flat=True)
        .filter(id_person=villainObject["id"], is_villain=True))

    villainObject = villainMapper(villainObject)

    return villainObject, 200