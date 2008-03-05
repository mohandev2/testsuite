#!/usr/bin/env python
 
"""
 (C) Copyright IBM Corp. 2008
 
 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  This
 file and program are licensed under a BSD style license.  See
 the Copying file included with the OpenHPI distribution for
 full licensing terms.
 
 Authors:
    Jayashree Padmanabhan <jayshree@in.ibm.com>
"""

from types import *
import unittest
from openhpi import *
from random import *
from rpt_resources import *

class TestSequence(unittest.TestCase):
       
    """
    runTest : Starting with an empty RPTable, adds 1 resource to it with data.
 * Fetches the data back using a NULL table as a parameter.
 * Passes the test if the interface returns NULL, else it fails.
 *
 Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        rptable = RPTable()
        oh_init_rpt(rptable)
        data1 = "My data 1"
        data2 = "My data 2"
        tmpdata = None
        
        self.assertEqual(oh_add_resource(rptable, rptentries[0], rptentries[0], KEEP_RPT_DATA), 0)
        self.assertEqual(oh_add_resource(rptable, rptentries[1], rptentries[1], KEEP_RPT_DATA), 0)
        
        tmpdata = oh_get_resource_data(rptable, SAHPI_FIRST_ENTRY)
        self.assertEqual(not (data1 != tmpdata), False)        
                
if __name__=='__main__':
        unittest.main()    
