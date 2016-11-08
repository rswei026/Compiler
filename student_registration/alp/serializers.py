
from rest_framework import serializers
from .models import Outreach
from student_registration.students.serializers import StudentSerializer


class OutreachSerializer(serializers.ModelSerializer):
    original_id = serializers.IntegerField(source='id', read_only=True)
    student_id = serializers.IntegerField(source='student.id', read_only=True)
    student_id_type_id = serializers.CharField(source='student.id_type_id', read_only=True)
    student_nationality_id = serializers.CharField(source='student.nationality_id', read_only=True)
    student_mother_nationality_id = serializers.CharField(source='student.mother_nationality_id', read_only=True)
    location = serializers.IntegerField(source='school.location_id', read_only=True)
    governorate_name = serializers.CharField(source='school.location.parent.name', read_only=True)
    school_number = serializers.CharField(source='school.number', read_only=True)
    student_age = serializers.CharField(source='student.calc_age')
    student_first_name = serializers.CharField(source='student.first_name')
    student_father_name = serializers.CharField(source='student.father_name')
    student_last_name = serializers.CharField(source='student.last_name')
    student_mother_fullname = serializers.CharField(source='student.mother_fullname')
    student_sex = serializers.CharField(source='student.sex')
    student_birthday_year = serializers.CharField(source='student.birthday_year')
    student_birthday_month = serializers.CharField(source='student.birthday_month')
    student_birthday_day = serializers.CharField(source='student.birthday_day')
    student_phone = serializers.CharField(source='student.phone')
    student_phone_prefix = serializers.CharField(source='student.phone_prefix')
    student_id_number = serializers.CharField(source='student.id_number')
    student_id_type = serializers.CharField(source='student.id_type')
    student_nationality = serializers.CharField(source='student.nationality')
    student_mother_nationality = serializers.CharField(source='student.mother_nationality')
    student_address = serializers.CharField(source='student.address')

    def create(self, validated_data):

        student_data = validated_data.pop('student', None)
        student_serializer = StudentSerializer(data=student_data)
        student_serializer.is_valid(raise_exception=True)
        student_serializer.instance = student_serializer.save()

        try:
            instance = Outreach.objects.create(**validated_data)
            instance.student = student_serializer.instance
            instance.save()

        except Exception as ex:
            raise serializers.ValidationError({'Outreach instance': ex.message})

        return instance

    def update(self, instance, validated_data):

        try:
            student_data = validated_data.pop('student', None)
            student_serializer = StudentSerializer(data=student_data)
            student_serializer.is_valid(raise_exception=True)
            student_serializer.instance = student_serializer.save()
            instance.student = student_serializer.instance

            instance.save()

        except Exception as ex:
            raise serializers.ValidationError({'Outreach instance': ex.message})

        return instance

    class Meta:
        model = Outreach
        fields = (
            'id',
            'original_id',
            'student_id',
            'student_first_name',
            'student_father_name',
            'student_last_name',
            'student_mother_fullname',
            'student_sex',
            'student_birthday_year',
            'student_birthday_month',
            'student_birthday_day',
            'student_age',
            'student_phone',
            'student_phone_prefix',
            'student_id_number',
            'student_id_type',
            'student_nationality',
            'student_mother_nationality',
            'student_id_type_id',
            'student_nationality_id',
            'student_mother_nationality_id',
            'student_address',
            'registered_in_unhcr',
            'participated_in_alp',
            'last_informal_edu_level',
            'last_informal_edu_year',
            'last_informal_edu_final_result',
            'student_address',
            'school',
            'section',
            'classroom',
            'last_education_level',
            'last_education_year',
            'owner',
            'exam_result_arabic',
            'exam_result_language',
            'exam_result_math',
            'exam_result_science',
            'registered_in_school',
            'level',
            'exam_school',
            'alp_round',
            'location',
            'governorate_name',
            'school_number',
        )


class OutreachExamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Outreach
        fields = (
            'exam_result_arabic',
            'exam_result_language',
            'exam_result_math',
            'exam_result_science',
            'level',
            'exam_corrector_arabic',
            'exam_corrector_language',
            'exam_corrector_math',
            'exam_corrector_science',
            'registered_in_level',
            'section',
            'assigned_to_level',
            'not_enrolled_in_this_school',
            'exam_not_exist_in_school',
        )
