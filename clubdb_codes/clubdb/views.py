from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib import messages
# from clubdb.forms import clubforms
from clubdb.models import club
from clubdb.models import events
from clubdb.forms import clubforms
from clubdb.forms import eventforms
from clubdb.forms import clubaddressforms
from clubdb.models import club_address
from django.db import connection
def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
    
def Insertclub(request):
    if request.method=="POST":
        if request.POST.get('club_id') and request.POST.get('club_name') and request.POST.get('club_email'):
            saverecord = club()
            saverecord.club_id=request.POST.get('club_id')
            saverecord.club_name=request.POST.get('club_name')
            saverecord.club_email=request.POST.get('club_email')
            saverecord.save()
            messages.success(request,'Club '+saverecord.club_name+' is saved successfully..')
            return render(request,'Insertclub.html')
    else:
        return render(request, 'Insertclub.html')

def showclub(request):
    showall=club.objects.all()
    context = {
        'data': showall
    }
    return render(request,'showclub.html',context)

def sortclub(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=club.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'sortclub.html',context)
    else:
        return render(request,'sortclub.html')

def EditClub(request,id):
    Editclub=club.objects.get(club_id=id)
    return render(request,'EditClub.html',{"club":Editclub})
 
def updateclub(request,id):
    Updateclub=club.objects.get(club_id=id)
    form=clubforms(request.POST,instance=Updateclub)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updates succesfully!!')
        return render(request,'EditClub.html',{"club":Updateclub})
        
def InputCustomQuery(request):
    return render(request, 'Query.html', {})


def runQueryClub(request):
    raw_query = "select \"club\".\"club_id\",\"club\".\"club_name\" from \"club\" "
    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()
    return render(request, 'Query.html', {'data': alldata})


def ProcessCustomQuery(request):
    raw_query = request.POST.get('query')

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    print(alldata)

    return render(request, 'runQueryClub.html', {'data':alldata,'colnames':colnames, 'lencol':range(len(colnames))})

def DeleteClub(request,id):
    delGameObj=club.objects.get(club_id=id)
    delGameObj.delete()
    showall=club.objects.all()
    messages.success(request,'Record deleted succesfully!!')
    return render(request,'DeleteClub.html',{"club": DeleteClub})


# ======================================================================================================


def showevent(request):
    showall=events.objects.all()
    context = {
        'data': showall
    }
    return render(request,'showevent.html',context)

def sortevent(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=events.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'sortevent.html',context)
    else:
        return render(request,'sortevent.html')

def EditEvent(request,id):
    Editevent=events.objects.get(event_id=id)
    return render(request,'EditEvent.html',{"event":Editevent})

def updateevent(request,id):
    Updateevent=events.objects.get(event_id=id)
    form=eventforms(request.POST,instance=Updateevent)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updates succesfully!!')
        return render(request,'EditEvent.html',{"event":Updateevent})

def Insertevent(request):
    if request.method=="POST":
        if request.POST.get('event_id') and request.POST.get('event_duration') and request.POST.get('event_name') and request.POST.get('event_date') and request.POST.get('event_theme') and request.POST.get('event_capacity') and request.POST.get('event_eligibility'):
            saverecord = events()
            saverecord.event_id=request.POST.get('event_id')
            saverecord.event_duration=request.POST.get('event_duration')
            saverecord.event_name=request.POST.get('event_name')
            saverecord.event_date=request.POST.get('event_date')
            saverecord.event_theme=request.POST.get('event_theme')
            saverecord.event_capacity=request.POST.get('event_capacity')
            saverecord.event_eligibility=request.POST.get('event_eligibility')
            saverecord.save()
            messages.success(request,'Event => '+saverecord.event_name+' is saved successfully..!')
            return render(request,'Insertevent.html')
    else:
        return render(request, 'Insertevent.html')


def DeleteEvent(request,id):
    delGameObj=events.objects.get(event_id=id)
    delGameObj.delete()
    showall=events.objects.all()
    messages.success(request,'Record deleted succesfully!!')
    return render(request,'DeleteEvent.html',{"club": DeleteEvent})


# =====================================================================================

def showaddress(request):
    showadd=club_address.objects.all()
    # showadd=club_address.objects.get(club_id=id)
    return render(request,'clubadd.html',{"Event":showadd})
    
def EditAdd(request,id):
    Editaddd=club_address.objects.get(club_id=id)
    return render(request,'EditAdd.html',{"Event":Editaddd})

def sortaddress(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            sorted=club_address.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request,'sortadd.html',context)
    else:
        return render(request,'sortadd.html')

def EditAdd(request,id):
    Editaddd=club_address.objects.get(club_id=id)
    return render(request,'EditAdd.html',{"Event":Editaddd})

def updateadd(request,id):
    Updateadd=events.objects.get(club_id=id)
    form=clubaddressforms(request.POST,instance=Updateadd)
    if form.is_valid():
        form.save()
        messages.success(request,'Record updates succesfully!!')
        return render(request,'updateadd.html',{"Event":Updateadd})

# def Insertevent(request):
#     if request.method=="POST":
#         if request.POST.get('event_id') and request.POST.get('event_duration') and request.POST.get('event_name') and request.POST.get('event_date') and request.POST.get('event_theme') and request.POST.get('event_capacity') and request.POST.get('event_eligibility'):
#             saverecord = events()
#             saverecord.event_id=request.POST.get('event_id')
#             saverecord.event_duration=request.POST.get('event_duration')
#             saverecord.event_name=request.POST.get('event_name')
#             saverecord.event_date=request.POST.get('event_date')
#             saverecord.event_theme=request.POST.get('event_theme')
#             saverecord.event_capacity=request.POST.get('event_capacity')
#             saverecord.event_eligibility=request.POST.get('event_eligibility')
#             saverecord.save()
#             messages.success(request,'Event => '+saverecord.event_name+' is saved successfully..!')
#             return render(request,'Insertevent.html')
#     else:
#         return render(request, 'Insertevent.html')


# def DeleteEvent(request,id):
#     delGameObj=events.objects.get(event_id=id)
#     delGameObj.delete()
#     showall=events.objects.all()
#     messages.success(request,'Record deleted succesfully!!')
#     return render(request,'DeleteEvent.html',{"club": DeleteEvent})

