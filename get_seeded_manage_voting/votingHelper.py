import string
import random
from .models import VoteCode
import html
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


def addVoteCodes(num):
    for i in range(int(num)):
        code_ = randomCode(4, 2)
        VoteCode.objects.create(code=code_).save()
    return "done"


def checkCode(codeRaw):
    codeUpperCase = codeRaw.upper()
    toRet = ""
    try:
        obj = VoteCode.objects.get(code=codeUpperCase)
        toRet = "success"
    except VoteCode.DoesNotExist:
        toRet = "failed"
    return toRet


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
    print(data)
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
    if stat == "failed":
        return "Wrong vote code"
    elif stat != "success":
        return "problem in castVote"
    else:
        deleteVoteCode(code)
        li = [
            voteIncrement(gen, "General"),
            voteIncrement(soc, "Social"),
            voteIncrement(tech, "Technology"),
        ]
        print(li)
        return voteMessage(li)

