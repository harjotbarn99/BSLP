from django.urls import path, include
from .views import (
    home_GSMV,
    deleteAllVoteCodesConfirm_GSMV,
    deleteVoteCode_GSMV,
    addVoteCodes_GSMV,
    deleteAllVoteCodes_GSMV,
    changeVotingStat_GSMV,
    add_votes_by_csv_checkin,
)


urlpatterns = [
    path("", home_GSMV, name="home-GSMV"),
    path(
        "deleteAllVoteCodesConfirm",
        deleteAllVoteCodesConfirm_GSMV,
        name="deleteAllVoteCodesConfirm-GSMV",
    ),
    path(
        "deleteAllVoteCodesConfirm/delete",
        deleteAllVoteCodes_GSMV,
        name="deleteAllVoteCodes-GSMV",
    ),
    path("addVoteCodes/", addVoteCodes_GSMV, name="addVoteCodes-GSMV"),
    path("deleteVoteCode/", deleteVoteCode_GSMV, name="deleteVoteCode-GSMV"),
    path("changeVotingStat/", changeVotingStat_GSMV, name="changeVotingStatus-GSMV"),
    path(
        "csvAddCheckinVoteCodes/", add_votes_by_csv_checkin, name="addByCSVcheckin-GSMV"
    ),
]

