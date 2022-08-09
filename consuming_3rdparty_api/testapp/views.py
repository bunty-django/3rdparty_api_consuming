from django.shortcuts import render
import requests

# Create your views here.


def get_client_ip(request):
    ip = request.META.get('HTTP_X_FORWARDED_FOR', '') or request.META.get('REMOTE_ADDR')
    # url = 'http://api.ipstack.com/2409:4062:2d86:9791:34d2:e071:12d1:b558?access_key=ce032c5e85ffb6f5c41f3390e7e96a00'
    url = 'http://api.ipstack.com/'+str(ip)+'?access_key=ce032c5e85ffb6f5c41f3390e7e96a00'
    response = requests.get(url)
    data = response.json()
    return render(request, 'testapp/info.html', {'data': data})

