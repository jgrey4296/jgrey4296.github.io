## pelicanconf.py -*- mode: Py -*-

AUTHOR       = 'John Grey'
SITENAME     = 'Mostly Harmless'
SITEURL      = "https://jgrey4296.github.io"
DEFAULT_LANG = 'en'

IGNORE_FILES = ["index.rst"]

# # Feed generation is usually not desired when developing
FEED_ALL_ATOM         = None
CATEGORY_FEED_ATOM    = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None

PLUGINS = []

# DEFAULT_METADATA       = {}
READERS                = {}

PORT         =  8000
BIND         =  '127.0.0.1'

# # [paths]
PATH                        = '.'
OUTPUT_PATH                 = '.pelican.site'
THEME                       = './_static/theme'
CACHE_PATH                  = 'cache'

##-- site.settings

# [site.settings]
ARTICLE_PERMALINK_STRUCTURE = ''
DEFAULT_ORPHANS             = 0
DEFAULT_PAGINATION          = False
DOCUTILS_SETTINGS           = {}
EXTRA_PATH_METADATA         = {}
FILENAME_METADATA           = r'(?P<date>\d{4}-\d{2}-\d{2}).*'
INDEX_SAVE_AS               = 'index.html'
# LOCALE                      = []  # defaults to user locale
PAGE_TRANSLATION_ID         = 'slug'
ARTICLE_TRANSLATION_ID      = 'slug'
PATH_METADATA               = ''

# [site.settings.datetime]
DATE_FORMATS                = {}
DEFAULT_DATE_FORMAT         = '%a %d %B %Y'
TIMEZONE                    = 'Europe/Rome'

# [site.setup]
INTRASITE_LINK_REGEX        =  '[{|](?P<what>.*?)[|}]'
LINKS                       = []
SOCIAL                      = []

# [site.static]
STATIC_PATHS                = ['_static/images', '_static/css', '_static/fonts', '_static/js']
STATIC_EXCLUDES             = []

# [site.articles]
DEFAULT_CATEGORY       =  'misc'
ARTICLE_PATHS          =  ["_posts", "_resources"]
ARTICLE_EXCLUDES       =  []
FORMATTED_FIELDS       =  ['summary']
SUMMARY_END_SUFFIX     =  '…'
SUMMARY_MAX_LENGTH     =  50

# [site.pages]
PAGE_EXCLUDES               =  ['_obsolete', 'wiki_', '.github', '.pelican.site', '.sphinx.site', '.site', '.tasks', '.temp']
PAGE_PATHS                  =  ['pages']

##-- end site.settings

##-- text and templates
# [site.theme]
THEME_STATIC_DIR       = '_theme'    # output dir name
THEME_STATIC_PATHS     = ['static']  # copy paths from theme
CSS_FILE               = 'main.css'

# [site.templates]
TEMPLATE_PAGES            = {}
TEMPLATE_EXTENSIONS       = ['.html']
THEME_TEMPLATES_OVERRIDES = []
DIRECT_TEMPLATES          = ['index', 'tags', 'categories', 'archives']
PAGINATED_TEMPLATES       = {'index': False, 'tag': False, 'category' : False,  'author' : False, 'resources': True}

# [rst]
PYGMENTS_RST_OPTIONS           =  {}

# [markdown]
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite" : {'css_class': 'highlight'},
        "markdown.extensions.extra"      : {},
        "markdown.extensions.meta"       : {},
        },
    "output_format": "html5",
}

##-- end text and templates

##-- build.config
# [build.core]
OUTPUT_SOURCES_EXTENSION = '.text'
DISQUS_SITENAME          = ""
GOOGLE_ANALYTICS         = ""
OUTPUT_RETENTION         =  []
IGNORE_FILES             =  ['.#*']

# [build.options]
OUTPUT_SOURCES                 = False
DELETE_OUTPUT_DIRECTORY        = False
STATIC_EXCLUDE_SOURCES         = True
FEED_ALL_ATOM                  = False
CATEGORY_FEED_ATOM             = False
TRANSLATION_FEED_ATOM          = False
AUTHOR_FEED_ATOM               = False
AUTHOR_FEED_RSS                = False
RELATIVE_URLS                  = True
RSS_FEED_SUMMARY_ONLY          = True
STATIC_CREATE_LINKS            = True
USE_FOLDER_AS_CATEGORY         = True
WITH_FUTURE_DATES              = True
NEWEST_FIRST_ARCHIVES          = True
REVERSE_CATEGORY_ORDER         = False
DISPLAY_PAGES_ON_MENU          = True
DISPLAY_CATEGORIES_ON_MENU     = True
STATIC_CHECK_IF_MODIFIED       = False

