"""
Process all posts and create tag aggregate pages
"""
from os.path import join,isfile,exists,isdir
from os import listdir
import yaml
# Setup root_logger:
from os.path import splitext, split
import logging as root_logger
LOGLEVEL = root_logger.DEBUG
LOG_FILE_NAME = "log.{}".format(splitext(split(__file__)[1])[0])
root_logger.basicConfig(filename=LOG_FILE_NAME, level=LOGLEVEL, filemode='w')

console = root_logger.StreamHandler()
console.setLevel(root_logger.INFO)
root_logger.getLogger('').addHandler(console)
logging = root_logger.getLogger(__name__)
##############################


load_dir = "_posts"
save_dir = "tags"

def load_yaml_data(filename):
    """ Load a specified file, parse it as yaml """
    logging.info("Loading Yaml For: {}".format(filename))
    with open(filename,'r') as f:
        count = 0;
        total = ""
        currLine = f.readline()
        while count < 2 and currLine is not None:
            if currLine == "---\n":
                count += 1
            elif count == 1:
                total += currLine
            currLine = f.readline()
    return yaml.safe_load(total)

def load_all_posts(dir_name):
    logging.info("Loading all Posts in {}".format(dir_name))
    files = listdir(dir_name)
    loadedData = [load_yaml_data(join(dir_name,f)) for f in files if splitext(f)[1] == ".md"]
    tagSet = set([t for x in loadedData for t in x['tags'].split(" ")])
    return tagSet

def make_tag_pages(tagSet):
    logging.info("Making Tag Pages: {}".format(tagSet))
    for tag in tagSet:
        write_yaml_tag_file(save_dir,tag)

def write_yaml_tag_file(dir,tag):
    logging.info('Creating Tag File: {}'.format(tag))
    with open(join(dir,"{}.md".format(tag)),'w') as f:
        f.write('---\n')
        f.write('layout: tag\n')
        f.write('title: {}\n'.format(tag))
        f.write('tag: {}\n'.format(tag))
        f.write('permalink: /tags/{}/\n'.format(tag))
        f.write('sitemap: false\n')
        f.write('---\n')


def write_index_file(dir_name):
    index_str = """---
layout: default
title: Tag Index
---
<h1> {{ page.title }} </h1>
<ul>
  {% assign sortedTags = site.tags | sort %}
  {% for tag in sortedTags %}
  <li>
    <a class="mono" href="{{site.github.url}}/tags/{{tag[0]}}">#{{tag[0]}}</a>
  </li>
  {% endfor %}
</ul>"""

    with open(join(dir_name, "index.html"), 'w') as f:
        f.write(index_str)


if __name__ == '__main__':
    logging.info('Creating Tag Files')
    tagSet = load_all_posts(load_dir)
    make_tag_pages(tagSet)
    write_index_file(save_dir)
