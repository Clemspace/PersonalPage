from django.shortcuts import render

def home(request):
    return render(request, 'researcher/home.html')

def about(request):
    return render(request, 'researcher/about.html')

def services(request):
    return render(request, 'researcher/services.html')

def portfolio(request):
    return render(request, 'researcher/portfolio.html')

def blog(request):
    return render(request, 'researcher/blog.html')

def contact(request):
    return render(request, 'researcher/contact.html')