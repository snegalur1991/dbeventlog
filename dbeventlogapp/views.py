from multiprocessing import context
from multiprocessing.sharedctypes import Value
from django.shortcuts import render, redirect
from .forms import detailsForm, detailsSearchForm, ServersEntryForm, ServersSearchForm, siteAddForm, siteSearchForm, ServerUpdateForm
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User


# Create your views here.
@login_required(login_url='/login/')
def home(request):
	title = 'Sinch SDI Database Eventlog'
	context = {
        "title": title,
        }
	return render(request, "home.html",context)

@login_required(login_url='/login/')
def add_event(request):
    form = detailsForm(request.POST or None)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.EnteredBy = request.user
        instance.save()
        #messages.success(request, 'Successfully Saved')
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        subject = f"New Event Log Entry for {form.cleaned_data['ServerName'] } on {form.cleaned_data['HostName']} by {form.cleaned_data['PerformedBy']}"
        body = f"New Event Log Entry for {form.cleaned_data['ServerName'] } on {form.cleaned_data['HostName']} by {form.cleaned_data['PerformedBy']}" + "\n"
        body += "DBServerName: " + str(form.cleaned_data['ServerName']) + "\n"
        body += "HostName: " + form.cleaned_data['HostName'] + "\n"
        body += "ServerType: " + form.cleaned_data['ServerType'] + "\n"
        body += "PerformedBy: " + form.cleaned_data['PerformedBy'] + "\n"
        EnteredBy1 = str(instance.EnteredBy)
        body += "EnteredBy: " + EnteredBy1 + "\n"
        body += "EnteredAt: " + dt_string + "\n"
        PerformedAt1 = form.cleaned_data['PerformedAt']
        PerformedAt1 = str(PerformedAt1)
        body += "PerformedAt: " + PerformedAt1 + "\n"
        body += "Comments: " + form.cleaned_data['Comments'] + "\n"
        
        #try:
            #send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, settings.DEFAULT_TO_EMAIL )
        #except BadHeaderError:
            #return HttpResponse("Invalid header found.")

        return redirect('/list_event')
        
    context = {
        "form": form,
        "title": "New Event",
    }
    return render(request, "add_event.html", context)

@login_required(login_url='/login/')
def list_event(request):
    title = 'List of Events'
    queryset = details.objects.filter().order_by('-CreatedOn')[:50]
    form = detailsSearchForm(request.POST or None)
    context = {
		"title": title,
		"queryset": queryset,
        "form": form
	}

    if request.method == 'POST':
        queryset = details.objects.filter(
            HostName__icontains=form['HostName'].value(),
            ServerName__icontains=form['ServerName'].value(),
            ServerType__icontains=form['ServerType'].value(),
            PerformedBy__icontains=form['PerformedBy'].value(),
            Comments__icontains=form['Comments'].value(),
        ).order_by('-CreatedOn')[:50]
        context = {
            "title": title,
            "queryset": queryset,
            "form": form,
        }
    return render(request, "list_event.html", context)

def add_server(request):
    form = ServersEntryForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.EnteredBy = request.user
        form.save()
        EnteredBy2 = str(instance.EnteredBy)
        subject = f"New Database Instance {form.cleaned_data['ServerName']} added by {EnteredBy2}"
        body = "App: " + str(form.cleaned_data["Application"]) + "\n"
        body += "ServerType: " + str(form.cleaned_data["ServerType"]) + "\n"
        body += "DBType: " + str(form.cleaned_data["DBType"]) + "\n"
        body += "ServerName: " + str(form.cleaned_data["ServerName"]) + "\n"
        body += "DBVersion: " + str(form.cleaned_data["DBVersion"]) + "\n"
        body += "HostName: " + str(form.cleaned_data["HostName"]) + "\n"
        body += "HostIP: " + str(form.cleaned_data["HostIP"]) + "\n"
        body += "HostVersion: " + str(form.cleaned_data["HostVersion"]) + "\n"
        body += "VIPName: " + str(form.cleaned_data["VIPName"]) + "\n"
        body += "Memory: " + str(form.cleaned_data["Memory"]) + "\n"
        body += "CPUs: " + str(form.cleaned_data["vCPUs"]) + "\n"
        # messages.success(request, 'Successfully Saved')
        #try:
            #send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, ['santosh.negalur@sinch.com'])
        #except BadHeaderError:
            #return HttpResponse("Invalid header found.")

        return redirect("/list_server")
    context = {
        "form": form,
        "title": "New Server Entry",
    }
    return render(request, "add_server.html", context)

@login_required(login_url='/login/')
def list_server(request):
    title = 'List of servers'
    queryset = servers.objects.all()
    form = ServersSearchForm(request.POST or None)
    context = {
		"title": title,
		"queryset": queryset,
        "form": form
	}

    if request.method == 'POST':
        queryset = servers.objects.filter(
            Application__icontains=form['Application'].value(),    
            ServerType__icontains=form['ServerType'].value(),
            DBType__icontains=form['DBType'].value(),
            ServerName__icontains=form['ServerName'].value(),
            HostName__icontains=form['HostName'].value(),
        )
        context = {
            "title": title,
            "queryset": queryset,
            "form": form,
        }
    return render(request, "list_server.html", context)

@login_required
def add_site(request):
    form = siteAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        #messages.success(request, 'Successfully Saved')
        return redirect('/list_site')
    context = {
        "form": form,
        "title": "New Site Entry",
    }
    return render(request, "add_site.html", context)

@login_required(login_url='/login/')
def list_site(request):
    title = 'List of DB Links'
    queryset = site.objects.all()
    form = siteSearchForm(request.POST or None)
    context = {
		"title": title,
		"queryset": queryset,
        "form": form
	}

    if request.method == 'POST':
        queryset = site.objects.all(
        )
        context = {
            "title": title,
            "queryset": queryset,
            "form": form,
        }
    return render(request, "list_site.html", context)


@login_required
def delete_server(request, pk):
	queryset = servers.objects.get(id=pk)
	if request.method == 'POST':
		queryset.delete()
		return redirect('/list_server')
	return render(request, 'delete_server.html')

@login_required
def update_server(request, pk):
	queryset = servers.objects.get(id=pk)
	form = ServerUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = ServerUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/list_server')

	context = {
		'form':form
	}
	return render(request, 'add_server.html', context)