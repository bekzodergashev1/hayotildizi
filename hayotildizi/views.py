from django.shortcuts import render, redirect
from django.views.generic import CreateView
from hayotildizi.forms import GuestForm
from hayotildizi.utils import send_bot_message


class HomeView(CreateView):
    template_name = 'main/index.html'
    success_url = 'home:home_index'
    form_class = GuestForm

    def form_valid(self, form):
        guest = form.save()

        send_bot_message(form.cleaned_data)
        return redirect(self.success_url)
