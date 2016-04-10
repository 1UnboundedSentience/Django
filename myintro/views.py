from django.http import HttpResponse
from django import template
from django.shortcuts import render


def donkey(request):
  return HttpResponse("Hello World!  This will soon be a webpage")

def penguin(request):
  return render(request, 'example-template.html',
    {
      'person_name' : "Jason",
      'item_list': ['snake', 'dog', 'cat'],
      'ordered_warranty': False,
      'company': "Google Inc.",
      'ship_date': "April 10, 2016"
    })