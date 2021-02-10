from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.contrib.auth import login, logout
from rest_framework import viewsets,views,response,generics,mixins,status,exceptions
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,BasePermission,SAFE_METHODS
from .models import Essays, Tarh, User
from .serializers import EssaysSerializer, TarhSerializer, LoginSerializer, UserSerializer, ProfileSerializer, CommentSerializer
from django.http import HttpResponse
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from datetime import datetime
from fluent_comments.models import FluentComment
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from threadedcomments.models import ThreadedComment 
# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))

class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    message = 'not owner'
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj == request.user


class UpdateModelMixin(object):
    """
    Update a model instance.
    """
    def partial_update(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(request.data,status=status.HTTP_202_ACCEPTED)

    def perform_update(self, serializer):
        serializer.save()


class EssaysViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Essays to be viewed or edited.
    """
    queryset = Essays.objects.all()
    serializer_class = EssaysSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (AllowAny,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def retrieve(self, request, pk=None):
        essay = self.get_object()
        serializer = self.serializer_class(essay,context={'request': request})
        return Response(serializer.data)

    


class TarhViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tarh to be viewed or edited.
    """
    queryset = Tarh.objects.all()
    serializer_class = TarhSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LoginView(views.APIView):
    permission_classes = (AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return response.Response(UserSerializer(user).data)


class LogoutView(views.APIView):
    def post(self, request):
        logout(request)
        return response.Response()


class RegisterUserView(generics.CreateAPIView,):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    def perform_create(self, serializer):
        if self.request.user != AnonymousUser:
            logout(self.request)
        user = serializer.save()
        # user.backend = settings.AUTHENTICATION_BACKENDS[0]
        login(self.request, user)

# class UserProfileRetriveView(generics.RetrieveAPIView):
#     serializer_class = UserProfileSerializer
#     # permission_classes = (AllowA)
#     lookup_field = 'pk'
#     authentication_classes = (SessionAuthentication,)
#     def get_object(self,*args, **kwargs):
#         return self.request.user



class ProfileView(viewsets.GenericViewSet,
            mixins.RetrieveModelMixin,
            mixins.ListModelMixin,
            UpdateModelMixin):
    """
    API endpoint that allows users profiles to be viewed or updated.
    """
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        AUser = get_object_or_404(queryset, pk=pk)
        serializer = ProfileSerializer(AUser)
        return Response(serializer.data)
    def perform_update(self, serializer):
        if serializer.data is not None:
            raise exceptions.ValidationError()
        serializer.save(user=self.request.user)
    # def update(self, *args, **kwargs):
    #     raise exceptions.MethodNotAllowed("POST", detail="Use PATCH")
    # def get_permissions(self):
    #     """
    #     Instantiates and returns the list of permissions that this view requires.
    #     """
    #     if self.action == 'retrieve' :
    #         permission_classes = [IsOwnerOrReadOnly]
    #     else:
    #         permission_classes = [AllowAny]
    #     return [permission() for permission in permission_classes]
# class UserView(generics.RetrieveAPIView):
#     serializer_class = UserSerializer
#     lookup_field = 'pk'

#     def get_object(self, *args, **kwargs):
#         return self.request.user
class CommentViewSet(viewsets.GenericViewSet,
                mixins.RetrieveModelMixin,
                mixins.ListModelMixin,
                mixins.CreateModelMixin
                ):
    queryset = FluentComment.objects.filter(parent_id = None)
    serializer_class = CommentSerializer
    # permission_classes = [AllowAny]
    # authentication_classes = [TokenAuthentication]    
    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data = self.request.data
            comment = data.get('comment')
            try:
                int(data.get('object_pk'))
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            try:
                Essays.objects.get(pk=data.get('object_pk'))
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                essay = data.get('object_pk')
            # if not isinstance(essay, int):
            
            if 'parent_id' not in data or data.get('parent_id') == '' or data.get('parent_id') == None:
                parent = None
            else:
                try:
                    int(data.get('parent_id'))
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    try:
                        ThreadedComment.objects.get(pk=data.get('parent_id'))
                    except:
                        return Response(status=status.HTTP_404_NOT_FOUND)
                    else:
                        parent = data.get('parent_id')

            
            submit_date = datetime.now()
            content = ContentType.objects.get(model="essays").pk
            comment = FluentComment.objects.create(
                object_pk=essay,
                comment=comment,
                submit_date=submit_date,
                content_type_id=content,
                user_id = self.request.user.id,
                site_id=1,
                parent_id=parent,
                
                )
            serializer = CommentSerializer(comment,context=  {'request': request})
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)