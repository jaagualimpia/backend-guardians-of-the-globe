from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import render

from api.services.hero_service import getAllHeroes, getHeroById
from api.services.matches_service import getAllMatches, getMatchById
from api.services.sponsor_service import getAllSponsors, getSponsorById
from api.services.villain_service import getAllVillains, getVillainById

# Create your views here.


def index(request):
    return render(request, 'index.html')


def villains(request):
    response = getAllVillains()
    return JsonResponse(response, status=200, safe=False)


def villain(request, id: int):
    response, status = getVillainById(id)
    return JsonResponse(response, status=status, safe=False)


def heroes(request):
    response = getAllHeroes()
    return JsonResponse(response, status=200, safe=False)


def hero(request, id: int):
    response, status = getHeroById(id)
    return JsonResponse(response, status=status, safe=False)


def matches(request):
    response, status = getAllMatches()
    return JsonResponse(response, status=status, safe=False)

def match(request, id: int):
    response, status = getMatchById(id)
    return JsonResponse(response, status=status, safe=False)


def sponsors(request):
    response = getAllSponsors()

    return JsonResponse(response, status=200, safe=False)


def sponsor(request, id):
    response, status = getSponsorById(id)

    return JsonResponse(response, status=status, safe=False)
