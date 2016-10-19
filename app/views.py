from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from app.models import Profile, Operations
# from app.forms import ProfileUpdateForm
# Create your views here.


def func_add(number1, number2):
    return int(number1) + int(number2)


def func_sub(number1, number2):
    return int(number1) - int(number2)


def func_mult(number1, number2):
    return int(number1) * int(number2)


def func_div(number1, number2):
    return int(number1) / int(number2)


def index_view(request):
    if request.GET:
        number1 = request.GET["number1"]
        number2 = request.GET["number2"]
        functions = request.GET["functions"]
        if functions == "+":
            answer = func_add(number1, number2)
        if functions == "-":
            answer = func_sub(number1, number2)
        if functions == "*":
            answer = func_mult(number1, number2)
        if functions == "/":
            try:
                answer = func_div(number1, number2)
            except ZeroDivisionError:
                answer = 0

        Operations.objects.create(user=request.user, number1=number1,
                                  number2=number2, function=functions,
                                  answer=answer)

    else:
        answer = 0
        number1 = 0
        number2 = 0
        functions = 0

    context = {
        "answer": answer,
        "number1": number1,
        "number2": number2,
        "function": functions
    }
    return render(request, "index.html", context)


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class ProfileView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self):
        context = super().get_context_data()
        if self.request.user.profile.is_owner:
            context['operations'] = Operations.objects.all()
            return context
        else:
            context['operations'] = Operations.objects.filter(user=self.request.user)
            return context


# class UpdateProfileView(FormView):
#     model = Profile
#     form_class = ProfileUpdateForm
#     template_name = "profile_update_form.html"
#     success_url = "/"
#
#     def form_valid(self, form):
#         instance = form.save(commit=False)
#         instance.user = self.request.user
#         self.request.user.access_level = instance.access_level
#         form.save()
#         return super().form_valid(form)
