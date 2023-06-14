from django.forms import ModelForm
from .models import *


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'


class CurricularUnitForm(ModelForm):
    class Meta:
        model = CurricularUnit
        fields = '__all__'


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'



