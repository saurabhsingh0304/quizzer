from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Quiz
from django.core.paginator import Paginator
import datetime
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

response= []
d1=datetime.datetime.now()
d2=datetime.datetime.now()

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        context = {'form': form,}
        return render(request, 'quizzer/registration.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        context = {}
        return render(request, 'quizzer/login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request,'quizzer/welcome.html')

@login_required(login_url='login')
def quizzes(request):
    quizzes = Quiz.objects.all()
    context = {'quizzes': quizzes,}
    return render(request, 'quizzer/available_quizzes.html', context)

@login_required(login_url='login')
def questions(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    question = quiz.question_set.all()
    question_count = question.count()
    paginator = Paginator(question,1)
    d1 = datetime.datetime.now()
    try:
        page = int(request.GET.get('page','1'))  
    except:
        page =1
    try:
        per = paginator.page(page)
    except(EmptyPage, InvalidPage):
        per = paginator.page(paginator.num_pages)
    context = {'question': question, 'per': per, 'count': question_count, 'pk':pk}
    return render(request, 'quizzer/question.html',context)


@login_required(login_url='login')
def save_ans(request):
    ans = request.GET['ans']
    response.append(ans)

@login_required(login_url='login')
def results(request, pk):
    answerlist = []
    k=0
    score=0
    quiz = Quiz.objects.get(pk=pk)
    question = quiz.question_set.all()
    for i in question:
        answerlist.append(i)
        k=k+1
    d2 = datetime.datetime.now()
    for j in range(k):
        if answerlist[j]==response[j]:
            score += 1
    response.clear()
    context = {'score':score, 'time':str((d2-question.d1))}
    return render(response, 'quizzer/result.html', context)
    
    
