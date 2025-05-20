from rest_framework import serializers

from superadmin_app.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','description','assigned_to','due_date','status','completion_report','worked_hours',]