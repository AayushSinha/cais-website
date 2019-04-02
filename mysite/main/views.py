from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import random
from .models import UserResponse
from rest_framework.views import APIView
from rest_framework.response import Response
counter = 0
responses = []
@login_required
def homepage(request):
     global counter,responses
     counter = 0
     responses = []
     return render(request, 'main/homepage.html', {'title': 'Homepage'})

def staticquiz(request):
    global counter
    print(counter)
    if request.method == 'POST':
        if request.POST.get('left'):
            counter = counter +1
            responses.append(request.POST.get('left'))
            print(request.POST.get('left'))
        if request.POST.get('right'):
            counter = counter +1
            print(request.POST.get('right'))
            responses.append(request.POST.get('right'))
        if request.POST.get('indifferent'):
            counter = counter +1
            print(request.POST.get('indifferent'))
            responses.append(request.POST.get('indifferent'))
        if counter == 10:
            user_resp = UserResponse()
            user_resp.user = request.user
            user_resp.response1 = responses[0]
            user_resp.response2 = responses[1]
            user_resp.response3 = responses[2]
            user_resp.response4 = responses[3]
            user_resp.response5 = responses[4]
            user_resp.response6 = responses[5]
            user_resp.response7 = responses[6]
            user_resp.response8 = responses[7]
            user_resp.response9 = responses[8]
            user_resp.response10 = responses[9]
            user_resp.save()
            return HttpResponse("Thank you for taking the test!")
        else:
            return render(request, 'main/staticquiz.html', {'title': 'Charts'})
    else:
        return render(request, 'main/staticquiz.html', {'title': 'Charts'})


def adaptivequiz(request):
    global counter
    print(counter)
    if request.method == 'POST':
        if request.POST.get('left'):
            counter = counter +1
            responses.append(request.POST.get('left'))
            print(request.POST.get('left'))
        if request.POST.get('right'):
            counter = counter +1
            print(request.POST.get('right'))
            responses.append(request.POST.get('right'))
        if request.POST.get('indifferent'):
            counter = counter +1
            print(request.POST.get('indifferent'))
            responses.append(request.POST.get('indifferent'))
        if counter == 10:
            user_resp = UserResponse()
            user_resp.user = request.user
            user_resp.response1 = responses[0]
            user_resp.response2 = responses[1]
            user_resp.response3 = responses[2]
            user_resp.response4 = responses[3]
            user_resp.response5 = responses[4]
            user_resp.response6 = responses[5]
            user_resp.response7 = responses[6]
            user_resp.response8 = responses[7]
            user_resp.response9 = responses[8]
            user_resp.response10 = responses[9]
            user_resp.save()
            return HttpResponse("Thank you for taking the test!")
        else:
            return render(request, 'main/adaptivequiz.html', {'title': 'Charts'})
    else:
        return render(request, 'main/adaptivequiz.html', {'title': 'Charts'})
def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)

class PolicyData(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, format=None):
        data = {
            "gen_male":[random.uniform(0,100),random.uniform(0,100)],
            "gen_female":[random.uniform(0,100),random.uniform(0,100)],
            "gen_other":[random.uniform(0,100),random.uniform(0,100)],
            "race_black":[random.uniform(0,100),random.uniform(0,100)],
            "race_hisp":[random.uniform(0,100),random.uniform(0,100)],
            "race_white":[random.uniform(0,100),random.uniform(0,100)],
            "race_other":[random.uniform(0,100),random.uniform(0,100)],
            "sex_lgbt":[random.uniform(0,100),random.uniform(0,100)],
            "sex_nonlgbt":[random.uniform(0,100),random.uniform(0,100)],
            "avg_success":[random.uniform(0,100),random.uniform(0,100)],
            "g_didi":[random.uniform(0,100),random.uniform(0,100)],
            "r_didi":[random.uniform(0,100),random.uniform(0,100)],
            "s_didi":[random.uniform(0,100),random.uniform(0,100)],
        }
        return Response(data)
