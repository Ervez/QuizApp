import time

from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
from django.http import HttpResponse


def question_view(request):
    questions = QuestionModel.objects.all()
    num_questions = len(questions)
    current_question_index = request.session.get('current_question_index', 0)
    question_index = request.session.get('question_index', 1)
    num_correct = request.session.get('num_correct', 0)
    if current_question_index == num_questions:
        return redirect('quiz_results')
    current_question = questions[current_question_index]
    context = {
        'current_question': current_question,
        'num_questions': num_questions,
        'current_question_index': current_question_index,
        'num_correct': num_correct,
        'question_index': question_index,
    }
    if request.method == 'POST':
        time.sleep(0.5)
        selected_option = request.POST['selected_option']
        if selected_option == current_question.answer:
            context['is_correct'] = True
            request.session['num_correct'] = num_correct + 1
        else:
            context['is_correct'] = False
        request.session['current_question_index'] = current_question_index + 1
        request.session['question_index'] = question_index + 1
        return redirect('question_view')
    return render(request, 'Quiz/question_view.html', context)


def quiz_results(request):
    num_correct = request.session.get('num_correct', 0)
    num_questions = len(QuestionModel.objects.all())
    if num_correct == num_questions:
        message = 'Congratulations! You answered all questions correctly!'
    elif num_correct == 0:
        message = 'Oops! You did not answer any questions correctly.'
    else:
        message = f'You answered {num_correct} out of {num_questions} questions correctly.'
    request.session.flush()
    return render(request, 'Quiz/quiz_results.html', {'message': message})


def addQuestion(request):
    if request.user.is_staff:
        form = AddQuestionForm()
        if request.method == 'POST':
            form = AddQuestionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'Quiz/addQuestion.html', context)
    else:
        return redirect('question_view')

def home(request):
    return render(request, 'Quiz/home.html')


def logoutPage(request):
    logout(request)
    return redirect('/')
