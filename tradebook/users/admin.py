from django.contrib import admin
from users.models import User, InvestorProfile, AdministratorProfile
# Register your models here.

admin.site.register(User)
admin.site.register(AdministratorProfile)
admin.site.register(InvestorProfile)
