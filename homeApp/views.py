from django.shortcuts import render
from .models import ShowService, ServiceStack, TeamMember, Subscription
from . import forms

# Create your views here.

def index(request):
    dict={
        'title':'SoftyIt',
        'hero_head':'Better Digital Experience With SoftyIT',
        'hero_desc':'Make us your technology partner to get innovative solutions',
        'count_client':10,
        'count_project':21,
        'count_hour':70,
        'count_worker':6,
    }

    # services
    services = ShowService.objects.all()
    stacks = ServiceStack.objects.all()
    l1 = stacks[0].service_stacks.split(',')
    l2 = stacks[0].service_stacks_icons.split(',')
    templ = stacks[0].service_stacks_icons_color.split(',')
    l3 = []
    for i in templ:
        l3.append('style=color:'+i+';')
    stk = zip(l1, l2, l3)
    dict.update({'services':services,'stacks':stk, })

    # team
    team = TeamMember.objects.all()
    dict.update({'team':team})

    #Subscription
    if request.method == 'POST':
        form = forms.SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            dict.update({'success_sub':'Subscribed Successfully!'})
    
    return render(request, 'homeApp/index.html', context=dict)


# contact page
def contact(request):
    dict = {}
    if request.method == 'POST':
        contactForm = forms.ProjectContactForm(request.POST)
        subscribeForm = forms.SubscriptionForm(request.POST)
        if contactForm.is_valid():
            contactForm.save()
            dict.update({'success':'Message sent successfully!'})
        if subscribeForm.is_valid():
            subscribeForm.save()
    return render(request, 'homeApp/contact.html', context=dict)
