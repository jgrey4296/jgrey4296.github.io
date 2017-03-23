from os.path import join,isfile,exists,isdir 
from os import listdir
import yaml

load_dir = "_posts"
save_dir = "tags"

def load_yaml_data(filename):
    """ Load a specified file, parse it as yaml """
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
            
def load_all_posts(dir):
    files = listdir(dir)
    loadedData = [load_yaml_data(join(dir,f)) for f in files]
    tagSet = set([t for x in loadedData for t in x['tags'].split(" ")])
    return tagSet

def make_tag_pages(tagSet):
    for tag in tagSet:
        write_yaml_tag_file(save_dir,tag)

def write_yaml_tag_file(dir,tag):
    print('Creating Tag File: {}'.format(tag))
    with open(join(dir,"{}.md".format(tag)),'w') as f:
        f.write('---\n')
        f.write('layout: tag\n')
        f.write('title: Posts with tag {}\n'.format(tag))
        f.write('tag: {}\n'.format(tag))
        f.write('permalink: /tags/{}/\n'.format(tag))
        f.write('sitemap: false\n')
        f.write('---\n')


if __name__ == '__main__':
    print('Creating Tag Files')
    tagSet = load_all_posts(load_dir)
    make_tag_pages(tagSet)
