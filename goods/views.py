from django.shortcuts import render
from customers.models import Customers
from .models import Good, Discount_code
from .forms import SeachForm, GoodForm
from staff.models import Staff
import hashlib
import random

# Create your views here.
def discount_codes(request):
    context = {}
    if request.method == 'POST':
        form1 = SeachForm(request.POST)
        form2 = GoodForm(request.POST)
        context["form1"] = form1
        context["form2"] = form2

        if form1.is_valid() and form2.is_valid():
            print("isvalid")
            email = form1.cleaned_data['email']
            user = Customers.objects.filter(user__email=email)
            context["users"] = user
            good = form2.cleaned_data['name']
            context["good"] = good
            salt = hashlib.sha1(str(random.random()).encode()).hexdigest()[:4]
            code = (salt[0]+'-'+salt[1]+'-'+salt[2]+'-'+salt[3]).upper()
            context["code"] = code
            staff = Staff.objects.filter(user=request.user)
            new_descount_code = Discount_code(code=code,
                                              good=good,
                                              customer=user[0],
                                              staff=staff[0])
            new_descount_code.save()
            context["code"] = code
    else:
        form1 = SeachForm()
        form2 = GoodForm()
        context = {"form1": form1, "form2": form2}

    return render(request, "goods/results.html", context)

'''
class CustomerSearchView(FormView):
    model = Customer
    form_class = SeachForm
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        print("isvalid")
        email = form.cleaned_data['email']
        users = Customers.objects.filter(user__email__contains=email)
        context["users"] = users
        print(users)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        return context  '''

