from rest_framework import serializers
from .models import Essays,Tarh,User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from fluent_comments.models import FluentComment
class EssaysSerializer(serializers.ModelSerializer):
    # username = serializers.SlugField(source="user.username")
    comments= serializers.SerializerMethodField()
    class Meta:
        model = Essays
        fields = ('title','user', 'context','rating','publishedDate','img','pk','comments')
        read_only_fields = ("user", )

    def get_comments(self,obj):
        essay_comment = FluentComment.objects.filter(object_pk = obj.id, parent_id = None)
        serializer = CommentSerializer(essay_comment,many=True)
        return serializer.data

class TarhSerializer(serializers.ModelSerializer):
    # username = serializers.SlugField(source="user.username")
    class Meta:
        model = Tarh
        fields = ( 'title',"user",'context','rating','publishedDate','img','pk')
        read_only_fields = ("user", )

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['email'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect email or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return {'user': user}


def validate_username(username):
    if User.objects.filter(**{'{}__iexact'.format(User.USERNAME_FIELD): username}).exists():
        raise ValidationError('User with this {} email already exists'.format(User.USERNAME_FIELD))
    return username

class UserSerializer(serializers.ModelSerializer):
    # Essays = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    Essays = EssaysSerializer(read_only=True,many=True)
    # Essays = serializers.CharField(source='get_Essay_object', read_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            'last_login',
            'email',
            'name',
            'is_active',
            'joined_at',
            'password',
            "BirthDate",
            "gender",
            "countries",
            "Mbti",
            "Essays"
        )
        read_only_fields = ('last_login', 'is_active', 'joined_at',"Essays")
        extra_kwargs = {
            'password': {'required': True, 'write_only': True},
            'name': {'required': True}
        }

    @staticmethod
    def validate_email(value):
        return validate_username(value)

    def create(self, validated_data):
        return User.objects.create_user(
                    validated_data.pop('email'),
                    validated_data.pop('password'),
                    **validated_data
                )

class ProfileSerializer(serializers.ModelSerializer):
    Essays = serializers.PrimaryKeyRelatedField(read_only=True,many=True)
    # Essays = EssaysSerializer(read_only=True,many=True)
    # Essays = serializers.CharField(source='get_Essay_object', read_only=True)
    class Meta:
        model = User
        fields = (
            'id',
            'last_login',
            'name',
            'is_active',
            'joined_at',
            "BirthDate",
            "gender",
            "countries",
            "Mbti",
            "Essays"
        )
        read_only_fields = ('last_login', 'is_active', 'joined_at',"Essays")

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(
            value,
            context=self.context)
        return serializer.data

class CommentSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    
    class Meta:
        model = FluentComment
        fields = (
            'comment',
            'id',
            'user_id',
            'parent_id',
            'object_pk',
            'children',
        )
    # def __init__(self, *args, **kwargs):
    #     super(CommentSerializer, self).__init__(*args, **kwargs)
    #     self.fields['parent_id'].read_only = False
