from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView, CreateView, View, UpdateView, DeleteView

from viewer.models.expence import Expence
from viewer.models.budget import Budget
from viewer.models.profile import Profile
from viewer.forms import SignUpForm, CreateExpenseForm, UpdateExpenseForm, UpdateBudgetForm, UpdateProfileForm


class ExpenseCreateView(CreateView):
    model = Expence
    form_class = CreateExpenseForm
    template_name = "add_edit_expense.html"
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        kwargs = super(ExpenseCreateView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs

    def form_invalid(self, form):
        return render(
            self.request, template_name="add_edit_expense.html",
            context={
                "form": form
            }
        )





class ExpenseEditView(UpdateView):
    model = Expence
    template_name = "add_edit_expense.html"
    form_class = UpdateExpenseForm
    success_url = reverse_lazy("home")


class ExpenseDeleteView(DeleteView):
    model = Expence
    success_url = reverse_lazy("home")
    template_name = "delete_expense.html"


class ProfileView(LoginRequiredMixin, View):
    model = Expence

    def get(self, request):
        categories = [category[1] for category in Expence.Catagory.choices]
        budget = self.request.user.profile.budget
        queryset = Expence.objects.filter(budget=budget)
        form = CreateExpenseForm

        return render(
            request, template_name="profile.html",
            context={
                "expenses": queryset,
                "budget": budget,
                "categories": categories,
                "form": form
            }
        )


class SubmitableLoginView(LoginView):
    template_name = "form.html"
    success_url = reverse_lazy("home")


class SubmitableSignUpView(CreateView):
    form_class = SignUpForm
    template_name = "form.html"
    success_url = reverse_lazy("login")


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = "form.html"
    success_url = reverse_lazy("home")


class WelcomeView(TemplateView):
    template_name = "home.html"


class ExpenceDetailView(DetailView):
    model = Expence
    template_name = "expence_detail.html"
    success_url = reverse_lazy("expence_detail")


class CategoryDetailView(View):
    model = Expence
    success_url = reverse_lazy("category_detail")

    def get(self, request, category_short):
        budget = self.request.user.profile.budget
        all_expenses = Expence.objects.filter(budget=budget)
        category_expenses = all_expenses.filter(category=category_short)
        category = category_short
        total_expenses = 0
        total_category_expenses = 0
        total_budget = self.request.user.profile.budget.total_budget

        for expense in all_expenses:
            total_expenses += expense.value

        for expense in category_expenses:
            total_category_expenses += expense.value

        category_to_all = round(total_category_expenses / total_expenses, 2)
        category_to_budget = round(total_category_expenses / total_budget, 2)

        return render(
            request, template_name="category_detail.html",
            context={
                "budget": budget,
                "all_expenses": all_expenses,
                "category_expenses": category_expenses,
                "category": category,
                "category_to_all": category_to_all,
                "category_to_budget": category_to_budget,
                "total_category_expenses": total_category_expenses
            }
        )


class DeleteProfileView(DeleteView):
    model = User
    template_name = "delete_profile.html"
    success_url = reverse_lazy("welcome")


class EditProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = "form.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        profile_id = self.request.user.profile.id
        return get_object_or_404(Profile, id=profile_id)


class EditBudgetView(UpdateView):
    form_class = UpdateBudgetForm
    # fields = ["name", "total_budget"]
    template_name = "edit_budget.html"
    success_url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        budget_id = self.request.user.profile.budget.id
        return get_object_or_404(Budget, id=budget_id)

    def form_valid(self, form):
        return super().form_valid(form)
