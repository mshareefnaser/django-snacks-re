from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Snacks
class HomeView(TemplateView):
    template_name = "home.html"

class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snacks
    context_object_name = "snacks"


class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snacks