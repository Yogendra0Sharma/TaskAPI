from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings


from TaskApp import views

#Define API Routes
router = routers.DefaultRouter() #we will try with SimpleRouter or can use either or

#router = routers.SimpleRouter()

router.register(r'task', views.TaskViewSet)  #we have only on viewset
#router.register(r'due_task',views.DueTaskViewSet)
#router.register(r'completed_task',views.CompletedTaskViewSet)


urlpatterns = [

    url(r'^',include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
