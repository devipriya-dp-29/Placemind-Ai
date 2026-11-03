from rest_framework import serializers
from .models import Company, PlacementDrive, Application, MockTest, MockTestResult
from users.serializers import UserSerializer

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class PlacementDriveSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company', write_only=True, required=False
    )
    company_name = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = PlacementDrive
        fields = '__all__'

    def create(self, validated_data):
        company_name = validated_data.pop('company_name', None)
        if company_name:
            company, created = Company.objects.get_or_create(name=company_name)
            validated_data['company'] = company
        return super().create(validated_data)

class ApplicationSerializer(serializers.ModelSerializer):
    student = UserSerializer(read_only=True)
    drive = PlacementDriveSerializer(read_only=True)
    drive_id = serializers.PrimaryKeyRelatedField(
        queryset=PlacementDrive.objects.all(), source='drive', write_only=True
    )

    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ('student', 'status')

class MockTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MockTest
        fields = ['id', 'title', 'description', 'duration_minutes', 'total_marks', 'questions', 'created_at']

class MockTestResultSerializer(serializers.ModelSerializer):
    test_title = serializers.CharField(source='test.title', read_only=True)
    
    class Meta:
        model = MockTestResult
        fields = '__all__'
        read_only_fields = ('student', 'taken_at')
