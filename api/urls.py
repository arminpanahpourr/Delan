from django.urls import path
from .views import Login, Register
# from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    # path('login/', Login),
    path('register/', Register.as_view()),
    path('logout/', Logout.as_view()),

]
