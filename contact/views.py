from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


def contact(request):
    """
    A view to return the contact page and send emails alerting
    the admin about a new Contact Form been submitted.
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        customer_query = request.POST.get('message')
        if form.is_valid():
            form.save()

            # Send an email letting the admin know about a new form submission
            send_mail(
                'Time To Rent - New Contact Form',
                'You have a new contact form available to you on '
                'Time To Rent. \n\n\nCustomer Query:'
                f'\n\n{customer_query}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
            )

            messages.success(request, 'Email sent. We will be in touch soon.')
            return redirect(reverse('home'))
        else:
            messages.error(
                request,
                'Contact request failed. Check the form is valid')
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'contact/contact.html', context)
