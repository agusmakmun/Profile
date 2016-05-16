from django.views import generic
from django.shortcuts import get_object_or_404
from profileapp.models import Profile

class Profile_View(generic.DetailView):
    template_name = 'profileapp/profile.html'

    def get_object(self):
        try:
            get_model = Profile.objects.first()
            return get_object_or_404(Profile, pk=get_model.pk)
        except: pass

    def get_context_data(self, **kwargs):
        context = super(Profile_View, self).get_context_data(**kwargs)
        return context