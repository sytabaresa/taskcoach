'''
Task Coach - Your friendly task manager
Copyright (C) 2004-2009 Frank Niessink <frank@niessink.com>

Task Coach is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Task Coach is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import generator, os
from taskcoachlib import meta


css = '''/*
CSS file generated by %(name)s %(version)s for:
%%s. 
You can edit this file, it will not be overwritten by Task Coach.
*/

body {
    color: #333;
    background-color: white;
    font: 11px verdana, arial, helvetica, sans-serif;
}

/* Styles for the table caption */
caption {
    font-size: 18px;
    font-weight: 900;
    color: #778;
}

/* Styles for the whole table */
#table {
    border-collapse: collapse;
    border: 2px solid #ebedff;
    margin: 10px;
    padding: 0;
}

/* Styles for the header row */
.header {
    font: bold 12px/14px verdana, arial, helvetica, sans-serif;
    color: #07a;
    background-color:#ebedff;
}

/* Mark the column that is sorted on */
#sorted {
    text-decoration: underline;
}

/* Styles for a specific column */
.subject {
    font-weight: bold;
}

/* Styles for regular table cells */
td {
    padding: 5px;
    border: 2px solid #ebedff;
}

/* Styles for table header cells */
th {
    padding: 5px;
    border: 2px solid #ebedff;
}

/* Other possibilities to tune the layout include:

   Change the styles for a header of a specific column, in this case the subject 
   column. Note how this style overrides the default style in the HTML file: 
   
   th.subject {
      text-align: center;
   }

   If the exported HTML file contains tasks it possible to change the color of 
   completed (or overdue, duesoon, inactive, active) tasks like this:
   
   .completed {
       color: red;
   }
   
*/
'''%meta.data.metaDict

class HTMLWriter(object):
    def __init__(self, fd, filename=None):
        self.__fd = fd
        self.__filename = filename
        self.__cssFilename = os.path.splitext(filename)[0] + '.css' if filename else ''

    def write(self, viewer, settings, selectionOnly=False):
        cssFilename = os.path.basename(self.__cssFilename)
        htmlText, count = generator.viewer2html(viewer, settings, cssFilename, selectionOnly)
        self.__fd.write(htmlText)
        self._writeCSS()
        return count
    
    def _writeCSS(self):
        if not self.__cssFilename or os.path.exists(self.__cssFilename):
            return
        try:
            fd = open(self.__cssFilename, 'wb')
            fd.write(css%self.__filename)
            fd.close()
        except IOError:
            pass