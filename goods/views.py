from django.shortcuts import render
from customers.models import Customers
from .models import Discount_code
from .forms import SeachForm, GoodForm
from staff.models import Staff
import hashlib
import random
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.contrib import messages


def user_search(request):
    context = {}
    if request.method == 'POST':
        form = SeachForm(request.POST)
        context["form"] = form

        if form.is_valid():
            print("isvalid")
            email = form.cleaned_data['email']
            user = Customers.objects.filter(user__email=email)
            try:
                pk = user[0].id
                context["users"] = user
                return HttpResponseRedirect(reverse('goods:discount', args=(pk,)))
            except:
                messages.error(request, 'Пользователь с таким E-mail в системе не зарегистрирован',
                               extra_tags='success')
            return HttpResponseRedirect(reverse('goods:user_search'))


    else:
        form = SeachForm()
        context = {"form": form}
    return render(request, "goods/customer.html", context)


def good_search(request, pk):
    context = {}
    user = Customers.objects.filter(id=pk)
    context["users"] = user[0]
    if request.method == 'POST':
        form2 = GoodForm(request.POST)
        context["form2"] = form2

        if form2.is_valid():
            print("isvalid")

            good = form2.cleaned_data['name']
            context["good"] = good
            salt = hashlib.sha1(str(random.random()).encode()).hexdigest()[:4]
            code = (salt[0]+'-'+salt[1]+'-'+salt[2]+'-'+salt[3]).upper()
            while Discount_code.objects.filter(code=code) == True:
                salt = hashlib.sha1(str(random.random()).encode()).hexdigest()[:4]
                code = (salt[0] + '-' + salt[1] + '-' + salt[2] + '-' + salt[3]).upper()
            context["code"] = code

            try:

                staff = Staff.objects.filter(user=request.user)
                new_descount_code = Discount_code(code=code,
                                                  good=good,
                                                  customer=user[0],
                                                  staff=staff[0])
                new_descount_code.save()
                context['result'] = 'Покупателю %s присвоен код %s' % (user[0], code)


            except:
                messages.error(request, 'Вы не зарегистрированы как персонал', extra_tags='success')
    else:
        form2 = GoodForm()
        context = {"form2": form2, "users": user[0]}

    return render(request, "goods/discount.html", context)

class DiscountsListlView(ListView):
    model = Discount_code
    context_object_name = 'discount_list'
    template_name = 'goods/discount_list.html'

