# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Question, Choice
import simplejson
from django.views import generic
from .forms import PersonForm
from django.db.models import Count


class IndexView(generic.ListView):
    template_name = 'myApp/index.html'
    context_object_name = 'data'

    def get_queryset(self):
        import pdb;pdb.set_trace()

        ########## Use of model_set instead of related_name ##########
        # bb = Question.objects.get(id=1)
        # mm = bb.choice_set.all()
        ##################################

        ######### USE  OF ANNOTATE #########

        # mm = Question.objects.annotate(Count('choices'))
        # print(mm[1].choices__count)

        #####################################

    	latest_question_list = Question.objects.order_by('-pub_date')

    	lst_question_answers = []
    	dct_data = {}
    	for ques in latest_question_list:
            choices = ques.choices.all()
            # import pdb;pdb.set_trace()
            dct_data['choices'] = [str(choice.choice_text) for choice in choices]
            dct_data['question'] = ques.question_text
            lst_question_answers.append(dct_data)
            dct_data = {}
	return lst_question_answers

def detail(request, question_id, answer_id):
	context_data = str(question_id) + ':' + str(answer_id)
	return HttpResponse(context_data)

def about(request):
    return render(request, 'myApp/about.html', {})

def person(request):
    form = PersonForm()
    return render(request, 'myApp/about.html', {'form': form})