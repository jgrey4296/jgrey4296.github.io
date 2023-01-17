# -*- mode:doit; -*-
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

from bkmkorg.doot_tasks import bibtex

if __name__ == "dooter":
    # the equivalent of main
    bib_locs = doot.locs.extend(name="bibtex", src="resources/bibliography")
    cleaner = bibtex.BibtexClean(dirs=bib_locs)
    report = bibtex.BibtexReport(dirs=bib_locs)
    pass
