from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login/login_form.html"
    success_url = "/"

    def get_success_url(self):
        super().get_success_url()
        try:
            pk = self.request.user.customers.id
            return reverse('customers:discount_code', args=(pk,))
        except:
            pass

        try:
            pk = self.request.user.staff.id
            return reverse('goods:user_search')
        except:
            messages.error(self.request, 'You are not registered as Customer and as Staff',
                           extra_tags='success')
            return ('/')


    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        messages.success(self.request, 'Congratulations you have logined  successfully to our site', extra_tags='success')
        return super(LoginView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.error(request, 'You are logout', extra_tags='info')
        return HttpResponseRedirect("/")




