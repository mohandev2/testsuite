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
from rpt_resources import *
from random import *

class TestSequence(unittest.TestCase):
       
    """
    runTest : Starts with an RPTable of 10 resources, multiple rdrs
 * on some resources. Remove rdr. Check if resource was removed
 * searching for it by type. If not fail, else passed test.
    
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        rptable = RPTable()
        oh_init_rpt(rptable)
        tmprdr = None
        i = 0
        
        for rpte in rptentries:
            self.assertEqual(oh_add_resource(rptable, rptentries[i], None, 0), 0)
        
        i=0
        for sensor in sensors:
            self.assertEqual(oh_add_rdr(rptable, SAHPI_FIRST_ENTRY, sensors[i], None,0), 0)
           
        for i in range (5, 7):  
            self.assertEqual(oh_add_rdr(rptable, rptentries[9].ResourceId, sensors[i], None,0), 0)
            
        oh_remove_rdr(rptable, rptentries[0].ResourceId, sensors[1].RecordId)
        tmprdr = oh_get_rdr_by_type(rptable, rptentries[0].ResourceId, sensors[1].RdrType, sensors[1].RdrTypeUnion.SensorRec.Num)
        self.assertEqual(not(tmprdr==None), False)
                        
if __name__=='__main__':
        unittest.main()    
