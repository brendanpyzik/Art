from django.shortcuts import render

# Create your views here.
def add_artist(request):
    print("worksARTIST")
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    return render(request, 'Forms/addinfo.html', {'message': 'Artist Added!'})

def add_piece(request):
    print("worksPiece")
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html', {'message': None})
    return render(request, 'Forms/addinfo.html', {'message': 'Piece Added!'})