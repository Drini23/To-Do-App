from django.db import router
from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from . import views


route = DefaultRouter()
route.register('task', views.TaskViewSet)
urlpatterns = route.urls

#tasks_router = routers.NestedDefaultRouter(
 #   router, 'task', lookup='task') KEMI PROBLEM ME NESTEDROUTERS NUK I IMPORTOJM DOT






