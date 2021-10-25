from rest_framework import serializers
from .models import Profile,My_projects

class ProfileListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'info')



class My_projectsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = My_projects
        fields = ('user', 'title', 'description', 'links')        