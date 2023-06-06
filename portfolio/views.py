from django.shortcuts import render

# Create your views here.
def home_page_view(request):
	return render(request, 'portfolio/home.html')

def about_me_page_view(request):
	return render(request, 'portfolio/about me.html')