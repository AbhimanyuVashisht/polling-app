from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# from django.http import Http404
from .models import Choice, Questions


def index(request):
    latest_question_list = Questions.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # output = ','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def details(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    # try:
    #     question = Questions.objects.get(pk=question_id)
    # except Questions.DoesNotExist:
    #     raise Http404("Question does not exist")
    # return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/detail.html', question)


def results(request, question_id):
    # response = "You're looking at the results of question %s."
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    # return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    # return HttpResponse("You're voting on question %s." % question_id)

