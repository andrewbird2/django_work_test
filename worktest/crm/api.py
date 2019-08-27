from rest_framework import serializers, viewsets, routers

from worktest.crm.models import Customer


# Serializers define the API representation.
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'email']


# ViewSets define the view behavior.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
