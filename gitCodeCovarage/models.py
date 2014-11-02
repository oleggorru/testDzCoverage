from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=32)

class Repository(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length=100)

class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    id_repo = models.ForeignKey(Repository.id)
    name = models.CharField(max_length=40)
class Commit(models.Model):
    id = models.AutoField(primary_key=True)
    id_branch = models.ForeignKey(Branch.id)
    ssh = models.CharField(max_length=40)
class Raw(models.Model):
    id = models.AutoField(primary_key=True)
    id_commit = models.ForeignKey(Commit.id)
    owner = models.CharField(max_length=20)
    file = models.CharField(max_length=20)
    coverage = models.BooleanField()
