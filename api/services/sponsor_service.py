import datetime
from api.models import Hero, Sponsor, Sponsorship

# {
#     "id": 1,
#     "name": "Jorge",
#     "dateOfBirth": "9/25/2003",
#     "gender": "Male",
#     "netWorth": 17000000,
#     "fortuneOrigin": "Data science",
#     "sponsoredHeroes": ["Magdalen, Fanchette", "Rebeka", "karey", "Dido"]
# }


def sponsorMapper(sponsorObject):
    return ({
            "id": sponsorObject["id"],
            "name": sponsorObject["name"],
            "netWorth": sponsorObject["netWorth"],
            "gender": sponsorObject["gender"],
            "dateOfBirth": datetime.datetime.strptime(str(sponsorObject["dateOfbirth"]), "%Y-%m-%d").strftime("%m/%d/%Y"),
            "fortuneOrigin": sponsorObject["fortune_origin"],
            "sponsoredHeroes": sponsorObject["sponsoredHeroes"]
            })


def getAllSponsors():
    sponsorObjectList = list(Sponsor.objects.all().values())

    for index in range(len(sponsorObjectList)):
        sponsorObjectList[index]["sponsoredHeroes"] = list(Hero.objects.filter(id__in=Sponsorship.objects.values_list(
            'hero_id', flat=True
        ).filter(sponsor_id=sponsorObjectList[index]["id"])
        ).values_list('name', flat=True))

        sponsorObjectList[index] = sponsorMapper(sponsorObjectList[index])

    return sponsorObjectList


def getSponsorById(sponsor_id: int):
    sponsorObject = list(Sponsor.objects.all().values().filter(id=sponsor_id))

    if len(sponsorObject) == 0:
        error = {}
        error["error"] = "Sponsor object with id " + str(sponsor_id) + " not found"

        return error, 404

    sponsorObject = sponsorObject[0]

    sponsorObject["sponsoredHeroes"] = list(Hero.objects.filter(id__in=Sponsorship.objects.values_list(
        'hero_id', flat=True
    ).filter(sponsor_id=sponsor_id)
    ).values_list('name', flat=True))

    sponsorObject = sponsorMapper(sponsorObject)

    return sponsorObject, 200
