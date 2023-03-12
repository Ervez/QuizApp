from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('addQuestion', addQuestion, name='addQuestion'),
    path('login', loginPage, name='login'),
    path('logout', logoutPage, name='logout'),
    path('register', registerPage, name='register'),
    path('', question_view, name='question_view'),
    path('results', quiz_results, name='quiz_results'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
