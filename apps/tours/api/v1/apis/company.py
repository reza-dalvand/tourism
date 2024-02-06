from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.core.permissions.check_tour_company_owner import CheckTourCompanyOwner
from apps.tours.models import TourismCompany
from apps.tours.serializers import TourismCompanySerializer


class TourismCompanyApi(ModelViewSet):
    """
    create change or ... after checking user is allowed
    to access this operation (with CheckTourCompanyOwner)

    """

    permission_classes = (IsAuthenticated, CheckTourCompanyOwner)
    queryset = TourismCompany.objects.all()
    serializer_class = TourismCompanySerializer
