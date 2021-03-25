from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views.generic.base import TemplateView

# For user testing...
from rest_framework.views import APIView

from .serializers import *
from .models import *

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from collaboratory_api.forms import CustomUserCreationForm
from tablib import Dataset
from .resources import OrganizationResource
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .serializers import *

class RegionViewSet(viewsets.ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all().order_by('region_id')

class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.all().order_by('role_id')

class CauseViewSet(viewsets.ModelViewSet):
    serializer_class = CauseSerializer
    queryset = Cause.objects.all().order_by('cause_id')

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('user_id')

class OrganizationViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationSerializer
    queryset=Organization.objects.all().order_by('name')

# specific view for search
class OrganizationSearchFilter(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$name']

class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('event_id')

class ChannelViewSet(viewsets.ModelViewSet):
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all().order_by('channel_id')

class AnnouncementViewSet(viewsets.ModelViewSet):
    serializer_class = AnnouncementSerializer
    queryset = Announcement.objects.all().order_by('announcement_id')

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('post_id')

class OrganizationRegionViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationRegionSerializer
    queryset = Organization_Region.objects.all().order_by('id')

class OrganizationCauseViewSet(viewsets.ModelViewSet):
    serializer_class = OrganizationCauseSerializer
    queryset = Organization_Cause_Alignment.objects.all().order_by('id')

class UserEventViewSet(viewsets.ModelViewSet):
    serializer_class = UserEventSerializer
    queryset = User_Event_Attendance.objects.all().order_by('id')

## Organization API Views: Former per React ##
# Now, we are rending only results from the search.

# @api_view(['GET', 'POST'])
# def organizations_list(request):
#     if request.method == 'GET':
#         data = Organization.objects.all()
#         serializer = OrganizationSerializer(data, context={'request': request}, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = OrganizationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT', 'DELETE'])
# def organizations_detail(request, pk):
#     try:
#         organization = Organization.objects.get(pk=pk)
#     except Organization.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = OrganizationSerializer(organization, data=request.data,context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         organization.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

## User API Views ##
@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        data = User.objects.all()
        serializer = UserSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def users_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def events_list(request):
    if request.method == 'GET':
        data = User.objects.all()
        serializer = UserSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def events_detail(request, pk):
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = EventSerializer(event, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Registration
#def dashboard(request):
#    return render(request, "users/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("react_app"))

#login
def landing(request):
    return render(request, "others/landing.html")


# @method_decorator(login_required, name='dispatch') #We will want this later for login
class MainView(TemplateView):
    # our hybrid template, shown above
    template_name = 'dashboard.html'
    def get_context_data(self, **kwargs):
        return {'context_variable': 'value'}


# Import View, Organization

def simple_upload(request):
    if request.method == 'POST':
        organization_resource = OrganizationResource()
        dataset = Dataset()
        new_orgs = request.FILES['myfile']

        imported_data = dataset.load(new_orgs.read())
        result = organization_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            organization_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'core/simple_upload.html')