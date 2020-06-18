

from django.urls import path, include
from .views import CandidatesListViewHome, CandidateDetailView, AddCandidateView, results_GSMC, \
    CandidateUpdateView,CandidateDeleteView, deleteAllCandidates_GSMC, deleteAllCandidatesConfirm_GSMC, clearVotes_GSMC




urlpatterns = [
    path("",CandidatesListViewHome.as_view(), name="home-GSMC"),
    path('addCandidate/',AddCandidateView.as_view(), name="addCandidate-GSMC" ),
    path('<int:pk>/',CandidateDetailView.as_view(), name="candidateDetail-GSMC"),
    path('<int:pk>/update/',CandidateUpdateView.as_view(), name="candidateUpdate-GSMC" ),
    path('<int:pk>/delete/',CandidateDeleteView.as_view(), name="candidateDelete-GSMC" ),

    path("results/", results_GSMC, name="results-GSMC"),
    path('deleteAllCandidatesConfirm/',deleteAllCandidatesConfirm_GSMC, name ="deleteAllCandidatesConfirm-GSMC"),
    path('deleteAllCandidatesConfirm/delete',deleteAllCandidates_GSMC, name ="deleteAllCandidates-GSMC"),
    path("clearVotes/",clearVotes_GSMC , name="clearVotes-GSMC"),




]