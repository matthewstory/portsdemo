import xapian as _x

from . import TERM_MAP

def query_parser(x_db):
    qp = _x.QueryParser()
    stemmer = _x.Stem("english")
    qp.set_stemmer(stemmer)
    qp.set_database(x_db)
    qp.set_stemming_strategy(_x.QueryParser.STEM_SOME)
    for k,v in TERM_MAP.iteritems():
        qp.add_prefix(k, v)
    return qp
