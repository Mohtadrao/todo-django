from django.urls import path, include
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name = 'addTask'),
    path('mark_as_done/<int:pk>', views.markDone, name = 'markDone'),
    path('unmark_as_done/<int:pk>', views.unmarkDone, name = 'unmarkDone'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
]