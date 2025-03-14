from rest_framework import serializers
from .models import (FacultyId, EmploymentHistory, OtherEmployment, UCICourse, 
                     DoctoralStudent, MasterStudent, PostdocStudent, 
                     UndergradResearch, OtherResearch, TeachingAward, 
                     TeachingInnovation, ProfDevelopmentTeaching, 
                     DiversityTeaching, IntellectualContributions, 
                     PreviousContributions, CompletedPartsOfWorks, 
                     ProfessionalResources, IntellectualProperty, 
                     ContractsGrantsFellowships, NonFinancialResources, 
                     ProfDevResearchActivities, DiversityResearchActivities, 
                     HonorsAward, Membership, ProfessionalActivity, 
                     ProfPublicService, ProfDevService, DiversityService,
                     UniversitySystemwide, Campus, School, Department,
                     ProfessionalDevelopement, DiversityAcitivites)

class FacultyIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyId
        fields = ('uuid', 'name', 'email', 'faculty_department')

class EmploymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentHistory
        fields = '__all__'

class OtherEmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherEmployment
        fields = '__all__'

class UCICourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UCICourse
        fields = '__all__'

class DoctoralStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctoralStudent
        fields = '__all__'

class MasterStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterStudent
        fields = '__all__'

class PostdocStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostdocStudent
        fields = '__all__'

class UndergradResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = UndergradResearch
        fields = '__all__'

class OtherResearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherResearch
        fields = '__all__'

class TeachingAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingAward
        fields = '__all__'

class TeachingInnovationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachingInnovation
        fields = '__all__'

class ProfDevelopmentTeachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfDevelopmentTeaching
        fields = '__all__'

class DiversityTeachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiversityTeaching
        fields = '__all__'

class IntellectualContributionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntellectualContributions
        fields = '__all__'

class PreviousContributionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousContributions
        fields = '__all__'

class CompletedPartsOfWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedPartsOfWorks
        fields = '__all__'

class ProfessionalResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalResources
        fields = '__all__'

class IntellectualPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = IntellectualProperty
        fields = '__all__'

class ContractsGrantsFellowshipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractsGrantsFellowships
        fields = '__all__'

class NonFinancialResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonFinancialResources
        fields = '__all__'

class ProfDevResearchActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfDevResearchActivities
        fields = '__all__'

class DiversityResearchActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiversityResearchActivities
        fields = '__all__'

class HonorsAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = HonorsAward
        fields = '__all__'

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'

class ProfessionalActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalActivity
        fields = '__all__'

class ProfPublicServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfPublicService
        fields = '__all__'

class ProfDevServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfDevService
        fields = '__all__'

class DiversityServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiversityService
        fields = '__all__'

class UniversitySystemwideSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniversitySystemwide
        fields = '__all__'

class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ProfessionalDevelopementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalDevelopement
        fields = '__all__'

class DiversityAcitivitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiversityAcitivites
        fields = '__all__'
