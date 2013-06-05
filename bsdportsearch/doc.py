import json
import os
from contextlib import closing

import xapian as _x

from . import ID, MAIN_INDEX, TERM_MAP, SKIP_THESE

def _desc_from_file(desc_path):
    '''Extract description from description file'''
    with closing(open(desc_path, 'r')) as desc_file:
        return desc_file.read()

def data2doc(data, x_db):
    # make a new document
    x_doc = _x.Document()

    # set string ID with Q prefix and data as JSON data
    x_id = 'Q{}'.format(data[ID])
    x_doc.set_data(json.dumps(data))
    x_doc.add_term(x_id)

    # setup indexer
    indexer = _x.TermGenerator()
    indexer.set_stemmer(_x.Stem("english"))
    indexer.set_document(x_doc)

    for k,v in data.iteritems():
        if k in SKIP_THESE:
            continue

        indexer.set_stemming_strategy(_x.QueryParser.STEM_SOME)
        content = v
        # contents of file at desc get indexed
        if k == 'desc':
            content = _desc_from_file(v)
        # basename and full path get indexed for path
        elif k == 'path':
            content = '{} {}'.format(content, os.path.basename(content))
        # category doesn't get stemmed
        elif k == 'category':
            indexer.set_stemming_strategy(_x.QueryParser.STEM_NONE)

        indexer.index_text(content, 1, TERM_MAP[k])
        if k in MAIN_INDEX:
            indexer.index_text(content)
            indexer.increase_termpos()

    return x_id, x_doc
