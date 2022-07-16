from django.shortcuts import redirect, render
from .forms import QuestionForm
from .models import Question
# Create your views here.


def index(request):
    if request.method == 'POST':
        print(request.POST)
        questions = Question.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = score/(total*10) * 100
        context = {
            'score': score,
            'time': request.POST.get('timer'),
            'correct': correct,
            'wrong': wrong,
            'percent': percent,
            'total': total
        }
        return render(request, 'quizes/result.html', context)
    else:
        questions = Question.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'quizes/index.html', context)


def add_question(request):
    if request.user.is_staff:
        form = QuestionForm()
        if(request.method == 'POST'):
            form = QuestionForm(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'quizes/add_question.html', context)
    else:
        return redirect('quizes:index')
