from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from movie.models import Movie
import random
import json
from movie.uid_mid import recommendationM


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
    if request.method == "POST":  # 获取类型信息，根据type进行查询并返回数据
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
    # print(result)
    return HttpResponse(json.dumps(result))


def show(request):  # 未完成
    detail = {}
    if request.method == "POST":     # 对点击的电影进行详细信息的展示
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
    return HttpResponse(json.dumps(detail))


def laji(request):
    return render_to_response('detail.html')


def login(request):
    return render_to_response('login.html')


def getid(request):  # 获取用户登录名，根据用户名进行推荐
    recommend = {}
    if request.method == "POST":
        uername = request.POST.get("name")
        recommend = recommendationM(uername)
    return HttpResponse(json.dumps(recommend))


def select_movie(request):  # 未完成 search by key word
    res = {}
    if request.method == "POST":
        info = request.POST.get("info")  # 获取搜索框的内容，根据info进行查询并返回数据
        movies_exact = Movie.objects.get(m_name=info)
        movie_apro = Movie.objects.filter(m_name__contains=info)
        # srci typei namei
        if movies_exact :
            res['src{}'.format(0)] = movies_exact.imgurl
            res['type{}'.format(0)] = movies_exact.type
            res['name{}'.format(0)] = movies_exact.m_name

        for x in range(len(movie_apro)):
            if movie_exact :
                x+=1
            res['src{}'.format(x)] = movies_exact[x].imgurl
            res['type{}'.format(x)] = movies_exact[x].type
            res['name{}'.format(x)] = movies_exact[x].m_name

    return HttpResponse(json.dumps(res))
