from django.shortcuts import render

def home_view(request):
    return render(request, 'users/home.html')

def story_view(request):
    return render(request, 'users/story.html')

def about_view(request):
    return render(request, 'users/about.html')

def contact_view(request):
    return render(request, 'users/contact.html')