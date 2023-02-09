from django.db import models
from django.db.models import fields
from pyexpat import model
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from .models import Meaning, Word,Sentence,Synonym,Pharase
#-----------------------------------------------------------
class MeaningSerializer(serializers.ModelSerializer):
    pass
class SentenceSerializer(serializers.ModelSerializer):
    pass
class SynonymSerializer(serializers.ModelSerializer):
    pass
class PharaseSerializer(serializers.ModelSerializer):
    pass
#-----------------------------------------------------------
class WordSerializer(serializers.ModelSerializer):
    wordmeaning  = SerializerMethodField()
    wordsentence = SerializerMethodField()
    wordsynonym  = SerializerMethodField()
    wordpharase  = SerializerMethodField()
    class Meta:
        model  =  Word
        # fields = ['word','wordmeaning','wordsentence']
        fields = '__all__'
    def get_wordmeaning(self,obj):
        data = obj.meaning_set.all()
        serialized = MeaningSerializer(data,many=True)
        return serialized.data
    def get_wordsentence(self,obj):
        data = obj.sentence_set.all()
        serializer = SentenceSerializer(data,many=True)
        return serializer.data
    def get_wordsynonym(self,obj):
        data = obj.synonym_set.all()
        serializer = SynonymSerializer(data,many=True)
        return serializer.data
    def get_wordpharase(self,obj):
        data = obj.pharase_set.all()
        serializer = PharaseSerializer(data,many=True)
        return serializer.data
#-----------------------------------------------------------
class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Sentence
        fields = '__all__'
#-----------------------------------------------------------
class SynonymSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Synonym
        fields = '__all__'
#-----------------------------------------------------------
#-----------------------------------------------------------
class MeaningSerializer(serializers.ModelSerializer):
    # word = WordSerializer(many=False)
    class Meta:
        model  =  Meaning
        # fields = ['meaning']
        fields = '__all__'
        # depth = 1
#-----------------------------------------------------------
class PharaseSerializer(serializers.ModelSerializer):
    class Meta:
        model  =  Pharase
        fields = '__all__'
        # depth = 1
#-----------------------------------------------------------
    
