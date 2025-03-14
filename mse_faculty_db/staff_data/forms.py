from django import forms
from .models import (EmploymentHistory, OtherEmployment, UCICourse, DoctoralStudent, MasterStudent, PostdocStudent, UndergradResearch, OtherResearch,
                     TeachingAward, TeachingInnovation, ProfDevelopmentTeaching, DiversityTeaching, IntellectualContributions, NotCreditedArtistic, PreviousContributions, CreditedArtistic, CompletedPartsOfWorks, ProfessionalResources,
                     IntellectualProperty, ContractsGrantsFellowships, NonFinancialResources,
                     ProfDevResearchActivities, DiversityResearchActivities, HonorsAward, Membership, ProfessionalActivity,
                     ProfPublicService, ProfDevService, DiversityService, UniversitySystemwide, Campus, School, Department, ProfessionalDevelopement, DiversityAcitivites)


class EmploymentHistoryForm(forms.ModelForm):
    class Meta:
        model = EmploymentHistory
        fields = ['faculty_id', 'period_start', 'period_end',
                  'title_rank', 'step', 'time_percentage', 'department']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'title_rank': forms.TextInput(attrs={'class': 'form-control'}),
            'step': forms.TextInput(attrs={'class': 'form-control'}),
            'time_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OtherEmploymentForm(forms.ModelForm):
    class Meta:
        model = OtherEmployment
        fields = ['faculty_id', 'period_start',
                  'period_end', 'position_description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'position_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class UCICourseForm(forms.ModelForm):
    class Meta:
        model = UCICourse
        fields = ['faculty_id', 'period_start', 'period_end', 'courseNumber', 'courseTitle',
                  'enrollment', 'numInstructors', 'percentTaught', 'coreCourse']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'courseNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'courseTitle': forms.TextInput(attrs={'class': 'form-control'}),
            'enrollment': forms.NumberInput(attrs={'class': 'form-control'}),
            'numInstructors': forms.NumberInput(attrs={'class': 'form-control'}),
            'percentTaught': forms.NumberInput(attrs={'class': 'form-control'}),
            'coreCourse': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class DoctoralStudentForm(forms.ModelForm):
    class Meta:
        model = DoctoralStudent
        fields = ['faculty_id', 'internalID', 'period_start', 'period_end', 'endpresent',
                  'studentName', 'role', 'department', 'comments', 'receivedPHD',
                  'candidacy', 'preDissComm', 'otherResearch']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'endpresent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'studentName': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'receivedPHD': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'candidacy': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'preDissComm': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'otherResearch': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class MasterStudentForm(forms.ModelForm):
    class Meta:
        model = MasterStudent
        fields = ['faculty_id', 'internalID', 'period_start', 'period_end', 'endpresent',
                  'studentName', 'role', 'department', 'comments']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'endpresent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'studentName': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class PostdocStudentForm(forms.ModelForm):
    class Meta:
        model = PostdocStudent
        fields = ['faculty_id', 'internalID', 'period_start', 'period_end', 'endpresent',
                  'studentName', 'role', 'department', 'comments']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'endpresent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'studentName': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class UndergradResearchForm(forms.ModelForm):
    class Meta:
        model = UndergradResearch
        fields = ['faculty_id', 'internalID', 'period_start', 'period_end', 'endpresent',
                  'studentName', 'role', 'department', 'comments']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'endpresent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'studentName': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class OtherResearchForm(forms.ModelForm):
    class Meta:
        model = OtherResearch
        fields = ['faculty_id', 'internalID', 'period_start', 'period_end', 'endpresent',
                  'studentName', 'role', 'department', 'comments']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'endpresent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'studentName': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class TeachingAwardForm(forms.ModelForm):
    class Meta:
        model = TeachingAward
        fields = ['faculty_id', 'internalID', 'period_start',
                  'period_end', 'description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class TeachingInnovationForm(forms.ModelForm):
    class Meta:
        model = TeachingInnovation
        fields = ['faculty_id', 'internalID', 'period_start',
                  'period_end', 'description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class ProfDevelopmentTeachingForm(forms.ModelForm):
    class Meta:
        model = ProfDevelopmentTeaching
        fields = ['faculty_id', 'internalID', 'period_start',
                  'period_end', 'description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class DiversityTeachingForm(forms.ModelForm):
    class Meta:
        model = DiversityTeaching
        fields = ['faculty_id', 'internalID', 'period_start',
                  'period_end', 'description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# Section 3


class IntellectualContributionsForm(forms.ModelForm):
    class Meta:
        model = IntellectualContributions
        fields = ['faculty_id', 'internalID', 'period_start', 'period_end',
                  'category', 'publication_citation']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'publication_citation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class NotCreditedArtisticForm(forms.ModelForm):
    class Meta:
        model = NotCreditedArtistic
        fields = ['faculty_id', 'internalID', 'period_start', 'period_end',
                  'category', 'creativeWork']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'creativeWork': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class PreviousContributionsForm(forms.ModelForm):
    class Meta:
        model = PreviousContributions
        fields = ['faculty_id', 'internalID', 'period_start', 'period_end',
                  'category', 'publication_citation']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'publication_citation': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class CreditedArtisticForm(forms.ModelForm):
    class Meta:
        model = CreditedArtistic
        fields = ['faculty_id', 'internalID', 'period_start', 'period_end',
                  'category', 'creativeWork']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'creativeWork': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class CompletedPartsOfWorksForm(forms.ModelForm):
    class Meta:
        model = CompletedPartsOfWorks
        fields = ['faculty_id', 'period_start', 'period_end',
                  'internalID', 'category', 'work_detail']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'work_detail': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class ProfessionalResourcesForm(forms.ModelForm):
    class Meta:
        model = ProfessionalResources
        fields = ['faculty_id', 'period_start',
                  'period_end', 'internalID', 'description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class IntellectualPropertyForm(forms.ModelForm):
    class Meta:
        model = IntellectualProperty
        fields = ['faculty_id', 'period_start',
                  'period_end', 'internalID', 'description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class ContractsGrantsFellowshipsForm(forms.ModelForm):
    class Meta:
        model = ContractsGrantsFellowships
        fields = ['faculty_id', 'internalID', 'period_start', 'period_end', 'previously_submitted',
                  'funding_source', 'number_or_title', 'role', 'amount']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'previously_submitted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'funding_source': forms.TextInput(attrs={'class': 'form-control'}),
            'number_or_title': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class NonFinancialResourcesForm(forms.ModelForm):
    class Meta:
        model = NonFinancialResources
        fields = ['faculty_id', 'internalID', 'period_start', 'period_end', 'previously_submitted', 'funding_source',
                  'number_or_title', 'role', 'perks_description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'previously_submitted': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'funding_source': forms.TextInput(attrs={'class': 'form-control'}),
            'number_or_title': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'perks_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class ProfDevResearchActivitiesForm(forms.ModelForm):
    class Meta:
        model = ProfDevResearchActivities
        fields = ['faculty_id', 'internalID',
                  'period_start', 'period_end', 'description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class DiversityResearchActivitiesForm(forms.ModelForm):
    class Meta:
        model = DiversityResearchActivities
        fields = ['faculty_id', 'period_start',
                  'period_end', 'internalID', 'description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class HonorsAwardForm(forms.ModelForm):
    class Meta:
        model = HonorsAward
        fields = ['faculty_id', 'internalID', 'period_start',
                  'period_end', 'description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['faculty_id', 'internalID', 'period_start',
                  'period_end', 'endpresent', 'description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'endpresent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class ProfessionalActivityForm(forms.ModelForm):
    class Meta:
        model = ProfessionalActivity
        fields = ['faculty_id', 'internalID', 'period_start', 'period_end', 'description',
                  'invitedEduGov', 'invitedProf', 'acceptedEduGov', 'acceptedProf', 'otherPresent',
                  'mediaInterview', 'articlesReviews']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            # Add widgets for the boolean fields as needed
        }


class ProfPublicServiceForm(forms.ModelForm):
    class Meta:
        model = ProfPublicService
        fields = ['faculty_id', 'internalID', 'period_start', 'period_end', 'description',
                  'profSocOutsideInst', 'journalEdit', 'reviewer', 'memberReviewBoard', 'adhocService',
                  'consulting', 'communityService']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'profSocOutsideInst': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'journalEdit': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'reviewer': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'memberReviewBoard': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'adhocService': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'consulting': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'communityService': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ProfDevServiceForm(forms.ModelForm):
    class Meta:
        model = ProfDevService
        fields = ['faculty_id', 'internalID', 'period_start',
                  'period_end', 'description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class DiversityServiceForm(forms.ModelForm):
    class Meta:
        model = DiversityService
        fields = ['faculty_id', 'internalID', 'period_start',
                  'period_end', 'description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class UniversitySystemwideForm(forms.ModelForm):
    class Meta:
        model = UniversitySystemwide
        fields = ['faculty_id', 'internalID', 'period_start',
                  'period_end', 'position_description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'position_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['faculty_id', 'internalID', 'period_start',
                  'period_end', 'position_description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'position_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['faculty_id', 'internalID', 'period_start',
                  'period_end', 'position_description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'position_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['faculty_id', 'internalID', 'period_start',
                  'period_end', 'position_description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'position_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class ProfessionalDevelopementForm(forms.ModelForm):
    class Meta:
        model = ProfessionalDevelopement
        fields = ['faculty_id', 'internalID', 'period_start',
                  'period_end', 'position_description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'position_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class DiversityAcitivitesForm(forms.ModelForm):
    class Meta:
        model = DiversityAcitivites
        fields = ['faculty_id', 'internalID', 'period_start',
                  'period_end', 'position_description']
        widgets = {
            'faculty_id': forms.Select(attrs={'class': 'form-control'}),
            'internalID': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'period_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'period_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'position_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
