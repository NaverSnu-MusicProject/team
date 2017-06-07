# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from propose import views
urlpatterns = [
    url(r'^test/$', views.test),
    url(r'^track/$', views.TrackList.as_view()),
    url(r'^track/(?P<pk>[0-9A-Z]+)/$',views.TrackDetail.as_view()),
    url(r'^tag/$',views.TagList.as_view()),
    url(r'^tag/(?P<pk>[0-9]+)/$',views.TagDetail.as_view()),
    url(r'^mtm/$', views.MTMList.as_view()),
    url(r'^mtm/(?P<pk>[0-9]+)/$',views.MTMDetail.as_view()),
    url(r'^play/$',views.PlayList.as_view()),
    url(r'^play/(?P<pk>[0-9]+)/$',views.PlayDetail.as_view()),
    url(r'^address/$',views.AddressList.as_view()),
    url(r'^address/(?P<pk>[0-9ㄱ-힣]+)/$',views.AddressDetail.as_view()),
    url(r'^address/(?P<pk>[0-9ㄱ-힣]+)/proposal/$',views.address_proposal_list),
]
