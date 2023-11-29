from django.shortcuts import render
from django.http import HttpResponse

def set_session(request):
    request.session['user_id'] = 1
    return HttpResponse("Session set!")

def get_session(request):
    user_id = request.session.get('user_id', None)
    return HttpResponse(f"User ID: {user_id}")

