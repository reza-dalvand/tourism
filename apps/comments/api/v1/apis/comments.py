from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer


class CommentApi(ModelViewSet):
    """
    Comment Api (use as common for tours and hotels app)

    Parameters:
        -body
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
