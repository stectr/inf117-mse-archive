from django.contrib import admin
from .models import FacultyId
from .models import EmploymentHistory, OtherEmployment  # section 1
from .models import UCICourse, DoctoralStudent, MasterStudent, PostdocStudent, UndergradResearch, OtherResearch, TeachingAward, TeachingInnovation, ProfDevelopmentTeaching, DiversityTeaching  # Section 2
from .models import IntellectualContributions, NotCreditedArtistic, PreviousContributions, CreditedArtistic, CompletedPartsOfWorks, ProfessionalResources, IntellectualProperty, ContractsGrantsFellowships, NonFinancialResources, ProfDevResearchActivities, DiversityResearchActivities  # Section 3
from .models import HonorsAward, Membership, ProfessionalActivity, ProfPublicService, ProfDevService, DiversityService  # Section 4
from .models import UniversitySystemwide, Campus, School, Department, ProfessionalDevelopement, DiversityAcitivites  # section 5


@admin.register(FacultyId)
class FacultyIdsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'faculty_department')
    search_fields = ('name', 'email', 'faculty_department')

# Section 1


@admin.register(EmploymentHistory)
class EmploymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'employment_id', 'period_start', 'period_end',
                    'title_rank', 'time_percentage', 'department')
    search_fields = ('faculty_id__name', 'employment_id', 'period_start', 'period_end',
                     'title_rank', 'time_percentage', 'department')


@admin.register(OtherEmployment)
class OtherEmploymentAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'employment_id', 'period_start',
                    'period_end', 'position_description')
    search_fields = ('faculty_id__name', 'employment_id', 'period_start',
                     'period_end', 'position_description')


# Section 2
@admin.register(UCICourse)
class UCICoursesAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'period_start', 'period_end', 'courseNumber', 'courseTitle',
                    'enrollment', 'numInstructors', 'percentTaught', 'coreCourse')
    search_fields = ('faculty_id__name', 'period_start', 'period_end', 'courseNumber', 'courseTitle',
                     'enrollment', 'numInstructors', 'percentTaught', 'coreCourse')


@admin.register(DoctoralStudent)
class DoctoralStudentsAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'period_end', 'endpresent', 'studentName', 'role',
                    'department', 'comments', 'receivedPHD', 'candidacy', 'preDissComm', 'otherResearch')
    search_fields = ('faculty_id__name', 'period_start', 'period_end', 'endpresent', 'studentName', 'role',
                     'department', 'comments', 'receivedPHD', 'candidacy', 'preDissComm', 'otherResearch')


@admin.register(MasterStudent)
class MasterStudentsAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'period_end', 'endpresent',
                    'studentName', 'role', 'department', 'comments')
    search_fields = ('faculty_id__name', 'period_start', 'period_end', 'endpresent',
                     'studentName', 'role', 'department', 'comments')


@admin.register(PostdocStudent)
class PostdocStudentsAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'period_end', 'endpresent',
                    'studentName', 'role', 'department', 'comments')
    search_fields = ('faculty_id__name', 'period_start', 'period_end', 'endpresent',
                     'studentName', 'role', 'department', 'comments')


@admin.register(UndergradResearch)
class UndergradResearchAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'period_end', 'endpresent',
                    'studentName', 'role', 'department', 'comments')
    search_fields = ('faculty_id__name', 'period_start', 'period_end', 'endpresent',
                     'studentName', 'role', 'department', 'comments')


@admin.register(OtherResearch)
class OtherResearchAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'period_end', 'endpresent',
                    'studentName', 'role', 'department', 'comments')
    search_fields = ('faculty_id__name', 'period_start', 'period_end', 'endpresent',
                     'studentName', 'role', 'department', 'comments')


@admin.register(TeachingAward)
class TeachingAwardsAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'period_end',
                    'description')
    search_fields = ('faculty_id__name', 'period_start', 'period_end',
                     'description')


@admin.register(TeachingInnovation)
class TeachingInnovationsAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'period_end',
                    'description')
    search_fields = ('faculty_id__name', 'period_start', 'period_end',
                     'description')


@admin.register(ProfDevelopmentTeaching)
class ProfDevelopmentTeachingAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'period_end',
                    'description')
    search_fields = ('faculty_id__name', 'period_start', 'period_end',
                     'description')


@admin.register(DiversityTeaching)
class DiversityTeachingAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'period_end',
                    'description')
    search_fields = ('faculty_id__name', 'period_start', 'period_end',
                     'description')


# Section 3
@admin.register(IntellectualContributions)
class IntellectualContributionsAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'period_start', 'internalID',
                    'category', 'publication_citation')
    search_fields = ('faculty_id__name', 'period_start',
                     'category', 'publication_citation')


@admin.register(NotCreditedArtistic)
class NotCreditedArtisticAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'period_start',
                    'internalID', 'category', 'creativeWork')
    search_fields = ('faculty_id__name', 'period_start', 'category', 'creativeWork')


