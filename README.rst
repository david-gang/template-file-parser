template-file-parser
====================

.. image:: https://api.codacy.com/project/badge/Grade/f3fb8c7e10fa444581604d43faf90b1d
   :alt: Codacy Badge
   :target: https://app.codacy.com/app/michaelgang/template-file-parser?utm_source=github.com&utm_medium=referral&utm_content=david-gang/template-file-parser&utm_campaign=badger


.. image:: https://api.codacy.com/project/badge/Coverage/bbffba1a08b842d2a3c94a4218efb8ce
   :alt: Codacy Coverage
   :target: https://www.codacy.com/app/michaelgang/template-file-parser?utm_source=github.com&utm_medium=referral&utm_content=david-gang/template-file-parser&utm_campaign=Badge_Coverage

|Build Status|

.. |Build Status| image:: https://travis-ci.org/david-gang/template-file-parser.svg?branch=master
   :target: https://travis-ci.org/david-gang/template-file-parser

**template-file-parser** is an convenient module for parsing files with the python `template syntax <https://docs.python.org/3.6/library/string.html#template-strings>`_.

This module was inspired by the following Stack overview `post <https://stackoverflow.com/a/6385940/2343743>`_.

The need of this module was for me to have an easy templating system manipulating configuration files, without learning a more complete but complicated templating system.
This is especially with configuration files of solr of kubernetes where just a small list of variables needs to be interpolated and written into a file.


Installation
------------

pip install template-file-parser

Usage
-----

::

    from template_file_parser import parse_file
    parse_file(in_file, out_file, variables, safe=False)

These are the parameters:

- in_file: The input file
- out_file: The output file
- variables : a dictionary where the keys are the variables in the template and the values are the values needed to substitute
- safe: if True then then not all variables in the template file needs to be declared. If False, all parameters needs to be declared. For more information read `here <https://docs.python.org/3.6/library/string.html#template-strings>`_

Disclaimer
----------
This library is only supported for python >= 3.4 as it fits my needs, and i don't want to mees up with the encoding differences between python 2 and 3.
This software is beta and breaking changes can occur between versions



