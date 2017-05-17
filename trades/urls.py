from django.conf.urls import url
import views

urlpatterns = [
    url(r'^confirm/(?P<id>\d+)', views.postTradeMyProduct, name='postTradeMyProduct'),
    url(r'^(?P<id>\d+)$', views.traderequest, name='traderequest'),
   ]
