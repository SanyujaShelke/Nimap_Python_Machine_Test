from django.urls import path
from .views import ClientListCreate, ClientRetrieveUpdateDestroy, ProjectListCreate, ProjectRetrieveUpdateDestroy, UserProjectsList

urlpatterns = [
    path('clients/', ClientListCreate.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroy.as_view(), name='client-detail'),
    path('clients/<int:pk>/projects/', ProjectListCreate.as_view(), name='client-project-list'),
    path('projects/', UserProjectsList.as_view(), name='user-project-list'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroy.as_view(), name='project-detail'),
]
