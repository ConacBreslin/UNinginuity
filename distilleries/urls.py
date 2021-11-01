from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_distilleries, name='distilleries'),
    path('<distillery_id>', views.individual_distillery, name='individual_distillery'),
]