import operator

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse('Hello')
    # return render(request, 'home.html', {'hi_there': 'This is me'})
    return render(request, 'home.html', {'hi_there': 'This is me'})


def eggs(request):
    return HttpResponse('<h1>Eggs are great</h1>')

def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordslist = fulltext.split()
    worddictionary = {}

    for word in wordslist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add to the dictionay
            worddictionary[word] = 1
    sortedWords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordslist), 'sortedWords': sortedWords})