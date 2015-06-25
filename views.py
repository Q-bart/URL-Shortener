
from django.http import  Http404, HttpResponse
from django.shortcuts import render_to_response
from appshort.forms import AddSite
from appshort.models import ShortURL, LongURL
import random, string


	