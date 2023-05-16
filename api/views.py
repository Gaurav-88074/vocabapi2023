from django.shortcuts import render
import imp
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# Create your views here.
# Create your views here.
#-------------------------
from .models import Word
from .models import Meaning
from .serializers import WordSerializer
#-----------------------
import random
import json
#-----------------------
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            '1' : 'http://127.0.0.1:8000/allvocab',
        },
        {
            '2' : 'https://vocabapi2023-production.up.railway.app/allvocab',
        },
        {
            '2' : 'https://vocabapi2023-production.up.railway.app/addvocab',
        }
    ]
    return Response(routes)
#---------------------------
#-----------------------
@api_view(['GET'])
def getWord(request):
    serialized = WordSerializer(Word.objects.all(),many = True)
    return Response(serialized.data)
#---------------------------
#---------------------------
@api_view(['POST'])
def addVocab(request):
    postData = request.data
    print(postData)
    wordValue = postData["word"]
    wordObject =Word.objects.create(
        word = wordValue
    )
    wordObject.save();
    meaningValue = postData["meaning"]
    meaningObject = Meaning.objects.create(
        word    = wordObject,
        meaning = meaningValue
    )
    meaningObject.save()
    
    return Response({
        "message" : "vocab has been added succesfully!"
    })
#---------------------------
#---------------------------
@api_view(['GET'])
def getMcqQuestion(request):
    serialized = WordSerializer(Word.objects.all(),many = True)
    res = serialized.data
    random.shuffle(res)
    if len(res)>4:
        pass
        mcqRes = []
        for i in range(len(res)-4):
            obj = res[i]
            choiceoOptions = [
                res[i  ]["wordmeaning"][0]["meaning"],
                res[i+1]["wordmeaning"][0]["meaning"],
                res[i+2]["wordmeaning"][0]["meaning"],
                res[i+3]["wordmeaning"][0]["meaning"]
            ]
            random.shuffle(choiceoOptions)
            mcqRes.append({
                '_id' : i,
                'word' : obj['word'],
                'meaning':obj["wordmeaning"][0]["meaning"],
                'choiceOptions':choiceoOptions
            })
        # print(mcqRes[:3])
        random.shuffle(mcqRes)
        return Response(mcqRes[::-1])
    # print(res[:4])
    return Response(res)
#---------------------------