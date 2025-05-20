from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from superadmin_app.models import Task
from user_app.permissions import IsAdminOrSuperAdmin
from user_app.serializers import TaskSerializer
# Create your views here.
class SigninAPIView(APIView):
    def post(self,request): 
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                response ={
                    "access_token":str(refresh.access_token),
                    "refresh_token":str(refresh),
                }
                return Response(response,status=status.HTTP_200_OK)
            else:
                return Response({"message":"Incorrect inputs"},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":"An error occured"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class TaskListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            tasks = Task.objects.filter(assigned_to=request.user)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": "An error occurred while retrieving tasks.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def put(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, assigned_to=request.user)
        except Task.DoesNotExist:
            return Response(
                {"error": "Task not found or not assigned to you."},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            input_status = request.data.get('status', task.status)
            new_status = input_status.strip().title() if input_status else task.status

            valid_statuses = dict(Task.STATUS_CHOICES).keys()
            if new_status not in valid_statuses:
                return Response(
                    {"error": f"Invalid status. Allowed values: {', '.join(valid_statuses)}"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            completion_report = request.data.get('completion_report')
            worked_hours = request.data.get('worked_hours')

            if new_status == 'Completed':
                if not completion_report or worked_hours in [None, '']:
                    return Response(
                        {"error": "Completion report and worked hours are required when marking task as Completed."},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                task.completion_report = completion_report
                task.worked_hours = worked_hours

            task.status = new_status
            task.save()

            serializer = TaskSerializer(task)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": "An unexpected error occurred.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class TaskReportAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrSuperAdmin]

    def get(self, request, pk):
        try:
            task = get_object_or_404(Task, pk=pk)

            if task.status != 'Completed':
                return Response(
                    {"error": "Report is only available for completed tasks."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            report_data = {
                "task_id": task.id,
                "assignee": task.assigned_to.username,
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date,
                "status": task.status,
                "completion_report": task.completion_report,
                "worked_hours": task.worked_hours,
            }

            return Response(report_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": "An error occurred while fetching the task report.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )