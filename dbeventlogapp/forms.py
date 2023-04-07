from django import forms
from dbeventlogapp.models import details, servers, site
from django.forms import ValidationError

class detailsForm(forms.ModelForm):
    def clean_Hostname(self):
        Hostname = self.cleaned_data.get('Hostname')
        server_list = []
        for server in servers.objects.values_list('HostName'):
            server_list.append(server)
            
        if self.instance.HostName not in server_list:
            raise forms.ValidationError("server does not exist")

    class Meta:
        model = details
        fields = [
            'HostName', 'ServerName', 'ServerType', 'Comments', 'PerformedBy', 'PerformedAt'
            ]
    


class detailsSearchForm(forms.ModelForm):
    class Meta:
        model = details
        fields = ['HostName', 'ServerName', 'ServerType', 'PerformedBy', 'Comments']

class ServersEntryForm(forms.ModelForm):
    class Meta:
        model = servers
        fields = [
            'Application', 'ServerType', 'DBType', 'ServerName', 'DBVersion', 'HostName', 'HostIP', 'HostVersion', 'VIPName', 'Memory', 'vCPUs'
            ]
 
class ServersSearchForm(forms.ModelForm):
    class Meta:
        model = servers
        fields = [
            'Application', 'ServerType', 'DBType', 'ServerName', 'DBVersion', 'HostName', 'HostIP', 'HostVersion', 'VIPName'
            ]

class siteAddForm(forms.ModelForm):
    class Meta:
        model = site
        fields = [
            'SiteName', 'URL_Link'
        ]

class siteSearchForm(forms.ModelForm):
    class Meta:
        model = site
        fields = [
            'SiteName', 'URL_Link'
        ]

class ServerUpdateForm(forms.ModelForm):
    class Meta:
        model = servers
        fields = [
            'Application', 'ServerType', 'DBType', 'ServerName', 'DBVersion', 'HostName', 'HostIP', 'HostVersion', 'VIPName', 'Memory', 'vCPUs'
            ]
