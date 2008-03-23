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

import unittest
import rpt_resources
from openhpi import *
from rpt_resources import *

class TestSequence(unittest.TestCase):
       
    """
    runTest : Starts with an RPTable of 1 resource, adds 5 sensors to first resource.
    Fetches an rdr using get_next with a Record Id not present in the resource.
    Success if the interface returns an error, otherwise there was a failure.
 
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        
        rptable = RPTable()
        oh_init_rpt(rptable)
        
        self.assertEqual(oh_add_resource(rptable, rptentries[0], None, 1), 0)  
          
        for sensor in sensors:
            self.assertEqual(oh_add_rdr(rptable, rptentries[0].ResourceId, sensor, None, 1), 0)  
        self.assertEqual(oh_get_rdr_next(rptable, rptentries[0].ResourceId, 1234567)==None, True) 
            
if __name__=='__main__':
        unittest.main()    
