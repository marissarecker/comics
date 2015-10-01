from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^archives/$', views.ComicStripListView.as_view(), name='comic-strip-list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^(?P<slug>[^/]+)/$', views.ComicStripDetailView.as_view(), name='comic-strip-detail')
]
