# "heroName": "Fanchette",
# "villainName": "Valle",
# "date": "12/15/2022",
# "isWinned": true

from api.models import Battle, Hero, Villain
import datetime


def matchMapper(matchObject):
    return ({
        "heroName": matchObject["hero"],
        "villainName": matchObject["villain"],
        "date": datetime.datetime.strptime(str(matchObject["date"]), "%Y-%m-%d").strftime("%m/%d/%Y"),
        "isWinned": matchObject["winned"]
    })

def getAllMatches():
    matchesObject = list(Battle.objects.all().values())

    for index in range(len(matchesObject)):
        matchesObject[index]["hero"] = Hero.objects.filter(id=matchesObject[index]["hero_id"]).values_list('name', flat=True)[0]
        matchesObject[index]["villain"] = Villain.objects.filter(id=matchesObject[index]["villain_id"]).values_list('name', flat=True)[0]
        
        matchesObject[index] = matchMapper(matchesObject[index])

    return matchesObject, 200

def getMatchById(id_match: int):
    matchesObject = list(Battle.objects.all().values().filter(id=id_match))

    if len(matchesObject) == 0:
        error = {}
        error["error"] = "Match object with id " + str(id) + " not found"

        return error, 404

    matchObject = matchesObject[0]

    matchObject["hero"] = Hero.objects.filter(id=matchObject["hero_id"]).values_list('name', flat=True)[0]
    matchObject["villain"] = Villain.objects.filter(id=matchObject["villain_id"]).values_list('name', flat=True)[0]
    
    matchObject = matchMapper(matchObject)

    return matchObject, 200