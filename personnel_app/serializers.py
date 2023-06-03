from rest_framework import serializers

from .models import Department, Personnel
from django.utils.timezone import now

class PersonnelSerializer(serializers.ModelSerializer):
    added_by = serializers.StringRelatedField()
    department = serializers.StringRelatedField()
    department_id = serializers.IntegerField()

    days_since_joined = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Personnel
        fields = "__all__"
        extra_kwargs = { "added_by" : {"read_only" : True}}
    
    def get_days_since_joined(self, obj):
        return (now() - obj.date_joined).days
    
    def get_full_name(self, obj):
        return obj.first_name + " " + obj.last_name
    
    def validate_salary(self, value):
        if not (50000 < value < 150000):
            raise serializers.ValidationError("Salary should be in range 50k and 150k")
        return value


class DepartmentSerializer(serializers.ModelSerializer):
    personnel_count = serializers.SerializerMethodField()
    class Meta:
        model = Department
        fields = "__all__"
    
    def get_personnel_count(self, obj):
        # count = Personnel.objects.filter(department = obj.id).count()
        # return count
        return Personnel.objects.filter(department = obj.id).count()

class DepartmentDetailSerializer(serializers.ModelSerializer):
    # staff = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    # staff = serializers.StringRelatedField(many = True, read_only = True)
    staff = PersonnelSerializer(many = True, read_only = True)
    class Meta:
        model = Department
        fields = "__all__"