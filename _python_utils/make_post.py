"""
A simple script to automatically create a post rather than
muck about with file name formats
"""
##-- imports
from os.path import join, isfile, exists, abspath
from os.path import split, isdir, splitext, expanduser
from os import listdir
from time import strftime
from os.path import splitext, split
import logging as root_logger
##-- end imports

##-- logging
LOGLEVEL      = root_logger.DEBUG
LOG_FILE_NAME = "log.{}".format(splitext(split(__file__)[1])[0])
root_logger.basicConfig(filename=LOG_FILE_NAME, level=LOGLEVEL, filemode='w')

console = root_logger.StreamHandler()
console.setLevel(root_logger.INFO)
root_logger.getLogger('').addHandler(console)
logging = root_logger.getLogger(__name__)
##-- end logging

divider          = "---\n"
target_directory = "_posts"
file_format      = "md"
time_format      = "%Y-%m-%d"
time_str         = strftime(time_format)
title            = input("Title of Post: ")
tags             = {x.strip() for x in input("Initial Tags: ").split(" ")}

file_name = "{}-{}.{}".format(time_str, title.replace(" ","_"), file_format)


if __name__ == '__main__':
    logging.info("Creating: {}".format(join(target_directory, file_name)))
    with open(join(target_directory, file_name), 'w') as f:
        f.write(divider)
        f.write("layout: post\n")
        f.write("title: {}\n".format(title))
        f.write("date: {}\n".format(time_str))
        f.write("tags: {}\n".format(" ".join(tags)))
        f.write(divider)
