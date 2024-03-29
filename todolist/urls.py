from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from todo.api import TaskResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(TaskResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
