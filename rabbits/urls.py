from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.list_detail import object_list

from django.contrib import admin
admin.autodiscover()

from pinax.apps.account.openid_consumer import PinaxConsumer

from homepage.views import homepage
from package.views import package_autocomplete, category

handler500 = "pinax.views.server_error"


urlpatterns = patterns("",

    url(r"^$", homepage, name="home"),

    
    url(r"^admin/invite_user/$", "pinax.apps.signup_codes.views.admin_invite_user", name="admin_invite_user"),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^about/", include("about.urls")),
    url(r"^account/", include("pinax.apps.account.urls")),
    url(r"^openid/(.*)", PinaxConsumer()),
    url(r"^profiles/", include("idios.urls")),
    url(r"^notices/", include("notification.urls")),
    url(r"^announcements/", include("announcements.urls")),
    url(r"^package/", include("package.urls")),
    url(r"^grid/", include("grid.urls")),    
    
    url(r"^category/(?P<slug>[a-z0-9\-\_]+)/$", category, name="category"),        
    
    url(
        regex = '^autocomplete/package/$',
        view = package_autocomplete,
        name    = 'package_autocomplete',        
    )
    
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
