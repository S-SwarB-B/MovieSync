from django.shortcuts import render, get_object_or_404, redirect

from .forms import RegisterForm
from .models import Users

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # теперь это работает
            user.save()
            return render(request, 'accounts/register_done.html')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})