@admin.register(PreviousContributions)
class PreviousContributionsAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'period_start', 'internalID',
                    'category', 'publication_citation')
    search_fields = ('faculty_id__name', 'period_start',
                     'category', 'publication_citation')


@admin.register(CreditedArtistic)
class CreditedArtisticAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'period_start',
                    'internalID', 'category', 'creativeWork')
    search_fields = ('faculty_id__name', 'period_start', 'category', 'creativeWork')


@admin.register(CompletedPartsOfWorks)
class CompletedPartsOfWorksAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'period_start',
                    'internalID', 'category', 'work_detail')
    search_fields = ('faculty_id__name', 'period_start', 'category', 'work_detail')


@admin.register(ProfessionalResources)
class ProfessionalResourcesAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'period_start', 'internalID', 'description')
    search_fields = ('faculty_id__name', 'period_start', 'description')


@admin.register(IntellectualProperty)
class IntellectualPropertyAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'description')
    search_fields = ('faculty_id__name', 'period_start', 'description')


@admin.register(ContractsGrantsFellowships)
class ContractsGrantsFellowshipsAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'period_start', 'internalID', 'previously_submitted',
                    'funding_source', 'number_or_title', 'role', 'amount')
    search_fields = ('faculty_id__name', 'period_start', 'previously_submitted', 'funding_source',
                     'number_or_title', 'role', 'amount')


@admin.register(NonFinancialResources)
class NonFinancialResourcesAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'period_start', 'internalID', 'previously_submitted',
                    'funding_source', 'number_or_title', 'role', 'perks_description')
    search_fields = ('faculty_id__name', 'period_start', 'previously_submitted', 'funding_source',
                     'number_or_title', 'role', 'perks_description')


@admin.register(ProfDevResearchActivities)
class ProfDevResearchActivitiesAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'description')
    search_fields = ('faculty_id__name', 'period_start', 'description')


@admin.register(DiversityResearchActivities)
class DiversityResearchActivitiesAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'description')
    search_fields = ('faculty_id__name', 'period_start', 'description')

# Section 4


@admin.register(HonorsAward)
class HonorsAwardsAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'period_end',
                    'description')
    search_fields = ('faculty_id__name', 'period_start', 'period_end',
                     'description')


@admin.register(Membership)
class MembershipsAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'period_end',
                    'endpresent', 'description')
    search_fields = ('faculty_id__name', 'period_start', 'period_end', 'endpresent',
                     'description')


@admin.register(ProfessionalActivity)
class ProfessionalActivityAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'period_end', 'description', 'invitedEduGov',
                    'invitedProf', 'acceptedEduGov', 'acceptedProf', 'otherPresent', 'mediaInterview', 'articlesReviews')
    search_fields = ('faculty_id__name', 'period_start', 'period_end', 'description', 'invitedEduGov', 'invitedProf',
                     'acceptedEduGov', 'acceptedProf', 'otherPresent', 'mediaInterview', 'articlesReviews')


@admin.register(ProfPublicService)
class ProfPublicService(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'period_end', 'description', 'profSocOutsideInst',
                    'journalEdit', 'reviewer', 'memberReviewBoard', 'adhocService', 'consulting', 'communityService')
    search_fields = ('faculty_id__name', 'period_start', 'period_end', 'description', 'profSocOutsideInst',
                     'journalEdit', 'reviewer', 'memberReviewBoard', 'adhocService', 'consulting', 'communityService')


@admin.register(ProfDevService)
class ProfDevServiceAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'period_end',
                    'description')
    search_fields = ('faculty_id__name', 'period_start', 'period_end',
                     'description')


@admin.register(DiversityService)
class DiversityServiceAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start', 'period_end',
                    'description')
    search_fields = ('faculty_id__name', 'period_start', 'period_end',
                     'description')

# Section 5


@admin.register(UniversitySystemwide)
class UniversitySystemWideAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start',
                    'period_end', 'position_description')
    search_fields = ('faculty_id__name', 'internalID', 'period_start',
                     'period_end', 'position_description')


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start',
                    'period_end', 'position_description')
    search_fields = ('faculty_id__name', 'internalID', 'period_start',
                     'period_end', 'position_description')


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start',
                    'period_end', 'position_description')
    search_fields = ('faculty_id__name', 'internalID', 'period_start',
                     'period_end', 'position_description')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start',
                    'period_end', 'position_description')
    search_fields = ('faculty_id__name', 'internalID', 'period_start',
                     'period_end', 'position_description')


@admin.register(ProfessionalDevelopement)
class ProfessionalDevelopementAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start',
                    'period_end', 'position_description')
    search_fields = ('faculty_id__name', 'internalID', 'period_start',
                     'period_end', 'position_description')


@admin.register(DiversityAcitivites)
class DiversityActivitiesAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'internalID', 'period_start',
                    'period_end', 'position_description')
    search_fields = ('faculty_id__name', 'internalID', 'period_start',
                     'period_end', 'position_description')
