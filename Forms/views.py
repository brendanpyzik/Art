from django.shortcuts import render

# Create your views here.
def add_artist(request):
    print("works")
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    return render(request, 'registration/profile.html')

def add_piece(request):
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    return render(request, 'registration/profile.html')