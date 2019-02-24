from rest_framework import routers
from testapi import views
from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(r'api1', views.SendEmailViewSet,base_name='SendEmailViewSet')
router.register(r'getdata', views.GetDataViewSet,base_name='GetDataViewSet')
# router.register(r'login', views.LoginViewSet,base_name='userlogin')
# router.register(r'getdata', views.GetDataViewSet,base_name='getdata')
urlpatterns = router.urls