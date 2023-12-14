# join_community/views.py
from django.shortcuts import render, redirect
from .forms import SignUpForm, SubscriptionForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            return redirect('join_community:subscribe')
    else:
        form = SignUpForm()

    return render(request, 'join_community/signup.html', {'form': form})


def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('join_community:success')

    form = SubscriptionForm(instance=request.user)
    return render(request, 'join_community/subscribe.html', {'form': form})


def success(request):
    return render(request, 'join_community/success.html')
