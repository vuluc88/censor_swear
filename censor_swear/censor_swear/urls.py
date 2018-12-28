from django.conf.urls import url, include
from rest_framework import routers
from censor_app.dialog import views as dialog_views

router = routers.DefaultRouter()
router.register(r'raw_dialogs', dialog_views.RawDialogViewSet)
router.register(r'censored_dialogs', dialog_views.CensoredDialogViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
