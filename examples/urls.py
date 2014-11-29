from django.conf.urls import include, url
from django.contrib import admin

from karenina import modules
from karenina.workflow import workflow

from tests.examples.helloworld.flows import HelloWorldFlow
from tests.examples.shipment.flows import ShipmentFlow
from tests.examples.customnode.flows import DynamicSplitFlow

workflow.register(HelloWorldFlow)
workflow.register(ShipmentFlow)
workflow.register(DynamicSplitFlow)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^management/', include('karenina.management.urls')),
    url(r'^', include(modules.default_registry.urls)),
]


from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect


def users(request):
    return {
        'users': User.objects.filter(is_active=True).order_by('-username')
    }


def login_as(request):
    user = request.REQUEST.get('user_pk', None)
    if user:
        try:
            user = User.objects.get(pk=user)
        except User.DoesNotExist:
            pass

    if user:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
    else:
        logout(request)

    return redirect('/workflow/')


urlpatterns += [url(r'^login_as/$', login_as, name="login_as")]
