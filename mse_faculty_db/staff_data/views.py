from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
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

from .serializers import (FacultyIdSerializer, EmploymentHistorySerializer, 
                          OtherEmploymentSerializer, UCICourseSerializer, 
                          DoctoralStudentSerializer, MasterStudentSerializer, 
                          PostdocStudentSerializer, UndergradResearchSerializer, 
                          OtherResearchSerializer, TeachingAwardSerializer, 
                          TeachingInnovationSerializer, ProfDevelopmentTeachingSerializer, 
                          DiversityTeachingSerializer, IntellectualContributionsSerializer, 
                          PreviousContributionsSerializer, CompletedPartsOfWorksSerializer, 
                          ProfessionalResourcesSerializer, IntellectualPropertySerializer, 
                          ContractsGrantsFellowshipsSerializer, NonFinancialResourcesSerializer, 
                          ProfDevResearchActivitiesSerializer, DiversityResearchActivitiesSerializer, 
                          HonorsAwardSerializer, MembershipSerializer, ProfessionalActivitySerializer, 
                          ProfPublicServiceSerializer, ProfDevServiceSerializer, 
                          DiversityServiceSerializer, UniversitySystemwideSerializer, 
                          CampusSerializer, SchoolSerializer, DepartmentSerializer,)

from .forms import (
    EmploymentHistoryForm, OtherEmploymentForm, UCICourseForm,
    DoctoralStudentForm, MasterStudentForm, PostdocStudentForm,
    UndergradResearchForm, OtherResearchForm, TeachingAwardForm,
    TeachingInnovationForm, ProfDevelopmentTeachingForm, DiversityTeachingForm,
    IntellectualContributionsForm, NotCreditedArtisticForm, PreviousContributionsForm,
    CreditedArtisticForm, CompletedPartsOfWorksForm, ProfessionalResourcesForm,
    IntellectualPropertyForm, ContractsGrantsFellowshipsForm, NonFinancialResourcesForm,
    ProfDevResearchActivitiesForm, DiversityResearchActivitiesForm, HonorsAwardForm,
    MembershipForm, ProfessionalActivityForm, ProfPublicServiceForm,
    ProfDevServiceForm, DiversityServiceForm, UniversitySystemwideForm,
    CampusForm, SchoolForm, DepartmentForm, ProfessionalDevelopementForm,
    DiversityAcitivitesForm)

import subprocess
from django.http import JsonResponse, HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
import tempfile
from django.conf import settings
import os
import json
import pathlib




