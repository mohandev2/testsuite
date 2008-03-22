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
from openhpi import *
from rpt_resources import *

class TestSequence(unittest.TestCase):
    """
    runTest : Starts with an RPTable of 10 resources, multiple rdrs
    on some resources. Remove rdr. Check if resource was removed
    searching for it by id. If not fail, else passed test.
    
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):
        rptable = RPTable()
        oh_init_rpt(rptable)

        for rpte in rptentries:
            self.assertEqual(oh_add_resource(rptable, rpte, None, 0), 0)

        for sensor in sensors:
            self.assertEqual(oh_add_rdr(rptable, SAHPI_FIRST_ENTRY, sensor, None,0), 0)

        for i in range (0, 7):  
            self.assertEqual(oh_add_rdr(rptable, rptentries[9].ResourceId, sensors[i], None,0), 0)

        oh_remove_rdr(rptable, rptentries[0].ResourceId, sensors[1].RecordId)
        tmprdr = oh_get_rdr_by_id(rptable, rptentries[0].ResourceId,sensors[1].RecordId)
        self.assertEqual(not(tmprdr==None), False)

if __name__=='__main__':
        unittest.main()    
