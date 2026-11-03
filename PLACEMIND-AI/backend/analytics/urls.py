from django.urls import path
from .views import PredictRiskView, AdminDashboardStatsView, StudentRiskListView

urlpatterns = [
    path('predict-risk/', PredictRiskView.as_view(), name='predict-risk'),
    path('admin-stats/', AdminDashboardStatsView.as_view(), name='admin-stats'),
    path('student-risks/', StudentRiskListView.as_view(), name='student-risks'),
]
