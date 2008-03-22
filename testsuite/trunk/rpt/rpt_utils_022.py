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
from rpt_resources import rptentries
from rpt_resources import sensors

class TestSequence(unittest.TestCase):
  
    """
    runTest : Starting with an empty RPTable, adds 1 resource to it
    that has an invalid Resource Id like SAHPI_FIRST_ENTRY.
    Passes the test if the interface returns an error, else it fails.
 *
 Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        rptable = RPTable()
        oh_init_rpt(rptable)
               
        rptentries[0].ResourceId = SAHPI_FIRST_ENTRY    
        self.assertEqual(not (oh_add_resource(rptable, rptentries[0], None, 0)), 0)
                       
if __name__=='__main__':
        unittest.main()    
