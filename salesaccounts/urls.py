
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
#from django.urls import reverse
from django.views.generic.base import RedirectView

#from . import views as risktypes_views
from salesaccounts.views import *

router = DefaultRouter(trailing_slash=False)
#router.register(r'account', AccountViewSet, base_name="account")
#router.register(r'person', PersonViewSet, base_name="person")

urlpatterns = [
    # API URIs
	url(r'^get_current_directory/$', get_current_directory, name='get_current_directory'),
	url(r'^import_leads/$', import_leads, name='import_leads'),
	url(r'^export_leads/$', export_leads, name='export_leads'),
	url(r'^import_services/$', import_services, name='import_services'),
	url(r'^import_accounts/$', import_accounts, name='import_accounts'),
	#url(r'^import_cremployee/$', import_cremployee, name='import_cremployee'),
	#url(r'^$', RedirectView.as_view(url=reverse('admin:index'))),
    #url(r'', include(router.urls)),
    url(r'^salesaccounts-auth/', include('rest_framework.urls', namespace='rest_framework')),
   	url(r'^users/$',  UserList.as_view(),name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user-detail'),
	#url(r'^index/(?P<pk>[0-9]+)/$', index, name='index'),
]
