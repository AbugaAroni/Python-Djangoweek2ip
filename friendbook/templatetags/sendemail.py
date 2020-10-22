from django import template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag
def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to the FriendBook App'
    sender = 'lamepimpalla@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/newsemail.txt',{"name": name})
    html_content = render_to_string('email/newsemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
