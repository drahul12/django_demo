from django.conf.urls import url
import views

urlpatterns = [
    url(r'^(?P<question_id>[0-9]+)/(?P<answer_id>[A-Z]+)/$', views.detail, name='detail'),
]
