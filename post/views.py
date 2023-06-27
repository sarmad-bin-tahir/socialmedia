from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from api.permissions import CanUpdateDeletePosts
from post.serializer import PostSerializer, PostGetSerializer, PostLikeUnlikeSerializer, PostLikeUnlikeGetSerializer
from post.models import Post, PostLikeUnlike
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, CanUpdateDeletePosts]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return PostGetSerializer
        else:
            return self.serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post = self.perform_create(serializer)
        post_serializer = PostGetSerializer(post, many=False)
        headers = self.get_success_headers(post_serializer.data)
        return Response(post_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        post = Post.objects.create(
            text=serializer.validated_data.get('text', ''),
            user_id=self.request.user
        )
        PostLikeUnlike.objects.create(post_id=post)
        return post


class PostLikeUnlikeView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostLikeUnlikeSerializer

    def put(self, request):
        try:
            data = request.data
            obj = PostLikeUnlike.objects.get(post_id=data.get('post_id'))
            obj.reaction = data.get('reaction')
            obj.user_id = request.user
            obj.save()
            serializer = PostLikeUnlikeGetSerializer(obj, many=False)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
