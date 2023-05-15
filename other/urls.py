from django.urls import path
from .views import Home, RefBooksView, NuQuestionView, ProgrammingContestView, ProductView, SearchView, projectDetails

app_name = 'other'
urlpatterns = [
    path('', Home, name='home'),
    path('search/', SearchView, name='search'),
    path('ref-books/', RefBooksView, name='ref-books'),
    path('project-details/<slug:slug>/',projectDetails, name='project_details'),
    path('nu-questions/', NuQuestionView, name='nu-questions'),
    path('programming-contest/', ProgrammingContestView, name='programming-contest'),
    path('product/', ProductView, name='product'),
]