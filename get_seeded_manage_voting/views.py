from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .votingHelper import changeVotingStat, getVotingStatus, addVoteCodes, checkCode, deleteVoteCode
from .models import VoteCode
from django.contrib import messages

# Create your views here.

@login_required
def home_GSMV(request):
    allVoteCodes = VoteCode.objects.all()
    length = len(allVoteCodes)
    context = {"voteCodes": allVoteCodes, "title": "Voting Manager Home - Get Seeded", "vStat": getVotingStatus(), "length": length}
    return render(request, "get_seeded_manage_voting/home_GSMV.html",context)


@login_required
def addVoteCodes_GSMV(request):
    num = request.POST.get("number")
    addVoteCodes(num)
    messages.success(request, f'{num} Vote Codes Added')
    return redirect('home-GSMV')


@login_required
def deleteVoteCode_GSMV(request):
    code = request.POST.get("code")
    status = checkCode(code)
    if status == "failed":
        messages.error(request, f"{code} is not a valid Vote Code")
        return redirect('home-GSMV')
    elif status == "success":
        deleteVoteCode(code)
        messages.success(request, f'Vote Codes deleted')
        return redirect('home-GSMV')
    else:
        messages.error(request, f" there's a bug while deleting code")
        return redirect('home-GSMV')


@login_required
def deleteAllVoteCodesConfirm_GSMV(request):
    return render(request, "get_seeded_manage_voting/deleteAllVoteCodesConfirm_GSMV.html", {"title": "Confirm Deleting All Vote Codes"})


@login_required
def deleteAllVoteCodes_GSMV(request):
    VoteCode.objects.all().delete()
    messages.success(request, f' All Vote Codes Deleted')
    return redirect('home-GSMV')


@login_required
def changeVotingStat_GSMV(request):
    message = changeVotingStat()
    return redirect('home-GSMV')