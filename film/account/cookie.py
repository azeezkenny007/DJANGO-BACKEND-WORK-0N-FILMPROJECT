from django.http import HttpResponse

def test_cookie(request):   
    if not request.COOKIES.get('color'):
        response = HttpResponse("Cookie Set")
        response.set_cookie('color', 'blue')
        return response
    else:
        return HttpResponse("Your favorite color is {0}".format(request.COOKIES['color']))
       
# example 2 
from django.http import HttpResponse

def set_cookie_view(request):
    response = HttpResponse('Cookie set')
    # set_cookie takes in a(name,value,max_age)
    # name = name of the cookie
    # value = value of the cookie
    # max_age = how many seconds for the cookie to last
    response.set_cookie('favorite_color', 'blue', max_age=30)
    return response

def get_cookie_view(request):
    favorite_color = request.COOKIES.get('favorite_color')
    return HttpResponse(f'Your favorite color is {favorite_color}')
