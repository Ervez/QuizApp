from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin', admin.site.urls),
    path('addQuestion', addQuestion, name='addQuestion'),
    path('logout', logoutPage, name='logout'),
    path('quiz', question_view, name='question_view'),
    path('results', quiz_results, name='quiz_results'),
    path('', home, name='home'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