class FacultyIdView(APIView):
    def get(self, request):
        teaching_staff = FacultyId.objects.all()
        serializer = FacultyIdSerializer(teaching_staff, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FacultyIdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class EmploymentHistoryView(APIView):
    def get(self, request):
        histories = EmploymentHistory.objects.all()
        serializer = EmploymentHistorySerializer(histories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmploymentHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class OtherEmploymentView(APIView):
    def get(self, request):
        employments = OtherEmployment.objects.all()
        serializer = OtherEmploymentSerializer(employments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OtherEmploymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UCICourseView(APIView):
    def get(self, request):
        courses = UCICourse.objects.all()
        serializer = UCICourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UCICourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class DoctoralStudentView(APIView):
    def get(self, request):
        students = DoctoralStudent.objects.all()
        serializer = DoctoralStudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoctoralStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class MasterStudentView(APIView):
    def get(self, request):
        students = MasterStudent.objects.all()
        serializer = MasterStudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MasterStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PostdocStudentView(APIView):
    def get(self, request):
        scholars = PostdocStudent.objects.all()
        serializer = PostdocStudentSerializer(scholars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostdocStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# UndergradResearchView
class UndergradResearchView(APIView):
    def get(self, request):
        researches = UndergradResearch.objects.all()
        serializer = UndergradResearchSerializer(researches, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UndergradResearchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# OtherResearchView
class OtherResearchView(APIView):
    def get(self, request):
        researches = OtherResearch.objects.all()
        serializer = OtherResearchSerializer(researches, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OtherResearchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# TeachingAwardView
class TeachingAwardView(APIView):
    def get(self, request):
        awards = TeachingAward.objects.all()
        serializer = TeachingAwardSerializer(awards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeachingAwardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# TeachingInnovationView
class TeachingInnovationView(APIView):
    def get(self, request):
        innovations = TeachingInnovation.objects.all()
        serializer = TeachingInnovationSerializer(innovations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeachingInnovationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# ProfDevelopmentTeachingView
class ProfDevelopmentTeachingView(APIView):
    def get(self, request):
        activities = ProfDevelopmentTeaching.objects.all()
        serializer = ProfDevelopmentTeachingSerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfDevelopmentTeachingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# DiversityTeachingView
class DiversityTeachingView(APIView):
    def get(self, request):
        activities = DiversityTeaching.objects.all()
        serializer = DiversityTeachingSerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiversityTeachingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# IntellectualContributionsView
class IntellectualContributionsView(APIView):
    def get(self, request):
        contributions = IntellectualContributions.objects.all()
        serializer = IntellectualContributionsSerializer(contributions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IntellectualContributionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# PreviousContributionsView
class PreviousContributionsView(APIView):
    def get(self, request):
        contributions = PreviousContributions.objects.all()
        serializer = PreviousContributionsSerializer(contributions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PreviousContributionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# CompletedPartsOfWorksView
class CompletedPartsOfWorksView(APIView):
    def get(self, request):
        works = CompletedPartsOfWorks.objects.all()
        serializer = CompletedPartsOfWorksSerializer(works, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompletedPartsOfWorksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# ProfessionalResourcesView
class ProfessionalResourcesView(APIView):
    def get(self, request):
        resources = ProfessionalResources.objects.all()
        serializer = ProfessionalResourcesSerializer(resources, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfessionalResourcesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# IntellectualPropertyView
class IntellectualPropertyView(APIView):
    def get(self, request):
        properties = IntellectualProperty.objects.all()
        serializer = IntellectualPropertySerializer(properties, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = IntellectualPropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# ContractsGrantsFellowshipsView
class ContractsGrantsFellowshipsView(APIView):
    def get(self, request):
        contracts = ContractsGrantsFellowships.objects.all()
        serializer = ContractsGrantsFellowshipsSerializer(contracts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContractsGrantsFellowshipsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# NonFinancialResourcesView
class NonFinancialResourcesView(APIView):
    def get(self, request):
        resources = NonFinancialResources.objects.all()
        serializer = NonFinancialResourcesSerializer(resources, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NonFinancialResourcesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# ProfDevResearchActivitiesView
class ProfDevResearchActivitiesView(APIView):
    def get(self, request):
        activities = ProfDevResearchActivities.objects.all()
        serializer = ProfDevResearchActivitiesSerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfDevResearchActivitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# DiversityResearchActivitiesView
class DiversityResearchActivitiesView(APIView):
    def get(self, request):
        activities = DiversityResearchActivities.objects.all()
        serializer = DiversityResearchActivitiesSerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiversityResearchActivitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# HonorsAwardView
class HonorsAwardView(APIView):
    def get(self, request):
        awards = HonorsAward.objects.all()
        serializer = HonorsAwardSerializer(awards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HonorsAwardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# MembershipView
class MembershipView(APIView):
    def get(self, request):
        memberships = Membership.objects.all()
        serializer = MembershipSerializer(memberships, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# ProfessionalActivityView
class ProfessionalActivityView(APIView):
    def get(self, request):
        activities = ProfessionalActivity.objects.all()
        serializer = ProfessionalActivitySerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfessionalActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# ProfPublicServiceView
class ProfPublicServiceView(APIView):
    def get(self, request):
        services = ProfPublicService.objects.all()
        serializer = ProfPublicServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfPublicServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# ProfDevServiceView
class ProfDevServiceView(APIView):
    def get(self, request):
        services = ProfDevService.objects.all()
        serializer = ProfDevServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfDevServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class DiversityServiceView(APIView):
    def get(self, request):
        services = DiversityService.objects.all()
        serializer = DiversityServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiversityServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UniversitySystemwideView(APIView):
    def get(self, request):
        entries = UniversitySystemwide.objects.all()
        serializer = UniversitySystemwideSerializer(entries, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UniversitySystemwideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CampusView(APIView):
    def get(self, request):
        campuses = Campus.objects.all()
        serializer = CampusSerializer(campuses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CampusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class SchoolView(APIView):
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class DepartmentView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ProfessionalDevelopementView(APIView):
    def get(self, request):
        developments = ProfessionalDevelopement.objects.all()
        serializer = ProfessionalDevelopementSerializer(developments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfessionalDevelopementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class DiversityAcitivitesView(APIView):
    def get(self, request):
        activities = DiversityAcitivites.objects.all()
        serializer = DiversityAcitivitesSerializer(activities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiversityAcitivitesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Regular Django Views
def home(request):
    return render(request, 'home.html')

def accounts_page(request):
    faculty_ids = FacultyId.objects.all()
    return render(request, 'accounts_page.html', {'faculty_ids': faculty_ids})

def get_faculty_entries(request, faculty_id):
    faculty = get_object_or_404(FacultyId, uuid=faculty_id)
    employment_entries = EmploymentHistory.objects.filter(faculty_id=faculty)
    other_employment_entries = OtherEmployment.objects.filter(faculty_id=faculty)
    uci_course_entries = UCICourse.objects.filter(faculty_id=faculty)
    doctoral_students = DoctoralStudent.objects.filter(faculty_id=faculty)
    master_students = MasterStudent.objects.filter(faculty_id=faculty)
    postdoc_students = PostdocStudent.objects.filter(faculty_id=faculty)
    undergrad_research_entries = UndergradResearch.objects.filter(faculty_id=faculty)
    other_research_entries = OtherResearch.objects.filter(faculty_id=faculty)
    teaching_award_entries = TeachingAward.objects.filter(faculty_id=faculty)
    teaching_innovation_entries = TeachingInnovation.objects.filter(faculty_id=faculty)
    prof_development_teaching_entries = ProfDevelopmentTeaching.objects.filter(faculty_id=faculty)
    diversity_teaching_entries = DiversityTeaching.objects.filter(faculty_id=faculty)
    intellectual_contributions_entries = IntellectualContributions.objects.filter(faculty_id=faculty)
    previous_contributions_entries = PreviousContributions.objects.filter(faculty_id=faculty)
    completed_parts_of_works_entries = CompletedPartsOfWorks.objects.filter(faculty_id=faculty)
    professional_resources_entries = ProfessionalResources.objects.filter(faculty_id=faculty)
    intellectual_property_entries = IntellectualProperty.objects.filter(faculty_id=faculty)
    contracts_grants_fellowships_entries = ContractsGrantsFellowships.objects.filter(faculty_id=faculty)
    non_financial_resources_entries = NonFinancialResources.objects.filter(faculty_id=faculty)
    prof_dev_research_activities_entries = ProfDevResearchActivities.objects.filter(faculty_id=faculty)
    diversity_research_activities_entries = DiversityResearchActivities.objects.filter(faculty_id=faculty)
    honors_award_entries = HonorsAward.objects.filter(faculty_id=faculty)
    membership_entries = Membership.objects.filter(faculty_id=faculty)
    professional_activity_entries = ProfessionalActivity.objects.filter(faculty_id=faculty)
    prof_public_service_entries = ProfPublicService.objects.filter(faculty_id=faculty)
    prof_dev_service_entries = ProfDevService.objects.filter(faculty_id=faculty)
    diversity_service_entries = DiversityService.objects.filter(faculty_id=faculty)
    university_systemwide_entries = UniversitySystemwide.objects.filter(faculty_id=faculty)
    campus_entries = Campus.objects.filter(faculty_id=faculty)
    school_entries = School.objects.filter(faculty_id=faculty)
    department_entries = Department.objects.filter(faculty_id=faculty)
    professional_developement_entries = ProfessionalDevelopement.objects.filter(faculty_id=faculty)
    diversity_activities_entries = DiversityAcitivites.objects.filter(faculty_id=faculty)

    return render(request, 'faculty_entries.html', {
        'faculty': faculty,
        'employment_entries': employment_entries,
        'other_employment_entries': other_employment_entries,
        'uci_course_entries': uci_course_entries,
        'doctoral_students': doctoral_students,
        'master_students': master_students,
        'postdoc_students': postdoc_students,
        'undergrad_research_entries': undergrad_research_entries,
        'other_research_entries': other_research_entries,
        'teaching_award_entries': teaching_award_entries,
        'teaching_innovation_entries': teaching_innovation_entries,
        'prof_development_teaching_entries': prof_development_teaching_entries,
        'diversity_teaching_entries': diversity_teaching_entries,
        'intellectual_contributions_entries': intellectual_contributions_entries,
        'previous_contributions_entries': previous_contributions_entries,
        'completed_parts_of_works_entries': completed_parts_of_works_entries,
        'professional_resources_entries': professional_resources_entries,
        'intellectual_property_entries': intellectual_property_entries,
        'contracts_grants_fellowships_entries': contracts_grants_fellowships_entries,
        'non_financial_resources_entries': non_financial_resources_entries,
        'prof_dev_research_activities_entries': prof_dev_research_activities_entries,
        'diversity_research_activities_entries': diversity_research_activities_entries,
        'honors_award_entries': honors_award_entries,
        'membership_entries': membership_entries,
        'professional_activity_entries': professional_activity_entries,
        'prof_public_service_entries': prof_public_service_entries,
        'prof_dev_service_entries': prof_dev_service_entries,
        'diversity_service_entries': diversity_service_entries,
        'university_systemwide_entries': university_systemwide_entries,
        'campus_entries': campus_entries,
        'school_entries': school_entries,
        'department_entries': department_entries,
        'professional_developement_entries': professional_developement_entries,
        'diversity_activities_entries': diversity_activities_entries,
    })

# def input_view(request):
#     print("Request Method:", request.method)
#     print("Request POST Data:", request.POST)
    
#     employment_history_form = EmploymentHistoryForm()
#     other_employment_form = OtherEmploymentForm()
    
#     if request.method == 'POST':
#         # Check if the submit button of a specific form is present in the POST data
#         # print("I MADE IT MOM")
#         if 'employment_history_form' in request.POST:
#             print("Please god")
#             employment_history_form = EmploymentHistoryForm(request.POST)
#             if employment_history_form.is_valid():
#                 print("IT SAVED")
#                 employment_history_form.save()
#                 return redirect('accounts_page.html')  
        
#         elif 'other_employment_form' in request.POST:
#             other_employment_form = OtherEmploymentForm(request.POST)
#             if other_employment_form.is_valid():
#                 other_employment_form.save()
#                 return redirect('accounts_page.html')  

#     return render(request, 'input.html', {
#         'employment_history_form': employment_history_form,
#         'other_employment_form': other_employment_form,
#     })

def input_view(request):
    # Instantiate all forms
    employment_history_form = EmploymentHistoryForm()
    other_employment_form = OtherEmploymentForm()
    uci_course_form = UCICourseForm()
    doctoral_student_form = DoctoralStudentForm()
    master_student_form = MasterStudentForm()
    postdoc_student_form = PostdocStudentForm()
    undergrad_research_form = UndergradResearchForm()
    other_research_form = OtherResearchForm()
    teaching_award_form = TeachingAwardForm()
    teaching_innovation_form = TeachingInnovationForm()
    prof_development_teaching_form = ProfDevelopmentTeachingForm()
    diversity_teaching_form = DiversityTeachingForm()
    intellectual_contributions_form = IntellectualContributionsForm()
    not_credited_artistic_form = NotCreditedArtisticForm()
    previous_contributions_form = PreviousContributionsForm()
    credited_artistic_form = CreditedArtisticForm()
    completed_parts_of_works_form = CompletedPartsOfWorksForm()
    professional_resources_form = ProfessionalResourcesForm()
    intellectual_property_form = IntellectualPropertyForm()
    contracts_grants_fellowships_form = ContractsGrantsFellowshipsForm()
    non_financial_resources_form = NonFinancialResourcesForm()
    prof_dev_research_activities_form = ProfDevResearchActivitiesForm()
    diversity_research_activities_form = DiversityResearchActivitiesForm()
    honors_award_form = HonorsAwardForm()
    membership_form = MembershipForm()
    professional_activity_form = ProfessionalActivityForm()
    prof_public_service_form = ProfPublicServiceForm()
    prof_dev_service_form = ProfDevServiceForm()
    diversity_service_form = DiversityServiceForm()
    university_systemwide_form = UniversitySystemwideForm()
    campus_form = CampusForm()
    school_form = SchoolForm()
    department_form = DepartmentForm()
    professional_development_form = ProfessionalDevelopementForm()
    diversity_activities_form = DiversityAcitivitesForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'employment_history_form':
            employment_history_form = EmploymentHistoryForm(request.POST)
            if employment_history_form.is_valid():
                employment_history_form.save()
                return redirect('accounts_page')

        elif form_type == 'other_employment_form':
            other_employment_form = OtherEmploymentForm(request.POST)
            if other_employment_form.is_valid():
                other_employment_form.save()
                return redirect('accounts_page')

        elif form_type == 'uci_course_form':
            try:
                # Try to get the existing course
                existing_course = UCICourse.objects.get(period_start=request.POST['period_start'], period_end=request.POST['period_end'])
                uci_course_form = UCICourseForm(request.POST, instance=existing_course)
            except UCICourse.DoesNotExist:
                # If it does not exist, create a new form
                uci_course_form = UCICourseForm(request.POST)

            if uci_course_form.is_valid():
                print("im here")
                uci_course_form.save()
                return redirect('accounts_page')
            else:
                print("UCI Course Form is not valid")
                print("Errors:", uci_course_form.errors.as_data())

        elif form_type == 'doctoral_student_form':
            doctoral_student_form = DoctoralStudentForm(request.POST)
            if doctoral_student_form.is_valid():
                doctoral_student_form.save()
                return redirect('accounts_page')

        elif form_type == 'master_student_form':
            master_student_form = MasterStudentForm(request.POST)
            if master_student_form.is_valid():
                master_student_form.save()
                return redirect('accounts_page')

         # Handle PostdocStudentForm
        elif form_type == 'postdoc_student_form':
            postdoc_student_form = PostdocStudentForm(request.POST)
            if postdoc_student_form.is_valid():
                postdoc_student_form.save()
                return redirect('accounts_page')

        # Handle UndergradResearchForm
        elif form_type == 'undergrad_research_form':
            undergrad_research_form = UndergradResearchForm(request.POST)
            if undergrad_research_form.is_valid():
                undergrad_research_form.save()
                return redirect('accounts_page')

        # Handle OtherResearchForm
        elif form_type == 'other_research_form':
            other_research_form = OtherResearchForm(request.POST)
            if other_research_form.is_valid():
                other_research_form.save()
                return redirect('accounts_page')

        # Handle TeachingAwardForm
        elif form_type == 'teaching_award_form':
            teaching_award_form = TeachingAwardForm(request.POST)
            if teaching_award_form.is_valid():
                teaching_award_form.save()
                return redirect('accounts_page')

        # Handle TeachingInnovationForm
        elif form_type == 'teaching_innovation_form':
            teaching_innovation_form = TeachingInnovationForm(request.POST)
            if teaching_innovation_form.is_valid():
                teaching_innovation_form.save()
                return redirect('accounts_page')

        # Handle ProfDevelopmentTeachingForm
        elif form_type == 'prof_development_teaching_form':
            prof_development_teaching_form = ProfDevelopmentTeachingForm(request.POST)
            if prof_development_teaching_form.is_valid():
                prof_development_teaching_form.save()
                return redirect('accounts_page')

        # Handle DiversityTeachingForm
        elif form_type == 'diversity_teaching_form':
            diversity_teaching_form = DiversityTeachingForm(request.POST)
            if diversity_teaching_form.is_valid():
                diversity_teaching_form.save()
                return redirect('accounts_page')

        elif form_type == 'intellectual_contributions_form':
            intellectual_contributions_form = IntellectualContributionsForm(request.POST)
            if intellectual_contributions_form.is_valid():
                intellectual_contributions_form.save()
                return redirect('accounts_page')

        elif form_type == 'not_credited_artistic_form':
            not_credited_artistic_form = NotCreditedArtisticForm(request.POST)
            if not_credited_artistic_form.is_valid():
                not_credited_artistic_form.save()
                return redirect('accounts_page')

        elif form_type == 'previous_contributions_form':
            previous_contributions_form = PreviousContributionsForm(request.POST)
            if previous_contributions_form.is_valid():
                previous_contributions_form.save()
                return redirect('accounts_page')

        elif form_type == 'credited_artistic_form':
            credited_artistic_form = CreditedArtisticForm(request.POST)
            if credited_artistic_form.is_valid():
                credited_artistic_form.save()
                return redirect('accounts_page')

        elif form_type == 'completed_parts_of_works_form':
            completed_parts_of_works_form = CompletedPartsOfWorksForm(request.POST)
            if completed_parts_of_works_form.is_valid():
                completed_parts_of_works_form.save()
                return redirect('accounts_page')

        elif form_type == 'professional_resources_form':
            professional_resources_form = ProfessionalResourcesForm(request.POST)
            if professional_resources_form.is_valid():
                professional_resources_form.save()
                return redirect('accounts_page')

        elif form_type == 'intellectual_property_form':
            intellectual_property_form = IntellectualPropertyForm(request.POST)
            if intellectual_property_form.is_valid():
                intellectual_property_form.save()
                return redirect('accounts_page')

        elif form_type == 'contracts_grants_fellowships_form':
            contracts_grants_fellowships_form = ContractsGrantsFellowshipsForm(request.POST)
            if contracts_grants_fellowships_form.is_valid():
                contracts_grants_fellowships_form.save()
                return redirect('accounts_page')

        elif form_type == 'non_financial_resources_form':
            non_financial_resources_form = NonFinancialResourcesForm(request.POST)
            if non_financial_resources_form.is_valid():
                non_financial_resources_form.save()
                return redirect('accounts_page')

        elif form_type == 'prof_dev_research_activities_form':
            prof_dev_research_activities_form = ProfDevResearchActivitiesForm(request.POST)
            if prof_dev_research_activities_form.is_valid():
                prof_dev_research_activities_form.save()
                return redirect('accounts_page')

        elif form_type == 'diversity_research_activities_form':
            diversity_research_activities_form = DiversityResearchActivitiesForm(request.POST)
            if diversity_research_activities_form.is_valid():
                diversity_research_activities_form.save()
                return redirect('accounts_page')

        elif form_type == 'honors_award_form':
            honors_award_form = HonorsAwardForm(request.POST)
            if honors_award_form.is_valid():
                honors_award_form.save()
                return redirect('accounts_page')

        elif form_type == 'membership_form':
            membership_form = MembershipForm(request.POST)
            if membership_form.is_valid():
                membership_form.save()
                return redirect('accounts_page')

        elif form_type == 'professional_activity_form':
            professional_activity_form = ProfessionalActivityForm(request.POST)
            if professional_activity_form.is_valid():
                professional_activity_form.save()
                return redirect('accounts_page')

        elif form_type == 'prof_public_service_form':
            prof_public_service_form = ProfPublicServiceForm(request.POST)
            if prof_public_service_form.is_valid():
                prof_public_service_form.save()
                return redirect('accounts_page')

        elif form_type == 'prof_dev_service_form':
            prof_dev_service_form = ProfDevServiceForm(request.POST)
            if prof_dev_service_form.is_valid():
                prof_dev_service_form.save()
                return redirect('accounts_page')

        elif form_type == 'diversity_service_form':
            diversity_service_form = DiversityServiceForm(request.POST)
            if diversity_service_form.is_valid():
                diversity_service_form.save()
                return redirect('accounts_page')

        elif form_type == 'university_systemwide_form':
            university_systemwide_form = UniversitySystemwideForm(request.POST)
            if university_systemwide_form.is_valid():
                university_systemwide_form.save()
                return redirect('accounts_page')
            else:
                # Handle the case when the form is not valid
                print(university_systemwide_form.errors)  # For debugging

        elif form_type == 'campus_form':
            campus_form = CampusForm(request.POST)
            if campus_form.is_valid():
                campus_form.save()
                return redirect('accounts_page')

        elif form_type == 'school_form':
            school_form = SchoolForm(request.POST)
            if school_form.is_valid():
                school_form.save()
                return redirect('accounts_page')

        elif form_type == 'department_form':

            department_form = DepartmentForm(request.POST)
            print(department_form)
            if department_form.is_valid():
                department_form.save()
                return redirect('accounts_page')

        elif form_type == 'professional_development_form':
            professional_development_form = ProfessionalDevelopementForm(request.POST)
            if professional_development_form.is_valid():
                professional_development_form.save()
                return redirect('accounts_page')

        elif form_type == 'diversity_activities_form':
            diversity_activities_form = DiversityAcitivitesForm(request.POST)
            if diversity_activities_form.is_valid():
                print("Like anyways")
                diversity_activities_form.save()
                return redirect('accounts_page')




    return render(request, 'input.html', {
        'employment_history_form': employment_history_form,
        'other_employment_form': other_employment_form,
        'uci_course_form': uci_course_form,
        'doctoral_student_form': doctoral_student_form,
        'master_student_form': master_student_form,
        'postdoc_student_form': postdoc_student_form,
        'undergrad_research_form': undergrad_research_form,
        'other_research_form': other_research_form,
        'teaching_award_form': teaching_award_form,
        'teaching_innovation_form': teaching_innovation_form,
        'prof_development_teaching_form': prof_development_teaching_form,
        'diversity_teaching_form': diversity_teaching_form,
        'intellectual_contributions_form': intellectual_contributions_form,
        'not_credited_artistic_form': not_credited_artistic_form,
        'intellectual_contributions_form': intellectual_contributions_form,
        'not_credited_artistic_form': not_credited_artistic_form,
        'previous_contributions_form': previous_contributions_form,
        'credited_artistic_form': credited_artistic_form,
        'completed_parts_of_works_form': completed_parts_of_works_form,
        'professional_resources_form': professional_resources_form,
        'intellectual_property_form': intellectual_property_form,
        'contracts_grants_fellowships_form': contracts_grants_fellowships_form,
        'non_financial_resources_form': non_financial_resources_form,
        'prof_dev_research_activities_form': prof_dev_research_activities_form,
        'diversity_research_activities_form': diversity_research_activities_form,
        'honors_award_form': honors_award_form,
        'membership_form': membership_form,
        'professional_activity_form': professional_activity_form,
        'prof_public_service_form': prof_public_service_form,
        'prof_dev_service_form': prof_dev_service_form,
        'diversity_service_form': diversity_service_form,
        'university_systemwide_form': university_systemwide_form,
        'campus_form': campus_form,
        'school_form': school_form,
        'department_form': department_form,
        'professional_development_form': professional_development_form,
        'diversity_activities_form': diversity_activities_form

    })

@csrf_exempt
def run_script(request):
    if request.method == 'POST':
        try:
            # Get JSON data from the request body
            json_data = json.loads(request.body.decode('utf-8'))

            if not json_data:
                raise ValueError('JSON data is missing')

            # Construct the path to the script
            #script_path = os.path.abspath(os.path.join(pathlib.Path.parents[2-1], 'testingparser.py'))
            script_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'testingparser.py'))


            # Add the JSON data as an argument to the subprocess command
            command = ['python', script_path, json.dumps(json_data)]
            process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()

            # Check if the script generated a PDF file
            pdf_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'output.pdf'))

            if os.path.exists(pdf_path):
                # Create a FileResponse with the PDF content
                #with open(pdf_path, 'rb') as pdf_file:
                response = FileResponse(open(pdf_path, 'rb'))
                return response
            else:
                return JsonResponse({'error': 'PDF file not found'})

        except Exception as e:
            return JsonResponse({'error': str(e)})

    return JsonResponse({'error': 'Invalid request method'})


