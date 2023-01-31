# -*- mode:doot; -*-
"""
Stub dooter file for task authoring

"""
# https://pydoit.org/
##-- imports
from __future__ import annotations
import pathlib as pl
import sys
import shutil
from doit.action import CmdAction
from doit import create_after
from doit.tools import set_trace, Interactive, PythonInteractiveAction
from doit.task import clean_targets

import doot
##-- end imports

##-- config
DOIT_CONFIG = {
    "action_string_formatting" : "new"
}

##-- end config

##-- post-config doot imports
# from doot.taskslib.groups import *
# from doot.taskslib.groups_secondary import *
##-- end post-config doot imports

from bkmkorg.doot_tasks import basic, bibtex, bookmark, tags

if __name__ == "dooter":
    # the equivalent of main
    cleaner      = bibtex.BibtexClean(locs=doot.locs)
    report       = bibtex.BibtexReport(locs=doot.locs)
    stubber      = bibtex.BibtexStub(locs=doot.locs)
    pdflib_clean = bibtex.LibDirClean(locs=doot.locs)

    noscript     = basic.NoScriptMerge(locs=doot.locs)

    # TODO report
    bkmks_update = bookmark.BookmarksUpdate(locs=doot.locs)
    bkmk_clean   = bookmark.BookmarksCleaner(locs=doot.locs)
    bkmk_report  = bookmark.BookmarksReport(locs=doot.locs)

    # TODO indexer
    tags_clean   = tags.TagsCleaner(locs=doot.locs)
    tags_report  = tags.TagsReport(locs=doot.locs)
    tags_index   = tags.TagsIndexer(locs=doot.locs)

    # TODO interface with jsekyll tasks
