The Demos
---------

### portindex

To index your ports tree into a database in /usr/ports/INDEX.db, run:

    ./portindex -v

You may find `bsdportsearch/doc.py` interesting, to see what's going on under
the hood.

### portsearch

To search your constructed database (/usr/ports/INDEX.db), run:

    ./portsearch query_string

To get long-format output (similar to make search), use the -l option:

    ./portsearch -l '(bash OR ksh)' AND 'maintainer=obrien*'
