# contact/views.py
from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'contact/contact_form.html', {'form': form})


def success_page_view(request):
    return render(request, 'contact/success_page.html')
