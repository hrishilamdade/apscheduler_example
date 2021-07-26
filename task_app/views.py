from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
# Create your views here.

from datetime import datetime
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler

def callB(val):
    print(val)
    sleep(20)
    return None

def triggerA():
    jobList=[1,2,3,4,5,6]
    schd = BackgroundScheduler()
    for i in jobList:
        callB(i)

def runApscheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(triggerA, 'interval', minutes=1)
    scheduler.start()



def index(request):
    runApscheduler()
    return HttpResponse("worked")