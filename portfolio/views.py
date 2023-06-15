from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import *
from .models import *


# Create your views here.

def home_page_view(request):
    ProjectsList = Project.objects.all()
    context = {'ProjectsList': ProjectsList}
    return render(request, 'portfolio/home.html', context)


def courses_page_view(request):
    AcademicsList = Academic.objects.all()
    CurricularUnitsList = CurricularUnit.objects.all()
    OtherCoursesList = OtherCourse.objects.all()
    CertificationsList = Certification.objects.all()
    context = {'AcademicsList': AcademicsList,
               'OtherCoursesList': OtherCoursesList,
               'CertificationsList': CertificationsList,
               'CurricularUnitsList': CurricularUnitsList}
    return render(request, 'portfolio/courses.html', context)



def playground_page_view(request):
    return render(request, 'portfolio/playground.html')


def blog_page_view(request):
    ProjectsList = Project.objects.all()

    articles_All = Article.objects.all()
    articles_Business = Article.objects.all().filter(area='Business')
    articles_Technology = Article.objects.all().filter(area='Technology')
    articles_Entertainment = Article.objects.all().filter(area='Entertainment')
    articles_Lifestyle = Article.objects.all().filter(area='Lifestyle')
    articles_Travel = Article.objects.all().filter(area='Travel')
    articles_Sports = Article.objects.all().filter(area='Sports')
    articles_Other = Article.objects.all().filter(area='Other')
    context = {'articles_All': articles_All,
               'articles_Business': articles_Business,
               'articles_Technology': articles_Technology,
               'articles_Entertainment': articles_Entertainment,
               'articles_Lifestyle': articles_Lifestyle,
               'articles_Travel': articles_Travel,
               'articles_Sports': articles_Sports,
               'articles_Other': articles_Other,
               'ProjectsList': ProjectsList}
    return render(request, 'portfolio/blog.html', context)


def article_page_view(request, article_id):
    article = Article.objects.get(pk=article_id)
    context = {'article': article}
    return render(request, 'portfolio/article.html', context)


def webDev_page_view(request):
    be_subjects = Subject.objects.filter(name__startswith='Back')
    fe_subjects = Subject.objects.filter(name__startswith='Front')
    other_subjects = Subject.objects.filter(name__startswith='Other')
    backEndTechsList = Tech_BackEnd.objects.all()
    frontEndTechsList = Tech_FrontEnd.objects.all()
    otherTechsList = Tech_Other.objects.all()
    context = {'be_subjects': be_subjects,
               'fe_subjects': fe_subjects,
               'other_subjects': other_subjects,
               'backEndTechsList': backEndTechsList,
               'frontEndTechsList': frontEndTechsList,
               'otherTechsList': otherTechsList}
    return render(request, 'portfolio/webDev.html', context)


def der_page_view(request):
    return render(request, 'portfolio/der.html')


def sitemap_page_view(request):
    return render(request, 'portfolio/sitemap.html')


#AUTHENTICATION---------------------------------------------------------------------------------------------
def login_page_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('portfolio:home'))
        else:
            return render(request, "portfolio/login.html", {
                'message': "Invalid credentials."
            })

    return render(request, 'portfolio/login.html')


def logout_page_view(request):
    logout(request)

    return render(request, 'portfolio/home.html')


#CRUD---------------------------------------------------------------------------------------------
@login_required
def add_author_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}

    return render(request, 'portfolio/add_author.html', context)

@login_required
def add_article_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form}
    return render(request, 'portfolio/add_article.html', context)


@login_required
def add_curricularUnit_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form = CurricularUnitForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:courses'))

    context = {'form': form}
    return render(request, 'portfolio/add_curricularUnit.html', context)


@login_required
def add_project_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('portfolio:home')

    context = {'form': form}
    return render(request, 'portfolio/add_project.html', context)

@login_required
def edit_article_page_view(request, article_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    article = Article.objects.get(id=article_id)
    form = ArticleForm(request.POST or None, instance=article )
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))
    context = {'form': form, 'article_id': article_id}
    return render(request, 'portfolio/edit_article.html', context)


@login_required
def edit_curricularUnit_page_view(request, curricularUnit_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    curricularUnit = CurricularUnit.objects.get(id=curricularUnit_id)
    form = CurricularUnitForm(request.POST or None, instance=curricularUnit)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:courses'))
    context = {'form': form, 'curricularUnit_id': curricularUnit_id }
    return render(request, 'portfolio/edit_curricularUnit.html', context)


@login_required
def edit_project_page_view(request, project_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))

    project = Project.objects.get(id=project_id)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('portfolio:home')
    context = {'form': form, 'project_id': project_id }
    return render(request, 'portfolio/edit_project.html', context)

@login_required
def remove_article(request, article_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))
    Article.objects.get(id=article_id).delete()
    return HttpResponseRedirect(reverse('portfolio:blog'))

def remove_curricularUnit(request, curricularUnit_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))
    CurricularUnit.objects.get(id=curricularUnit_id).delete()
    return HttpResponseRedirect(reverse('portfolio:courses'))

@login_required
def remove_project(request, project_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('portfolio:login'))
    Project.objects.get(id=project_id).delete()
    return HttpResponseRedirect(reverse('portfolio:home'))


