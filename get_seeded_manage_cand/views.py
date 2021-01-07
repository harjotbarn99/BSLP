from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Candidate
from get_seeded_manage_voting.votingHelper import changeVotingStat
from django.urls import reverse_lazy

# Create your views here.


class CandidatesListViewHome(LoginRequiredMixin, ListView):
    model = Candidate
    template_name = "get_seeded_manage_cand/candidatesList_GSMC.html"
    context_object_name = "candidates"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Candidates List - Get Seeded Manage"
        context["title"] = title
        return context


class AddCandidateView(LoginRequiredMixin, CreateView):
    template_name = "get_seeded_manage_cand/addCandidate_GSMC.html"
    model = Candidate
    fields = ["name", "category", "venture", "details"]
    # success_url = reverse_lazy("home-GSMC")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Add Candidate - Get Seeded Team"
        context["title"] = title
        return context


class CandidateDetailView(LoginRequiredMixin, DetailView):
    model = Candidate
    template_name = "get_seeded_manage_cand/candidateDetail_GSMC.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Candidate Details - Get Seeded Team"
        context["title"] = title
        return context


class CandidateUpdateView(LoginRequiredMixin, UpdateView):
    model = Candidate
    template_name = "get_seeded_manage_cand/candidateUpdate_GSMC.html"
    fields = ["name", "category", "image", "venture", "details"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Update Candidates - Get Seeded Team"
        context["title"] = title
        return context


class CandidateDeleteView(LoginRequiredMixin, DeleteView):
    model = Candidate
    template_name = "get_seeded_manage_cand/candidateDelete_GSMC.html"
    success_url = reverse_lazy("home-GSMC")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = "Delete Candidates - Get Seeded Team"
        context["title"] = title
        return context


@login_required
def deleteAllCandidatesConfirm_GSMC(request):
    map = {"title": "Delete all - Get Seeded Team "}
    return render(
        request, "get_seeded_manage_cand/deleteAllCandidatesConfirm_GSMC.html"
    )


@login_required
def deleteAllCandidates_GSMC(request):
    Candidate.objects.all().delete()
    messages.success(request, f"All Candidates Deleted")
    return redirect("home-GSMC")


@login_required
def clearVotes_GSMC(request):
    all = Candidate.objects.all()
    for cand in all:
        cand(votes=0).save()
    messages.success(request, f"Votes cleared")
    return redirect("home-GSMC")


@login_required
def results_GSMC(request):
    changeVotingStat()
    techList = Candidate.objects.filter(category="Technology").order_by("-votes")
    genList = Candidate.objects.filter(category="General").order_by("-votes")
    socialList = Candidate.objects.filter(category="Social").order_by("-votes")
    context = {
        "techs": techList,
        "gens": genList,
        "socs": socialList,
        "title": "Voting Page - Get Seeded",
    }
    return render(request, "get_seeded_manage_cand/resultsPage_GSMC.html", context)
