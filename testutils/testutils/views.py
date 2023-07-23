# I have create this file-Imran

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Home")

def analyze(request):
    userText = request.GET.get('text', 'default')
    puncSwitch= request.GET.get('punctuation', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')

    print(userText)
    print(puncSwitch)
    text=''
    dic={}

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if puncSwitch=='on':
        for i in userText:
            if i not in punctuations:
                text=text+i
    else:
        text="Empty"
    print(text)

    dic['Punctuation']= text
    text = ''

    if fullcaps == 'on':
        for i in userText:
            text=text+i.upper()
    else:
        text="Empty"
    print(f"full caps {text}")
    dic["fullcaps"]=text

    text=""
    print(dic['fullcaps'])

    if newlineremover == 'on':
        for i in userText:
            if i != '\n':
                text=text+i
    else:
        text="Empty"

    dic["newlineremover"]=text
    text=""

    if extraspaceremover == 'on':
        for i, ch in enumerate(userText):
            if not (userText[i] == ' ' and userText[i+1] == ' '):
                text = text+ch
    else:
        text = "Empty"

    dic["extraspaceremover"]=text

    return render(request, 'analyze.html',dic)



