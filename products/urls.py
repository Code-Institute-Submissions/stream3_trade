from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.all_products, name='products'),
    url(r'^profile/(?P<id>\d+)/$', views.product_detail, name='product_detail'),
    url(r'^profile/(?P<id>\d+)', views.profile_detail, name='profile_detail'),
    url(r'^profile/items/(?P<id>\d+)$', views.others_products, name='others_products'),
    url(r'^profile/items/delete/(?P<id>\d+)', views.deleterequest, name='deleterequest'),
    url(r'^profile/items/delete/yes/(?P<id>\d+)$', views.deleteobject, name='deleteobject'),
    url(r'^profile/items/nodelete/$', views.deleteobjectno, name='deleteobjectno'),


]

