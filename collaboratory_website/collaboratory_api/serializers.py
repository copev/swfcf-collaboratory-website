#serializers.py

from rest_framework import serializers
from .models import Region, Role, Cause, User, Organization, Event, Channel, Announcement, Post, Organization_Region, Organization_Cause_Alignment, User_Event_Attendance
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User as auth_user


class RegionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Region
		fields = ('region_id', 'name')

class RoleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Role
		fields = ('role_id', 'name')

class CauseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cause
		fields = ('cause_id', 'name')

class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
	cause_id = serializers.SlugRelatedField(
	many=True,
	read_only=True,
	slug_field='name'
	)
	region_id = serializers.SlugRelatedField(
	many=True,
	read_only=True,
	slug_field='name'
	)
    # cause = serializers.SlugRelatedField(read_only=True, slug_field='name', many=True)
    # region = serializers.SlugRelatedField(read_only=True, slug_field='name', many=True)
	class Meta:
		model = Organization
		fields = ('org_id', 'ein', 'name', 'address1', 'address2', 'city', 'state', 'zip', 'country', 'phone', 'mission', 'website', 'facebook', 'twitter', 'founded', 'cause_id', 'region_id')

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = auth_user
        fields = ('username', 'first_name', 'last_name', 'email')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	user = AuthUserSerializer(required=True)
	organization_id = OrganizationSerializer(read_only=True)
	
	class Meta:
		model = User
		#fields = ('user_id', 'username', 'password', 'first_name', 'last_name', 'phone', 'email', 'registration_date', 'preferred_pronouns', 'role_id', 'organization_id')
		fields = ('user_id', 'user', 'registration_date', 'role_id', 'organization_id')

'''
class UserSerializer(serializers.HyperlinkedModelSerializer):
	#email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
	#username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])
	#password = serializers.CharField(min_length=8)

	# org = OrganizationSerializer(read_only=True)

	organization_id = OrganizationSerializer(read_only=True)

	class Meta:
		model = User
		fields = ('username', 'password', 'first_name', 'last_name', 'phone', 'email', 'registration_date', 'preferred_pronouns', 'role_id', 'organization_id')
'''
class EventSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Event
		fields = ('name', 'date', 'description', 'organization_id', 'user_id')

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Channel
		fields = ('channel_id', 'name', 'description')

class AnnouncementSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Announcement
		fields = ('announcement_id', 'title', 'text', 'date', 'user_id', 'event_id')

class PostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = ('post_id', 'title', 'text', 'channel_id', 'user_id')

class OrganizationRegionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Organization_Region
		fields = ('id', 'organization_id', 'region_id')

class OrganizationCauseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Organization_Cause_Alignment
		fields = ('id', 'organization_id', 'cause_id')

class UserEventSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User_Event_Attendance
		fields = ('id', 'user_id', 'event_id')
