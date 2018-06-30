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
    print(movie)
    for i in range(7):
        num = random.randint(0, len(movie))
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
        print(num)
        if num not in nums:
            nums.append(num)
    for i in range(6):
        result['src{}'.format(i)] = movie[nums[i]].imgurl
        result['type{}'.format(i)] = movie[nums[i]].type
        result['name{}'.format(i)] = movie[nums[i]].m_name
    # print(result)
    return HttpResponse(json.dumps(result))

#def search_key(request):
    # raw code without test

    

