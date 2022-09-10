from django.contrib import admin
from .models import ShowService, ServiceStack, TeamMember, Subscription,ProjectContact

# Register your models here.

admin.site.register(ShowService)
admin.site.register(ServiceStack)
admin.site.register(TeamMember)
admin.site.register(Subscription)
admin.site.register(ProjectContact)