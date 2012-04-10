from django.conf.urls.defaults import patterns, url

from extjs4.views import Extjs4AppView

urlpatterns = patterns('generic_extjs4_app',
                       url(r'^$', Extjs4AppView.as_view(title='Really simple app')),
                      )
