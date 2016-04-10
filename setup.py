#!/usr/bin/env python
# -*- coding: utf-8 -*-


from distutils.core import setup
import sys

if len(sys.argv) > 1 and sys.argv[1] == 'py2exe':
    import py2exe


setup(
    version     = "0.3.01D",
    description = "Shadowrun 3rd Prob",
    name        = "wxProb3",
    author      = 'TLed',

    options = {"py2exe": {"compressed": 1,
                          "optimize": 2,
                          "ascii": 1,
                          "bundle_files": 1,
                          "dll_excludes": "MSVCP90.dll mswsock.dll powrprof.dll".split(),
                          "excludes": ['_ssl','tcl','tk','pyreadline','optparse','pickle','Tkconstants', 'Tkinter',
                                      'BaseHTTPServer','email','SocketServer',
                              ],
                          },
               },
    zipfile = None,
    windows = ["wxProb3.py"]

)
