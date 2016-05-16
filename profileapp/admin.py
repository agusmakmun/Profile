from django.contrib import admin
from profileapp.models import *

class Job_Experience_Admin(admin.TabularInline):
    model = Job_Experience
    extra = 1

class Education_Admin(admin.TabularInline):
    model = Education
    extra = 1

class Awards_Admin(admin.TabularInline):
    model = Awards
    extra = 1

class Resume_Admin(admin.TabularInline):
    model = Resume
    extra = 1

class Portfolio_Admin(admin.TabularInline):
    model = Portfolio
    extra = 1

class Skills_Admin(admin.TabularInline):
    model = Skills
    extra = 1

class Profile_Admin(admin.ModelAdmin):
    inlines = [ Job_Experience_Admin, Education_Admin, Awards_Admin, Resume_Admin, Portfolio_Admin, Skills_Admin ]
    save_on_top = True

    def has_add_permission(self, request):
        count = Profile.objects.all().count()
        if count == 0:
            return True
        return False

admin.site.register(Profile, Profile_Admin)