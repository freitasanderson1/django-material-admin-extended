from django.urls import path

from materialdash.admin.sites import site


urlpatterns = [
    path('', site.urls, name='base')
]
