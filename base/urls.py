from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,DeleteView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'), 
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'), 
    path('task-create/', TaskCreate.as_view(), name='task-create'), #할일 추가 경로
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'), #할일 수정 
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    
]