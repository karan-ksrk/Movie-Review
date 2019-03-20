from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('AddMovie', views.addmovie, name='addmovie'),
    path('submission', views.submission, name='submission'),
    path('detail/<int:movie_id>', views.detail, name='detail'),
    path('login', LoginView.as_view(), name='login'), 
    path('logout', LogoutView.as_view(), name='logout'), 
    path('category/<int:cat_id>', views.Categorys, name='category'),
    
  
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)