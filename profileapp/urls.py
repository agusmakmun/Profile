from django.conf.urls import include, url
from profileapp.views import Profile_View

urlpatterns = [
    url(r'^$', Profile_View.as_view(), name="home_page"),
]
