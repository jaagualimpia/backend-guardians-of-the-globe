import datetime
from api.models import Hero, Weakness, Abilities, Sponsorship, Battle, Villain
from django.db.models import Count


# "id": 1,
# "name": "Magdalen",
# "dateOfBirth": "12/6/2002",
# "gender": "Female",
# "description": "Kazan State Finance and Economics Institute ",
# "weaknesses": ["Shortness", "fire", "wind"],
# "abilities": ["darkness", "super strength", "x-ray vision"],
# "principalSponsor": 2,
# "mostFoughtVillain": "un villano bien feroz"


def findPrincipalSponsor(id: int):
    if Sponsorship.objects.filter(hero_id=id).exists():
        return Sponsorship.objects.values_list('sponsor_id', flat=True).filter(hero_id=id).order_by('-amount')[0]

    return None


def findMostFoughtVillain(hero_id: int):
    if Battle.objects.filter(hero_id=hero_id).exists():
        return Battle.objects.filter(hero_id=hero_id).values('villain_id').annotate(count=Count('*')).order_by('-count').values_list('villain_id', flat=True)[0]

    return None


def heroMapper(heroObject):
    hero = {}

    hero["id"] = heroObject["id"]
    hero["name"] = heroObject["name"]
    hero["dateOfBirth"] = datetime.datetime.strptime(str(heroObject["dateOfBirth"]), "%Y-%m-%d").strftime("%m/%d/%Y")
    hero["gender"] = heroObject["gender"]
    hero["description"] = heroObject["description"]
    hero["weaknesses"] = heroObject["weaknesses"]
    hero["abilities"] = heroObject["abilities"]
    hero["principalSponsor"] = heroObject["principalSponsor"]
    hero["mostFoughtVillain"] = heroObject["mostFoughtVillain"]

    return hero


def getAllHeroes():
    heroesObjectList = list(Hero.objects.all().values())

    for index in range(len(heroesObjectList)):

        heroesObjectList[index]["weaknesses"] = list(Weakness.objects.values_list(
            'weakness', flat=True)
            .filter(id_person=heroesObjectList[index]["id"], is_villain=False))

        heroesObjectList[index]["abilities"] = list(Abilities.objects.values_list(
            'ability', flat=True)
            .filter(id_person=heroesObjectList[index]["id"], is_villain=False))

        heroesObjectList[index]["principalSponsor"] = findPrincipalSponsor(
            heroesObjectList[index]["id"])

        heroesObjectList[index]["mostFoughtVillain"] = findMostFoughtVillain(
            heroesObjectList[index]["id"])
        
        heroesObjectList[index] = heroMapper(heroesObjectList[index])

    return heroesObjectList


def getHeroById(id: int):
    heroObject = list(Hero.objects.filter(id=id).values())


    if len(heroObject) == 0:
        error = {}
        error["error"] = "Hero object with id " + str(id) + " not found"
        
        return error, 404 
    
    heroObject = heroObject[0]

    heroObject["weaknesses"] = list(Weakness.objects.values_list(
        'weakness', flat=True)
        .filter(id_person=heroObject["id"], is_villain=False))

    heroObject["abilities"] = list(Abilities.objects.values_list(
        'ability', flat=True)
        .filter(id_person=heroObject["id"], is_villain=False))

    heroObject["principalSponsor"] = findPrincipalSponsor(heroObject["id"])

    heroObject["mostFoughtVillain"] = findMostFoughtVillain(heroObject["id"])

    heroObject = heroMapper(heroObject)

    return heroObject, 200
