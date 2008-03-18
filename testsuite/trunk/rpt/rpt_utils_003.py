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
from rpt_resources import rptentries, objcmp
from random import *

class TestSequence(unittest.TestCase):
       
    """
    runTest : Starts with an RPTable of 10 resources and fetches
 * them randomly by the ResourceId and compares them against the original
 * resource. A failed comparison means the test failed,
 * otherwise the test passed.
    
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):

        rptable = RPTable()
        oh_init_rpt(rptable);
        resources = [];
        RAND_MAX = 0x7fff
        i=0
        k=0

        while i<10:
                self.assertEqual(oh_add_resource(rptable, rptentries[i], None, 0), 0)
                resources.append(rptentries[i])
                i=i+1
        
        j=i
        
        while resources :
                randentry = tmpentry = SaHpiRptEntryT()
                tmpnode = []

                k = int(i*random()/(RAND_MAX+1.0) )
                tmpnode = resources[k]
                randentry = tmpnode
                
                tmpentry = oh_get_resource_by_id(rptable, randentry.ResourceId)
                self.assertEqual(not (tmpentry), 0)   
                self.assertEqual((objcmp(randentry, tmpentry) and objcmp(tmpentry, SaHpiRptEntryT)), 0)    
                resources.remove(tmpnode)
                i=i-1

if __name__=='__main__':
        unittest.main()    
