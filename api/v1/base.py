from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class DefaultPagination(PageNumberPagination):
    page_size = 100  # Default number of elements in each page
    page_size_query_param = 'page_size'
    max_page_size = 150  # Max number of elements in each page


class BaseModelViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    pagination_class = DefaultPagination
    authentication_classes = [JWTAuthentication]


class BaseModelWithUserViewSet(BaseModelViewSet):

    def get_queryset(self):
        queryset = super(BaseModelWithUserViewSet, self).get_queryset()
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """ This method is override to set user in Model """
        serializer.save(user=self.request.user)
