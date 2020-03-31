from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Tour, Hotel, Article, Order, Message
from django.views.generic.edit import FormView
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import login, logout
from django import forms
from datetime import datetime
from django.views.generic.base import View
import templates

app_url = '/tours/'

def individual(request, hotel_id):
    message = None

    if 'message' in request.GET:
        message = request.GET['message']

    return render(
        request,
        'hotel.html',
        {
            'hotel': Hotel.objects.get(id=hotel_id),
            'message': message,
            'latest_messages':
                Message.objects
                .filter(chat_id=hotel_id)
                .order_by('-pub_date')[:5]

        }
    )


def main(request):
    message = None

    if 'message' in request.GET:
        message = request.GET['message']

    return render(
        request,
        'main_page.html',
        {
            'first_art': Article.objects.all()[0],
            'articles': Article.objects.all()[1:],
            'message': message
        }
    )


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = app_url + 'login/'
    template_name = 'reg/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'reg/login.html'
    success_url = app_url

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(app_url)


class PasswordChangeView(FormView):
    form_class = PasswordChangeForm
    template_name = 'reg/ password_change_form.html'
    success_url = app_url + 'login/'

    def get_form_kwargs(self):
        kwargs = super(PasswordChangeView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        if self.request.method == 'POST':
            kwargs['data'] = self.request.POST
        return kwargs

    def form_valid(self, form):
        form.save()
        return super(PasswordChangeView, self).form_valid(form)

def post(request, hotel_id):
    msg = Message()
    msg.author = request.user
    msg.chat = get_object_or_404(Hotel, pk=hotel_id)
    msg.message = request.POST['message']
    msg.pub_date = datetime.now()
    msg.save()
    return HttpResponseRedirect(app_url + 'hotels/' + str(hotel_id))


def tours(request):
    message = None
    search_inf = request.GET.get('tours_search', '')
    tours = []
    if search_inf:
        tours = Tour.objects.filter(
            Q(tour_name__icontains=search_inf) | Q(country__icontains=search_inf))
        print(tours.count)
    else:
        tours = Tour.objects.all()
        print(type(tours))

    if tours.count() == 0:
        tours = Tour.objects.all()
    paginator = Paginator(tours, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    if 'message' in request.GET:
        message = request.GET['message']

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    return render(
        request,
        'tours.html',
        {
            'page_obj': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url,
            'message': message
        }
    )


def index(request):
    message = None
    search_inf = request.GET.get('hotels_search', '')
    hotels = []
    if search_inf:
        hotels = Hotel.objects.filter(
            Q(hotel_name__icontains=search_inf) | Q(country__icontains=search_inf))
        print(hotels.count)
    else:
        hotels = Hotel.objects.all()
        print(type(hotels))

    if hotels.count() == 0:
        hotels = Hotel.objects.all()
    paginator = Paginator(hotels, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    if 'message' in request.GET:
        message = request.GET['message']

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    return render(
        request,
        'hotels.html',
        {
            'page_obj': page,
            'is_paginated': is_paginated,
            'next_url': next_url,
            'prev_url': prev_url,
            'message': message
        }
    )


def individual_tour(request, tour_id):
    if request.method == 'POST':
        spam = Order()
        spam.name = request.POST.get('name')
        spam.surname = request.POST.get('surname')
        spam.mail = request.POST.get('mail')
        spam.phone = request.POST.get('phone')
        spam.place = request.POST.get('place')
        ll = request.POST.get('value')
        spam.tour = Tour.objects.get(id=tour_id)
        spam.save()
        message = None
        userform = UserForm()
        if 'message' in request.GET:
            message = request.GET['message']

        return render(
            request,
            'tour.html',
            {
                'tour': Tour.objects.get(id=tour_id),
                'message': message,
                'latest_messages':
                    Message.objects
                .filter(chat_id=tour_id)
                .order_by('-pub_date')[:5],
                'form': userform

            }
        )
    else:
        message = None
        userform = UserForm()
        if 'message' in request.GET:
            message = request.GET['message']

        return render(
            request,
            'tour.html',
            {
                'tour': Tour.objects.get(id=tour_id),
                'message': message,
                'latest_messages':
                    Message.objects
                    .filter(chat_id=tour_id)
                    .order_by('-pub_date')[:5],
                    'form': userform

            }
        )


class UserForm(forms.Form):
    name = forms.CharField(label='Имя')
    surname = forms.CharField(label='Фамилия')
    mail = forms.EmailField(label='Почта')
    phone = forms.CharField(label='Телефон')
    place = forms.IntegerField(label='Количество мест')


def admin(request):
    message = None

    if 'message' in request.GET:
        message = request.GET['message']

    return render(
        request,
        'adminpanel.html',
        {
            'message': message,
            'orders': Order.objects.all()
        }
    )


def delete_order_admin(request, order_id):
    ord = Order.objects.get(id=order_id)
    ord.delete()
    return HttpResponseRedirect(app_url + 'admin/')
