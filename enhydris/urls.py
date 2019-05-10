from django.contrib import admin
from django.urls import include, path
from django.views.generic import View

from enhydris import views
from enhydris.api import urls as enhydris_api_urls

admin.autodiscover()

urlpatterns = [
    path("", views.StationListView.as_view(), name="station_list"),
    path(
        "stations/kml/",
        views.StationListView.as_view(template_name="enhydris/placemarks.kml"),
    ),
    path("admin/", admin.site.urls),
    path("api/", include(enhydris_api_urls)),
]

# A view that does nothing, that will be used in some fake patterns below
_null_view = View.as_view()

# When a user registers, an email is sent, containing a link that the user has to click
# in order to confirm the email. In order to create that link, django-rest-auth uses
# reverse("account_confirm_email"). So we include that in the urlpatterns, although it's
# not actually being used and should not be served by Django. The web server should be
# configured to route that URL to the front-end, which should then POST to the
# verify-email API endpoint in order to perform the actual verification.
urlpatterns += [
    path("confirm-email/<str:key>/", _null_view, name="account_confirm_email")
]

# When a user registers, django-allauth runs reverse("account_email_verification_sent")
# in order to redirect to a page that says "We sent an email verification, click the
# link in that email". In our case, registration is done by POST to an API endpoint,
# which merely responds with "201". However, because something in django-allauth or in
# django-rest-auth is suboptimal, django-allauth still runs this reverse() (whose return
# value is eventually not used). We therefore add this URL so that the reverse() doesn't
# raise a NoReverseMatch exception. It might have been more correct to fix that in a
# custom django-allauth adapter, but all this is a big mess anyway (see
# https://github.com/Tivix/django-rest-auth/issues/292), so it's not worth it.
urlpatterns += [
    path(
        "dummy/account-email-verification/",
        _null_view,
        name="account_email_verification_sent",
    )
]
