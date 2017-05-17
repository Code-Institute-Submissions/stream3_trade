from django.conf.urls import url
from .views import register, profile, logout, login
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from products.views import addMyProduct

import views

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^myprofile/$', views.get_details, name='get_details'),
    url(r'^myprofile/profile/myproducts$', views.postMyProduct, name='postMyProduct'),
    url(r'^myprofile/profile/myproduct/(?P<id>\d+)/$', views.postMyProductDetail, name='postMyProductDetail'),
    url(r'^myprofile/profile/create/$', views.create_profile, name='create_profile'),
    url(r'^myprofile/profile/edit/$', views.profileupdate, name='profileupdate'),
    url(r'^myprofile/profile/additem/$', addMyProduct, name='addMyProduct'),
    url(r'^myprofile/profile/offers/$', views.alltradeoffers, name='alltradeoffers'),
    url(r'^myprofile/profile/offers/(?P<id>\d+)$', views.refusetrade, name='refusetrade'),

    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password/reset/$', password_reset,
        {'post_reset_redirect': '/user/password/reset/done/'}, name='password_reset'),
    url(r'^password/reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
     password_reset_confirm, {'post_reset_redirect': '/user/password/done/'}, name='password_reset_confirm'),
    url(r'^password/done/$', password_reset_complete, name='password_reset_complete'),
]