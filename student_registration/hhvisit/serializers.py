
from rest_framework import serializers
from .models import  HouseholdVisit , SpecificReason , HouseholdVisitAttempt , ChildVisit , MainReason
from student_registration.registrations.serializers import RegisteringAdultSerializer ,StudentSerializer



class MainReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainReason


class SpecificReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecificReason



class VisitAttemptSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        try:
            instance = HouseholdVisitAttempt.objects.create(**validated_data)
            instance.save()

        except Exception as ex:
            raise serializers.ValidationError({'HouseholdVisitAttempt instance': ex.message})

        return instance

    class Meta:
        model = HouseholdVisitAttempt
        fields = (
            'household_found',
            'comment',
            'date',
        )

class ChildVisitSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(source='student.first_name')
    father_name = serializers.CharField(source='student.father_name')
    last_name = serializers.CharField(source='student.last_name')
    mother_fullname = serializers.CharField(source='student.mother_fullname')
    main_reason =  serializers.CharField(source='main_reason.name')
    specific_reason = serializers.CharField(source='specific_reason.name')

    def create(self, validated_data):

        student_data = validated_data.pop('student', None)
        student_serializer = StudentSerializer(data=student_data)
        student_serializer.is_valid(raise_exception=True)
        student_serializer.instance = student_serializer.save()

        mainreason_data = validated_data.pop('main_reason', None)
        mainreason_serializer = MainReasonSerializer(data=mainreason_data)
        mainreason_serializer.is_valid(raise_exception=True)
        mainreason_serializer.instance = MainReasonSerializer.save()

        specificreason_data = validated_data.pop('specific_reason', None)
        specificreason_serializer = SpecificReasonSerializer(data=specificreason_data)
        specificreason_serializer.is_valid(raise_exception=True)
        specificreason_serializer.instance = SpecificReasonSerializer.save()

        try:
            instance = ChildVisit.objects.create(**validated_data)
            instance.student = student_serializer.instance
            instance.main_reason = mainreason_serializer.instance
            instance.specific_reason = specificreason_serializer.instance
            instance.save()

        except Exception as ex:
            raise serializers.ValidationError({'ChildVisit instance': ex.message})

        return instance

    class Meta:
        model = ChildVisit
        fields = (
            'first_name',
            'father_name',
            'last_name',
            'mother_fullname',
            'service_provider',
            'main_reason',
            'specific_reason'
        )


class HouseholdVisitSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    registeringadult_id = serializers.IntegerField(source='registering_adult.id', read_only=True)
    first_name = serializers.CharField(source='registering_adult.first_name', read_only=True)
    father_name = serializers.CharField(source='registering_adult.father_name', read_only=True)
    last_name = serializers.CharField(source='registering_adult.last_name', read_only=True)
    address = serializers.CharField(source='registering_adult.address', read_only=True)
    primary_phone = serializers.CharField(source='registering_adult.primary_phone', read_only=True)
    secondary_phone = serializers.CharField(source='registering_adult.secondary_phone', read_only=True)
    visit_attempt = VisitAttemptSerializer(many=True, read_only=True)
    children_visits = ChildVisitSerializer(many=True, read_only=True)

    def create(self, validated_data):

        registeringadult_data = validated_data.pop('registering_adult', None)
        registeringadult_serializer = RegisteringAdultSerializer(data=registeringadult_data)
        registeringadult_serializer.is_valid(raise_exception=True)
        registeringadult_serializer.instance = RegisteringAdultSerializer.save()

        try:
            instance = HouseholdVisit.objects.create(**validated_data)
            instance.registering_adult = RegisteringAdultSerializer.instance
            instance.save()

        except Exception as ex:
            raise serializers.ValidationError({'HouseholdVisit instance': ex.message})

        return instance

    class Meta:
        model = HouseholdVisit
        fields = (
            'id',
            'visit_status',
            'registeringadult_id',
            'first_name',
            'father_name',
            'last_name',
            'address',
            'primary_phone',
            'secondary_phone',
            'visit_attempt',
            'children_visits'
        )
