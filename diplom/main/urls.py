from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.index), name='home'),
    path('chapter', login_required(views.chapter), name='chapter'),
    path('responsible', login_required(views.responsible), name='responsible'),
    path('period', login_required(views.period), name='period'),
    path('division', login_required(views.division), name='division'),
    path('report', login_required(views.report), name='report'),
    path('delete-records', login_required(views.delete_records), name='delete_records'),
    path('logout_view', login_required(views.logout_view), name='logout_view'),
    path('<int:pk>/update', login_required(views.update.as_view()), name='update'),
    path('<int:pk>/update_chapter', login_required(views.update_chapter.as_view()), name='update_chapter'),
    path('<int:pk>/update_period', login_required(views.update_period.as_view()), name='update_period'),
    path('<int:pk>/update_division', login_required(views.update_division.as_view()), name='update_division'),
    path('<int:pk>/update_responsible', login_required(views.update_responsible.as_view()), name='update_responsible'),
]
