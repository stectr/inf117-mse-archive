from django.db import models
import uuid


class FacultyId(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    faculty_department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# ----- Section 1


class EmploymentHistory(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    employment_id = models.AutoField(primary_key=True)  # autofield for now

    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    title_rank = models.CharField(
        max_length=100, verbose_name="Title & Rank")  # Assistant Professor, etc
    # e.g. III OS / can be NULL
    step = models.CharField(null=True, blank=True, max_length=100)
    time_percentage = models.DecimalField(
        decimal_places=0, max_digits=3, verbose_name="Time")  # e.g. 50 for 50%
    # e.g. Materials Science & Engineering
    department = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Employment History"
        verbose_name_plural = "Employment Histories"


class OtherEmployment(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    employment_id = models.AutoField(primary_key=True)  # autofield for now

    period_start = models.DateField(verbose_name="Period Start", null=True)
    # but for now I'm using two values
    period_end = models.DateField(verbose_name="Period End", null=True)
    position_description = models.TextField(
        verbose_name="Position/Description")

    class Meta:
        verbose_name = "Other Employment"


# ----- Section 2: Teaching Activity During Review Period
class UCICourse(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)

    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    courseNumber = models.CharField(
        max_length=15, verbose_name="Course Number")
    courseTitle = models.CharField(max_length=30, verbose_name="Course Title")
    enrollment = models.IntegerField()
    numInstructors = models.IntegerField(verbose_name="Number of Instructors")
    percentTaught = models.IntegerField(verbose_name="Percent Taught")
    # Needs to be underlined if core course
    coreCourse = models.BooleanField(verbose_name="Core Course")

    class Meta:
        verbose_name = "UCI Course"


class DoctoralStudent(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    # If the end date is marked as "present"
    endpresent = models.BooleanField(verbose_name="Until Present?")
    '''If startyear == endyear then just have one variable? Or let PDF conversion figure it out.'''
    studentName = models.CharField(max_length=100, verbose_name="Student Name")
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    comments = models.TextField(blank=True)
    '''These flags below will determine which subsections each entry belongs to.'''
    receivedPHD = models.BooleanField(
        verbose_name="Has this student received their Ph.D or Pharm.D?")
    candidacy = models.BooleanField(
        verbose_name="Has this student advanced to candidacy?")
    preDissComm = models.BooleanField(
        verbose_name="Was this student in a pre-dissertation committee?")
    otherResearch = models.BooleanField(verbose_name="Other")

    class Meta:
        verbose_name = "Doctoral Student"
        # Add only one of endyear & endpresent constraint
        # Add only one of the last 4 constraint


class MasterStudent(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    # If the end date is marked as "present"
    endpresent = models.BooleanField(verbose_name="Until Present?")
    '''If startyear == endyear then just have one variable? Or let PDF conversion figure it out.'''
    studentName = models.CharField(max_length=100, verbose_name="Student Name")
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name = "Master's Student"
        # Add only one of endyear & endpresent constraint


class PostdocStudent(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    # If the end date is marked as "present"
    endpresent = models.BooleanField(verbose_name="Until Present?")
    '''If startyear == endyear then just have one variable? Or let PDF conversion figure it out.'''
    studentName = models.CharField(max_length=100, verbose_name="Student Name")
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name = "Postdoctoral Scholar"
        # Add only one of endyear & endpresent constraint


class UndergradResearch(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    # If the end date is marked as "present"
    endpresent = models.BooleanField(verbose_name="Until Present?")
    '''If startyear == endyear then just have one variable? Or let PDF conversion figure it out.'''
    studentName = models.CharField(max_length=100, verbose_name="Student Name")
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name = "Undergraduate Student Research Supervision"
        # Add only one of endyear & endpresent constraint


class OtherResearch(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    # If the end date is marked as "present"
    endpresent = models.BooleanField(verbose_name="Until Present?")
    '''If startyear == endyear then just have one variable? Or let PDF conversion figure it out.'''
    studentName = models.CharField(max_length=100, verbose_name="Student Name")
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    comments = models.TextField(blank=True)

    class Meta:
        verbose_name = "Other Research or Teaching Supervision"
        # Add only one of endyear & endpresent constraint


class TeachingAward(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    # If they want to input the date themselves, such as "Spring 2021"
    # dateinput = models.CharField(
    #     max_length=30, blank=True, verbose_name="Custom Date Input")
    description = models.TextField()

    class Meta:
        verbose_name = "Teaching Award"


class TeachingInnovation(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    # If they want to input the date themselves, such as "Spring 2021"
    # dateinput = models.CharField(
    #     max_length=30, blank=True, verbose_name="Custom Date Input")
    description = models.TextField()

    class Meta:
        verbose_name = "Teaching Innovation"


class ProfDevelopmentTeaching(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    # If they want to input the date themselves, such as "Spring 2021"
    # dateinput = models.CharField(
    #     max_length=30, blank=True, verbose_name="Custom Date Input")
    description = models.TextField()

    class Meta:
        verbose_name = "Professional Development Activity Related to Teaching"
        verbose_name_plural = "Professional Development Activities Related to Teaching"


class DiversityTeaching(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    # If they want to input the date themselves, such as "Spring 2021"
    # dateinput = models.CharField(
    #     max_length=30, blank=True, verbose_name="Custom Date Input")
    description = models.TextField()

    class Meta:
        verbose_name = "Diversity Activity Related to Teaching"
        verbose_name_plural = "Diversity Activities Related to Teaching"

# ----- Section 3: Research and Creative Activity During Review Period


class IntellectualContributions(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    publication_citation = models.TextField(verbose_name="Publication")
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)

    class Meta:
        verbose_name = "Intellectual Contribution (Not Credited in a Prior Review)"
        verbose_name = "Intellectual Contributions (Not Credited in a Prior Review)"


class NotCreditedArtistic(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    creativeWork = models.TextField(verbose_name="Creative Work")
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)

    class Meta:
        verbose_name = "Artistic and Professional Performance and Exhibit (Not Credited in a Prior Review)"
        verbose_name_plural = "Artistic and Professional Performances and Exhibits (Not Credited in a Prior Review)"


class PreviousContributions(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    # Fields are the same as IntellectualContributions
    category = models.CharField(max_length=100)
    publication_citation = models.TextField(verbose_name="Publication")
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)

    class Meta:
        verbose_name = "Intellectual Contribution (Previously Submitted in a Prior Review)"
        verbose_name = "Intellectual Contributions (Previously Submitted in a Prior Review)"


class CreditedArtistic(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    creativeWork = models.TextField(verbose_name="Creative Work")
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)

    class Meta:
        verbose_name = "Artistic and Professional Performance and Exhibit (Previously Submitted in a Prior Review)"
        verbose_name_plural = "Artistic and Professional Performances and Exhibits (Previously Submitted in a Prior Review)"


class CompletedPartsOfWorks(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    category = models.CharField(max_length=100)
    # Publication citation or creative work
    work_detail = models.TextField(verbose_name="Publication or Creative Work")
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)

    class Meta:
        verbose_name = "Completed Part of Larger Work"
        verbose_name_plural = "Completed Parts of Larger Works"


class ProfessionalResources(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    # Assuming multiple dates can be included
    # dates_active = models.CharField(
    #     max_length=100, verbose_name="Date(s) Active")
    description = models.TextField()
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)

    class Meta:
        verbose_name = "Professional Online & System Resource Produced/Maintained"
        verbose_name_plural = "Professional Online & System Resources Produced/Maintained"


class IntellectualProperty(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    description = models.TextField()
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)

    class Meta:
        verbose_name = "Intellectual Property - Patent, Copyright, Etc."
        verbose_name_plural = "Intellectual Property - Patents, Copyrights, Etc."


class ContractsGrantsFellowships(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    previously_submitted = models.BooleanField(
        verbose_name="Previously Submitted")
    funding_source = models.CharField(
        max_length=200, verbose_name="Funding Source")
    number_or_title = models.CharField(
        max_length=100, verbose_name="Number or Title")
    role = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # date_span = models.CharField(
    #     max_length=100, verbose_name="Date Span of Award")
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)

    class Meta:
        verbose_name = "Contract, Grant, Fellowship"
        verbose_name_plural = "Contracts, Grants, Fellowships"


class NonFinancialResources(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    # Similar to ContractsGrantsFellowships but with a description instead of an amount
    previously_submitted = models.BooleanField(
        verbose_name="Previously Submitted")
    funding_source = models.CharField(
        max_length=200, verbose_name="Funding Source")
    number_or_title = models.CharField(
        max_length=100, verbose_name="Number or Title")
    role = models.CharField(max_length=100)
    perks_description = models.TextField(verbose_name="Amount")
    # date_span = models.CharField(
    # max_length=100, verbose_name="Date Span of Award")
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)

    class Meta:
        verbose_name = "Allocation of Other Non-Financial Resource"


class ProfDevResearchActivities(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Professional Development Activity Related to Research/Creative Activity"
        verbose_name_plural = "Professional Development Activities Related to Research/Creative Activities"


class DiversityResearchActivities(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    description = models.TextField()

    class Meta:
        verbose_name = "Diversity Activity Related to Research/Creative Activity"
        verbose_name_plural = "Diversity Activities Related to Research/Creative Activities"

# ----- Section 4: Professional Recognition and Activity During Review Period


class HonorsAward(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    # If they want to input the date themselves, such as "Spring 2021"
    # dateinput = models.CharField(
    #     max_length=30, blank=True, verbose_name="Custom Date Input")
    description = models.TextField()

    class Meta:
        verbose_name = "Honors and Awards"
        verbose_name_plural = "Honors and Awards"


class Membership(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    # If the end date is marked as "present"
    endpresent = models.BooleanField(verbose_name="Until Present?")
    # If they want to input the date themselves, such as "Spring 2021"
    # dateinput = models.CharField(
    #     max_length=30, blank=True, verbose_name="Custom Date Input")
    description = models.TextField()

    class Meta:
        verbose_name = "Membership"


class ProfessionalActivity(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    # If they want to input the date themselves, such as "Spring 2021"
    # dateinput = models.CharField(
    #     max_length=30, blank=True, verbose_name="Custom Date Input")
    description = models.TextField()
    '''These flags below will determine which subsections each entry belongs to.'''
    invitedEduGov = models.BooleanField(
        verbose_name="Invited presentation at an educational, governmental (or similar) institution")
    invitedProf = models.BooleanField(
        verbose_name="Invited presentation at a professional meeting")
    acceptedEduGov = models.BooleanField(
        verbose_name="Accepted presentation at an educational, governmental (or similar) institution")
    acceptedProf = models.BooleanField(
        verbose_name="Accepted presentation at a professional meeting")
    otherPresent = models.BooleanField(
        verbose_name="Other presentation at a professional meeting")
    mediaInterview = models.BooleanField(
        verbose_name="Media Appearance and/or Interview")
    articlesReviews = models.BooleanField(
        verbose_name="Professional article about you or published review of your work")

    class Meta:
        verbose_name = "Professional Activity"
        verbose_name_plural = "Professional Activities"


class ProfPublicService(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    # If they want to input the date themselves, such as "Spring 2021"
    # dateinput = models.CharField(
    #     max_length=30, blank=True, verbose_name="Custom Date Input")
    description = models.TextField()
    '''These flags below will determine which subsections each entry belongs to.'''
    profSocOutsideInst = models.BooleanField(
        verbose_name="Service to Professional Societies / Outside Institutions")
    journalEdit = models.BooleanField(
        verbose_name="Journal Editor / Membership on Journal Editorial Boards")
    reviewer = models.BooleanField(
        verbose_name="Reviewer of Manuscripts / Journal Articles")
    memberReviewBoard = models.BooleanField(
        verbose_name="Standing Member of Review Boards for Funding Agencies")
    adhocService = models.BooleanField(
        verbose_name="Ad hoc Service as Referee of Proposals")
    consulting = models.BooleanField(verbose_name="Consulting Activities")
    communityService = models.BooleanField(verbose_name="Community Service")

    class Meta:
        verbose_name = "Professional and Public Service"


class ProfDevService(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    # If they want to input the date themselves, such as "Spring 2021"
    # dateinput = models.CharField(
    #     max_length=30, blank=True, verbose_name="Custom Date Input")
    description = models.TextField()

    class Meta:
        verbose_name = "Professional Development Activity Related to Professional and Public Service"
        verbose_name_plural = "Professional Development Activities Related to Professional and Public Service"


class DiversityService(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)
    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    # If they want to input the date themselves, such as "Spring 2021"
    # dateinput = models.CharField(
    #     max_length=30, blank=True, verbose_name="Custom Date Input")
    description = models.TextField()

    class Meta:
        verbose_name = "Diversity Activity Related to Professional and Public Service"
        verbose_name_plural = "Diversity Activities Related to Professional and Public Service"

# ----- Section 5


class UniversitySystemwide(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)  # autofield for now

    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    position_description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = "University/Systemwide Service"


class Campus(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)  # autofield for now

    period_start = models.DateField(verbose_name="Period Start", null=True)
    period_end = models.DateField(verbose_name="Period End", null=True)
    position_description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = "Campus Service"


class School(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)  # autofield for now

    period_start = models.DateField(verbose_name="Period Start", null=True)
    # but for now I'm using two values
    period_end = models.DateField(verbose_name="Period End", null=True)
    position_description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = "School Service"


class Department(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)  # autofield for now

    period_start = models.DateField(verbose_name="Period Start", null=True)
    # but for now I'm using two values
    period_end = models.DateField(verbose_name="Period End", null=True)
    position_description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = "Department Service"


class ProfessionalDevelopement(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)  # autofield for now

    period_start = models.DateField(verbose_name="Period Start", null=True)
    # but for now I'm using two values
    period_end = models.DateField(verbose_name="Period End", null=True)
    position_description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = "Professional Development Activity Related to University/Systemwide Service"
        verbose_name_plural = "Professional Development Activities Related to University/Systemwide Service"


class DiversityAcitivites(models.Model):
    faculty_id = models.ForeignKey(
        FacultyId, on_delete=models.CASCADE, null=True)
    internalID = models.AutoField(primary_key=True)  # autofield for now

    period_start = models.DateField(verbose_name="Period Start", null=True)
    # but for now I'm using two values
    period_end = models.DateField(verbose_name="Period End", null=True)
    position_description = models.TextField(verbose_name="Description")

    class Meta:
        verbose_name = "Diversity Activity Related to University/Systemwide Service"
        verbose_name_plural = "Diversity Activities Related to University/Systemwide Service"
