from django.http import HttpResponse
from django.shortcuts import render

MENU = {"главная":"/" , "о журнале":"/about" , "новости":"/news"}

def main_page(request):
    title = "Главная страница"
    data = {"menu":MENU, "title": title }
    return render(request, "./index.html", context=data)

def news_page(request):
    title = "Новости месяца"
    data = {"menu":MENU, "title": title }
    return render(request, "./news.html", context=data)

def about_page(request):
    title = "О сайте"
    data = {"menu":MENU, "title": title }
    return render(request, "./about.html", context=data)
