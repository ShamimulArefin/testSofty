from django import forms
from .models import Subscription, ProjectContact

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('email',)

class ProjectContactForm(forms.ModelForm):
    class Meta:
        model = ProjectContact
        fields = '__all__'
