from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Requirement#, CreateRequirement
from django.forms.models import model_to_dict


# Create your views here.
class RequirementIndex(generic.ListView):
    model = Requirement
    template_name = 'requirements/index.html'
    context_object_name = 'requirement_list'
    paginate_by = 10

    def get_queryset(self):
        return Requirement.objects.all()

class RequirementDetail(generic.DetailView):
    model = Requirement
    template_name = 'requirements/detail.html'

    # Add a dictionary containing the model information to the context when
    # rendering the view.
    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    requirement_object_dictionary = Requirement.objects.filter(id=context['requirement'].id).values()[0]
    #    context['requirement_object'] = requirement_object_dictionary
    #    return context

class RequirementUpdate(generic.UpdateView):
    model = Requirement
    template_name = 'requirements/edit.html'
    fields = [
        'description',
        'parent',
        'is_constraint',
        'min_measure_of_effectiveness',
        'target_measure_of_effectiveness',
        'rationale',
        'remarks',
        'acceptance_criteria_type',
        'priority',
        'status'
    ]

class RequirementCreate(generic.CreateView):
    model = Requirement
    template_name = 'requirements/create.html'
    fields = [
        'description',
        'parent',
        'is_constraint',
        'min_measure_of_effectiveness',
        'target_measure_of_effectiveness',
        'rationale',
        'remarks',
        'acceptance_criteria_type',
        'priority',
        'status'
    ]
