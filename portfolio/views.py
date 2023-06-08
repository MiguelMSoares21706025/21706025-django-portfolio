from django.shortcuts import render

# Create your views here.
def home_page_view(request):
	return render(request, 'portfolio/home.html')

def courses_page_view(request):
	return render(request, 'portfolio/courses.html')

def playground_page_view(request):
	return render(request, 'portfolio/playground.html')

def sitemap_page_view(request):
	return render(request, 'portfolio/sitemap.html')

def blog_page_view(request):
	return render(request, 'portfolio/blog.html')

def webDev_page_view(request):
	return render(request, 'portfolio/webDev.html')

def about_page_view(request):
	return render(request, 'portfolio/about.html')

