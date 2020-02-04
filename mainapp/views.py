from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def main(request): #메인 화면
    return render(
    request, 
    'mainapp/index.html', 
    {})
def signin(request): #로그인 화면
    return render(
    request, 
    'mainapp/signin.html', 
    {})
def signup(request): #회원가입 화면
    return render(
    request, 
    'mainapp/signup.html', 
    {})
def swipe(request): #스와이프 화면
    return HttpResponse('<h1>스와이프이얍</h1>')

def like(request): #좋아요 리스트 화면
    return HttpResponse('<h1>좋아요얍</h1>')

def mypage(request): #마이페이지
    return HttpResponse('<h1>마이페이지얍</h1>')

def detail(request): #음식점 상세페이지
    return HttpResponse('<h1>상세페이지얍</h1>')