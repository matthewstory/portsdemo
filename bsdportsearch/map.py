# field name to be used for ID
ID = 'path'

# positions from make describe output
DESCRIBE_POSITIONS = (
    ( 'name', 'XNAME', ),
    ( 'path', 'XPATH', ),        # basename is indexed
    ( 'prefix', 'XPREF', ),      # not indexed at current
    ( 'comment', 'XCOMM', ),
    ( 'desc', 'XDESC', ),        # file contents are indexed
    ( 'maintainer', 'XMAIN', ),
    ( 'category', 'XCATE', ),    # not stemmed
    ( 'extract-dep', 'XEXTR', ), # not indexed at current
    ( 'patch-dep', 'XEXTR', ),   # not indexed at current
    ( 'fetch-dep', 'XFETC', ),   # not indexed at current
    ( 'build-dep', 'XBUIL', ),
    ( 'run-dep', 'XRUND', ),
    ( 'site', 'XSITE', ),        # not indexe at current
)

# list of fields to not be indexed
SKIP_THESE = ( 'prefix', 'extract-dep', 'patch-dep', 'fetch-dep', )

# list of fields to be indexed into non-prefix too
MAIN_INDEX = ( 'name', 'path', 'comment', 'desc', 'maintainer', 'category', )

# term-map
TERM_MAP = {k:v for k,v in DESCRIBE_POSITIONS}