# [feeds]
FEED_ALL_ATOM                  = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM             = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_ATOM               = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS                = 'feeds/{slug}.rss.xml'
TRANSLATION_FEED_ATOM          = 'feeds/all-{lang}.atom.xml'
FEED_MAX_ITEMS                 = 100

##-- end build.config

##-- jinja
# [jinja]
JINJA_FILTERS                          =  {}
JINJA_GLOBALS                          =  {}
JINJA_TESTS                            =  {}

# [jinja.JINJA_ENVIRONMENT]
trim_blocks   = True
lstrip_blocks = True
extensions    = ['jinja2.ext.debug']

##-- end jinja

##-- pelican settings
# [logging]
LOG_FILTER                             =  []

# [typogrify]
TYPOGRIFY                              =  False
TYPOGRIFY_IGNORE_TAGS                  =  []
TYPOGRIFY_DASHES                       =  'default'

# [slugify]
SLUG_REGEX_SUBSTITUTIONS               =  [
 ["[^\\w\\s-]", ''],  # remove non-alphabetical/whitespace/'-' chars
 ["(?u)\\A\\s*", ''], # strip leading whitespace
 ["(?u)\\s*\\Z", ''], # strip trailing whitespace
 ["[-\\s]+",    '-'],   # reduce multiple whitespace or '-' to single '-'
]
SLUGIFY_SOURCE                         =  'title'
SLUGIFY_USE_UNICODE                    =  False
SLUGIFY_PRESERVE_CASE                  =  False

# [cache]
CACHE_CONTENT                          = False
LOAD_CONTENT_CACHE                     = False
GZIP_CACHE                             = True
CONTENT_CACHING_LAYER                  = 'reader'
CHECK_MODIFIED_METHOD                  = 'mtime'

##-- end pelican settings

##-- urls
# [[site.urls]]
ARTICLE_URL                            =  '{slug}.html'
ARTICLE_SAVE_AS                        =  '{slug}.html'
ARTICLE_ORDER_BY                       =  'reversed-date'
ARTICLE_LANG_URL                       =  '{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS                   =  '{slug}-{lang}.html'
DRAFT_URL                              =  'drafts/{slug}.html'
DRAFT_SAVE_AS                          =  'drafts/{slug}.html'
DRAFT_LANG_URL                         =  'drafts/{slug}-{lang}.html'
DRAFT_LANG_SAVE_AS                     =  'drafts/{slug}-{lang}.html'

PAGE_URL                               =  'pages/{slug}.html'
PAGE_SAVE_AS                           =  'pages/{slug}.html'
PAGE_ORDER_BY                          =  'basename'
PAGE_LANG_URL                          =  'pages/{slug}-{lang}.html'
PAGE_LANG_SAVE_AS                      =  'pages/{slug}-{lang}.html'

DRAFT_PAGE_URL                         =  'drafts/pages/{slug}.html'
DRAFT_PAGE_SAVE_AS                     =  'drafts/pages/{slug}.html'
DRAFT_PAGE_LANG_URL                    =  'drafts/pages/{slug}-{lang}.html'
DRAFT_PAGE_LANG_SAVE_AS                =  'drafts/pages/{slug}-{lang}.html'

STATIC_URL                             =  '{path}'
STATIC_SAVE_AS                         =  '{path}'

CATEGORY_URL                           =  'category/{slug}.html'
CATEGORY_SAVE_AS                       =  'category/{slug}.html'

TAG_URL                                =  'tag/{slug}.html'
TAG_SAVE_AS                            =  'tag/{slug}.html'

AUTHOR_URL                             =  'author/{slug}.html'
AUTHOR_SAVE_AS                         =  'author/{slug}.html'

YEAR_ARCHIVE_URL                       =  ''
YEAR_ARCHIVE_SAVE_AS                   =  ''
MONTH_ARCHIVE_URL                      =  ''
MONTH_ARCHIVE_SAVE_AS                  =  ''
DAY_ARCHIVE_URL                        =  ''
DAY_ARCHIVE_SAVE_AS                    =  ''

##-- end urls
