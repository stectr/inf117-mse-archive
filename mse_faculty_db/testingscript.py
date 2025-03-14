# @format
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "mse_faculty_db.settings")
django.setup()
from staff_data.models import *


# Import your model after setting up Django

# Now you can use the model
alle = EmploymentHistory.objects.all()

print(alle)
for i in alle:
    print(i.employment_id)
    print(i.faculty_id)
# print(alle.employment_id)

# set "DJANGO_SETTINGS_MODULE=mse_faculty_db.settings"
