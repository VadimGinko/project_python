from django.conf.urls import url

from . import views
import templates
app_name = 'tours'
urlpatterns = [
    url(r'^hotels/$', views.index, name='index'),
    url(r'^$', views.main, name='main'),
    url(r'^hotels/([0-9]+)/$', views.individual, name='individual'),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^password-change/', views.PasswordChangeView.as_view()),
    url(r'^hotels/([0-9]+)/post/$', views.post, name='post'),
    url(r'^tour/$', views.tours, name='tour'),
    url(r'^tour/([0-9]+)/$', views.individual_tour, name='individual'),
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^admin/([0-9]+)/$', views.delete_order_admin, name='delete_order_admin'),
]
