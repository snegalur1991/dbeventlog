from doctest import IGNORE_EXCEPTION_DETAIL
from logging import PlaceHolder
from statistics import mode
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField

#class members(models.Model):
#	member_name = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

user_choice = (('karvinth','Arvinth'),('ahegde','Ashik'),('sdey','Saikat'), ('vsatisha', 'Vinay'),('snegalur','Santosh'),('cursu','Catalina'),('jlove', 'Joe'))
ServerTypeChoice = (('Production','Production'), ('Staging','Staging'), ('Development', 'Development'), ('Pre-Production', 'Pre-Production'), ('Decommissioned', 'Decommissioned'))

# Create your models here.
class details(models.Model):
    HostName = models.CharField(max_length=120, default='', blank=True, null=True)
    ServerName = models.CharField(max_length=120, default='', blank=True, null=True)
    CreatedOn = models.DateTimeField(auto_now_add=True, null=True)
    PerformedAt = models.DateTimeField(default=timezone.now)
    EnteredBy = models.ForeignKey(User, default=None, on_delete=models.DO_NOTHING)
    PerformedBy = models.CharField(choices=user_choice,max_length=20, null=True, blank=True )
    ServerType = models.CharField(max_length=20, default='', blank=True, null=True, choices=ServerTypeChoice)
    Comments = RichTextField()



class servers(models.Model):
    Application = models.CharField(max_length=10, default='', blank=True, null=True)
    ServerType = models.CharField(max_length=20, default='', blank=True, null=True, choices=ServerTypeChoice)
    DBTypeChoice = (('ASE','ASE'), ('REP','REP'), ('IQ', 'IQ'), ('MySQL', 'MySQL'), ('MSSQL', 'MSSQL'), ('Others', 'Others'))
    DBType = models.CharField(max_length=20, default='', blank=True, null=True, choices=DBTypeChoice)
    ServerName = models.CharField(max_length=120, default='', unique=True, blank=True,)
    DBVersion = models.CharField(max_length=1000, default='', blank=True, null=True)
    HostName = models.CharField(max_length=120, default='', blank=True, null=True)
    HostIP = models.CharField(max_length=20, default='', blank=True, null=True)
    HostVersion = models.CharField(max_length=120, default='', blank=True, null=True)
    VIPName = models.CharField(max_length=20, default='', blank=True, null=True)
    Memory = models.IntegerField(blank=True, null=True)
    vCPUs = models.IntegerField(blank=True, null=True)


class site(models.Model):
    id = models.AutoField(primary_key=True)
    SiteName = models.CharField(max_length=120, default='', blank=True, null=True)
    URL_Link = models.URLField(max_length=10000)

