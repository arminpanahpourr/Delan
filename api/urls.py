from django.urls import path
from .views import Register, Logout

urlpatterns = [
    # path('login/', Login),
    path('register/', Register.as_view()),
    path('logout/', Logout.as_view()),

]
