from django.urls import path
from . import views
urlpatterns = [
    path('add', views.AddExpense.as_view()),
    path('get', views.GetExpense.as_view()),
    path('delete/<int:id>', views.DeleteExpense.as_view()),
    path('update/<int:id>', views.UpdateExpense.as_view())
]