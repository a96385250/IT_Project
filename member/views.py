from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.core.cache import cache

from member.models import Persons

# Create your views here.

def create(request):
    persons = Persons()
    persons.FristName='邦'
    persons.LastName='幫忙'
    persons.Age = 13

    print(persons.save())
    
    # contextJson = serializers.serialize("json",context)
    return HttpResponse("Create OK")

def read(request):
    # return HttpResponse("Read OK")
    # 檢查 Redis 中是否有統計資料的快取
    redisPersons = cache.get('persons')
    
    if(redisPersons is None):
        # 若快取不存在，執行統計計算並存入快取
        personsDataFromDB = serializers.serialize("json", Persons.objects.all())
        cache.set('persons', personsDataFromDB, 60)
        print("No Cache Data")
        return HttpResponse(personsDataFromDB, content_type="application/json")
    else:
        personsDataFromCache = cache.get('persons')
        print("Cache Data")
        return HttpResponse(personsDataFromCache, content_type="application/json")

    

def checkRedis(request):
    redisPersons = cache.get("persons")

    if(redisPersons is None):
        print("No cache")

    return HttpResponse("Check Redis")


