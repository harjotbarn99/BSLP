from django.shortcuts import render
from get_seeded_manage_cand.models import Candidate
from get_seeded_manage_voting.votingHelper import getVotingStatus, castVote
from django.contrib import messages

# Create your views here.

def votingPage_GSV(request):
    if request.method == "GET":
        techList = Candidate.objects.filter(category="Technology")
        genList = Candidate.objects.filter(category="General")
        socialList = Candidate.objects.filter(category="Social")
        context = {
            "techs": techList,
            "gens" : genList,
            "socs" : socialList,
            "title" : "Voting Page - Get Seeded",
            "vStat": getVotingStatus()
        }
        return render(request, "get_seeded_voting/votingPage_GSV.html", context)
    elif request.method == "POST":
        data = request.POST
        message = castVote(data)
        techList = Candidate.objects.filter(category="Technology")
        genList = Candidate.objects.filter(category="General")
        socialList = Candidate.objects.filter(category="Social")
        context = {
            "techs": techList,
            "gens": genList,
            "socs": socialList,
            "title": "Voting Page - Get Seeded",
            "vStat": getVotingStatus()
        }
        messages.success(request, message)
        return render(request, "get_seeded_voting/votingPage_GSV.html", context)
    context = {
        "title" : "Voting Page - Get Seeded"
    }
    messages.error(request, "problem during loading page")
    return render(request, "get_seeded_voting/votingPage_GSV.html", context)