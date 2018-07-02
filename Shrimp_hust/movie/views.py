from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render_to_response
from movie.models import Movie
import random
import json


def index(request):
    result = {}
    nums = []
    movie = Movie.objects.all().all()

    while len(nums) < 6:
        num = random.randint(0, len(movie))
        if num not in nums:
            nums.append(num)
    for i in range(6):
        result['src{}'.format(i)] = movie[nums[i]].imgurl
        result['type{}'.format(i)] = movie[nums[i]].type
        result['name{}'.format(i)] = movie[nums[i]].m_name
    return render(request, 'movie.html', result)


def search(request):
    if request.method == "POST":
        movie_type = request.POST.get("type")
    result = {}
    nums = []
    movie = Movie.objects.filter(type__contains=movie_type)
    while len(nums) < 6:
        num = random.randint(0, len(movie))
        if num not in nums:
            nums.append(num)
    for i in range(6):
        result['src{}'.format(i)] = movie[nums[i]].imgurl
        result['type{}'.format(i)] = movie[nums[i]].type
        result['name{}'.format(i)] = movie[nums[i]].m_name
    return HttpResponse(json.dumps(result))


def show(request):
    detail = {}
    if request.method == "POST":
        movie_name = request.POST.get("name")
        movie = Movie.objects.get(m_name=movie_name)
        detail["name"] = movie.m_name
        detail["src"] = movie.imgurl
        detail["director"] = movie.director
        detail["editor"] = movie.screenwriter
        detail["actor"] = movie.actor
        detail["type"] = movie.type
        detail["area"] = movie.area
        detail["time"] = movie.length
        detail["rate"] = movie.rate
        # print(detail)
    return HttpResponse(json.dumps(detail))


def laji(request):
    return render_to_response('detail.html')


def login(request):
    return render_to_response('login.html')
