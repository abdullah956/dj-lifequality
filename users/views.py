from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def story_view(request):
    return render(request, 'story.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')