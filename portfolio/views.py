import json

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from notebook.settings import EMAIL_HOST_USER
from portfolio.forms import ContactMailSend
from portfolio.functions import generate_form_errors
from portfolio.models import About, Ulli, Experience


def index(request):
    var_contact_form = ContactMailSend()
    about_dt = About.objects.all()
    title_two = Ulli.objects.filter(ul_name='My main Interests are:')
    title_three = Ulli.objects.filter(ul_name='My working philosophies:')
    title_four = Ulli.objects.filter(ul_name='Contact Details')
    experience_dt = Experience.objects.filter(section='Experience')
    education_dt = Experience.objects.filter(section='EDUCATION')
    context = {
        "caption": "Portfolio",
        "about": about_dt,
        "li_title_two": title_two,
        "li_title_three": title_three,
        "li_title_four": title_four,
        "experiences": experience_dt,
        "educations": education_dt,
        "contact_form": var_contact_form,
    }
    return HttpResponse(render(request, 'resumer/home.html', context))


def contacting(request):
    if request.method == "POST":
        j_form = ContactMailSend(request.POST)
        if j_form.is_valid():
            j_form.save()
            str_one = 'Hi, This is AbdulRahim K with you, your query is with me on this subject ' \
                      '' + str(j_form['air_subject'].value()) + 'and I will redirect to you soon.' \
                                                                '                                  ' \
                                                                '                                    ' \
                                                                'Thanks & Regards.'
            mail_subject = 'Welcome to Notebook'
            mail_message = str_one
            mail_recipient = str(j_form['air_email'].value())
            send_mail(mail_subject,
                      mail_message, EMAIL_HOST_USER, [mail_recipient], fail_silently=False)

            user_subject = str(j_form['air_subject'].value())
            user_message = str(j_form['air_message'].value())
            user_message = user_message + "                        His Name is : " \
                           + str(j_form['air_name'].value()) + "   His Mobile number: " \
                           + str(j_form['air_phone'].value())
            send_mail(user_subject,
                      user_message, EMAIL_HOST_USER, [EMAIL_HOST_USER], fail_silently=False)

            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Registration successfully created.",
            }
        else:
            message = generate_form_errors(j_form, formset=False)

            response_data = {
                "status": "a",
                "stable": "true",
                "title": "form validation error",
                "message": message,
            }

        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    else:
        return HttpResponse("Invalid Request")
