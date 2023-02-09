from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
#--------------------------------------
class Word(models.Model):
    _id  = models.AutoField(primary_key=True,editable=False)
    word = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self) -> str:
        return f"{self.word}"
#--------------------------------------
class Meaning(models.Model):
    _id = models.AutoField(primary_key=True,editable=False)
    word = models.ForeignKey(Word,on_delete= models.SET_NULL,null=True)
    meaning = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self) -> str:
        return f"{self.word} {self.meaning}"
#--------------------------------------
class Sentence(models.Model):
    _id = models.AutoField(primary_key=True,editable=False)
    word = models.ForeignKey(Word,on_delete= models.SET_NULL,null=True)
    sentence = models.CharField(max_length=300,null=True,blank=True)
    def __str__(self) -> str:
        return f"{self.word} {self.sentence}" 
#--------------------------------------
class Synonym(models.Model):
    _id = models.AutoField(primary_key=True,editable=False)
    word = models.ForeignKey(Word,on_delete= models.SET_NULL,null=True)
    similar = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self) -> str:
        return f"{self.word} {self.similar}"
#--------------------------------------
class Antononym(models.Model):
    _id = models.AutoField(primary_key=True,editable=False)
    word = models.ForeignKey(Word,on_delete= models.SET_NULL,null=True)
    opposite = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self) -> str:
        return f"{self.word} {self.opposite}"
#--------------------------------------
class Pharase(models.Model):
    _id = models.AutoField(primary_key=True,editable=False)
    word = models.ForeignKey(Word,on_delete= models.SET_NULL,null=True)
    sentence = models.CharField(max_length=400,null=True,blank=True)
    def __str__(self) -> str:
        return f"{self.word} {self.sentence}"
#--------------------------------------
# class Like(models.Model):
#     _id = models.AutoField(primary_key=True,editable=False)
#     word = models.ForeignKey(Word,on_delete= models.SET_NULL,null=True)
#     def __str__(self) -> str:
#         return f"{self.word}"