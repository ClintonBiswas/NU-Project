from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
import threading
from django.contrib import messages
from django.db.models import Q
from user.models import RefBooks, NuQuestion, AddProjects, ProgrammingContest,Contact, OurTeam

# Create your views here.
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# class EmailThread(threading.Thread):
#     def __init__(self, email_message):
#         self.email_message = email_message
#         threading.Thread.__init__(self)
#     def run(self):
#         self.email_message.send()

def Home(request):
    project = AddProjects.objects.all()
    team = OurTeam.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        print(email)
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, description=message)
        # email_message = EmailMessage(
        # f'Hi {name}, Thanks for Contacting With me',
        # 'Our customer agent will contact you soon.',
        # settings.EMAIL_HOST_USER,
        # [email],
        # )
        # EmailThread(email_message).start()
        messages.success(request,"Thanks for submission. Please check your email")
    
    dict = {'projects':project,'teams': team}
    return render(request, 'other/home.html', context=dict)

def SearchView(request):
    query = request.GET.get('query')
    results = []
    results1 = []
    if query:
        results = RefBooks.objects.filter(book_name__icontains=query)
        try:
            query_int = int(query)  # Convert the input value to an integer
            results1 = NuQuestion.objects.filter(
                Q(subject_name__icontains=query) |
                Q(question_type__icontains=query) |
                Q(question_year=query_int)
            )
        except ValueError:
            results1 = NuQuestion.objects.filter(
                Q(subject_name__icontains=query) |
                Q(question_type__icontains=query)
            )

    dict = {'results': results, 'results1': results1, 'query': query}
    return render(request, 'other/search.html', context=dict)

def projectDetails(request, slug):
    project = AddProjects.objects.get(slug=slug)
    dict = {'project':project}
    return render(request, 'other/project_d.html', context=dict)


def RefBooksView(request):
    book = RefBooks.objects.all()
    dict={'books': book}
    return render(request, 'other/ref_bookV.html', context=dict)

def NuQuestionView(request):
    question = NuQuestion.objects.all()
    dict={'questions': question}
    return render(request, 'other/question.html', context=dict)

def ProgrammingContestView(request):
    contest = ProgrammingContest.objects.all()
    dict = {'contests':contest}
    return render(request, 'other/pcontest.html', context=dict)

def ProductView(request):
    dict = {}
    return render(request, 'other/product.html', context=dict)

