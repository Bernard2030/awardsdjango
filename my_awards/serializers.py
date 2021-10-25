from django.db.models import fields
from rest_framework import serializers
from .models import Profile, My_projects


class ProfileSerializer(serializers.ModelSwrializer):
    class Meta:
        model = Profile
        fields('user', 'bio', 'info')


class My_projectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = My_projects
        fields = ('title', 'description', 'links', 'user')        