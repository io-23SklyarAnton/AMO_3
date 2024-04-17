from django.shortcuts import render
from django.views.generic import FormView

from algorithm.forms import DrawGraphForm
from algorithm.services.graphs import draw_function_and_mistake_graphs


class ShowVariantGraphs(FormView):
    form_class = DrawGraphForm
    template_name = 'graph.html'
    success_url = '#'

    def form_valid(self, form):
        cd = form.cleaned_data
        a, b, function = cd['a'], cd['b'], cd['function']
        draw_function_and_mistake_graphs(a, b, function)
        return super().form_valid(form)
