__author__ = 'welserjr'

import pdfkit

pdfkit.from_url('http://twitter.com', 'fb.pdf')
pdfkit.from_file('test.html', 'welser.pdf')
pdfkit.from_string('Hello!', 'out3.pdf')

