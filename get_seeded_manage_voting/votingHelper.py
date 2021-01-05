import string
import random
import csv
import html

from .models import VoteCode
from get_seeded_manage_cand.models import Candidate


# generates a random string with numAlph alphabets and numNum  numbers
def randomCode(numAlph, numNum):
    code = ""
    for i in range(numAlph):
        code += random.choice(string.ascii_uppercase)
    for i in range(numNum):
        code += random.choice(string.digits)
    finalCode = ""
    for i in random.sample(code, len(code)):
        finalCode += i
    return finalCode


def checkCode(codeRaw):
    codeUpperCase = codeRaw.upper()
    try:
        obj = VoteCode.objects.get(code=codeUpperCase)
        return True
    except VoteCode.DoesNotExist:
        return False


def add_vote_code(code_):
    stat = checkCode(code_)
    if not stat:
        VoteCode.objects.create(code=code_).save()
        return True
    else:
        return False


def addVoteCodes(num):
    if len(VoteCode.objects.all()) + num > 1000:
        return "failed"
    i = 0
    while i != num:
        code_ = randomCode(4, 2)
        if add_vote_code(code_):
            i += 1
    return "done"


def addByCsv(file, to_leave=7, index=-1):
    with open("current.csv", "wb") as f:
        f.write(file)
    with open("current.csv", "r") as r:
        data = csv.reader(r)
        i = 0
        for line in data:
            i += 1
            if i < to_leave:
                continue
            code_ = line[-1]
            if code_ == "":
                code_ = line[2]
            add_vote_code(code_)
    return i - to_leave + 1


# Voting status

votingStatus = "Voting is disabled"

# disable voting
def disableVoting():
    global votingStatus
    votingStatus = "Voting is disabled"
    return


# enable voting
def enableVoting():
    global votingStatus
    votingStatus = "Voting is enabled"
    return


# Change voting status
def changeVotingStat():
    print("changing voting stat")
    global votingStatus
    if votingStatus == "Voting is enabled":
        disableVoting()
        return "voting disabled"
    elif votingStatus == "Voting is disabled":
        enableVoting()
        return "Voting enabled"
    return "problem changing status"


def getVotingStatus():
    return votingStatus


def deleteVoteCode(codeRaw):
    codeUpperCase = codeRaw.upper()
    obj = VoteCode.objects.get(code=codeUpperCase)
    obj.delete()
    return


def voteMessage(li):
    if "None" in li[0] or "None" in li[1] or "None" in li[2]:
        return (
            li[0]
            + ";  "
            + li[1]
            + ";  "
            + li[2]
            + ";   Please contact Get Seeded team if selecting None for a category was not your intention"
        )
    elif "exist" in li[0] or "exist" in li[1] or "exist" in li[2]:
        return (
            li[0]
            + ";  "
            + li[1]
            + ";  "
            + li[2]
            + ";   Please contact Get Seeded team as a Venture you selected does not exist"
        )
    else:
        return li[0] + ";  " + li[1] + ";  " + li[2]


def voteIncrement(vent, category):
    if vent == "none":
        return f"None was selected for {category}"
    else:
        try:
            cand = Candidate.objects.get(venture=vent)
            cand.castVote()
        except Candidate.DoesNotExist:
            return f"Venture does not exist {vent}"
    return f"Successfully voted for {vent} in category {cand.category}"


def castVote(data):
    if votingStatus == "Voting is disabled":
        return votingStatus + ", please wait for the Get seeded team to enable it"
    try:
        code = html.escape(data.get("voteCode"))
        gen = html.escape(data.get("gen"))
        soc = html.escape(data.get("soc"))
        tech = html.escape(data.get("tech"))
    except VoteCode.DoesNotExist:
        return "Problem with form data "
    if code == "":
        return "Vote Code is empty"
    stat = checkCode(code)
    print(stat)
    if not stat:
        return "Wrong vote code"
    else:
        deleteVoteCode(code)
        li = [
            voteIncrement(gen, "General"),
            voteIncrement(soc, "Social"),
            voteIncrement(tech, "Technology"),
        ]
        return voteMessage(li)

