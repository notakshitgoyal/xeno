from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')
def about(request):
    return render(request, 'core/about.html')

# def signup(request):
#     form = UserCreationForm()
#     return render(request, 'userprofile/signup.html', {
#         'form': form
#     })
