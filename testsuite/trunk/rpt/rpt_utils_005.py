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
import r
from random import *

class TestSequence(unittest.TestCase):
       
    """
    runTest : Starts with an RPTable of 10 resources with data and fetches
 * them randomly by the Resource Id and compares the data against
 * the original data. A failed comparison means the test failed,
 * otherwise the test passed.
        
    Return value: 0 on success, 1 on failure
    """
    def runTest(self):

        print "start"
    
        rptable = RPTable()
        oh_init_rpt(rptable);
        resources = [];
        RAND_MAX = 0x7fff
        i=0
        k=0

        while i<10:
                data = r.rptentries[i].ResourceId
                self.assertEqual(oh_add_resource(rptable, r.rptentries[i], data, 0), 0)
                resources.append(r.rptentries[i])
                i=i+1
        
       
        while resources :
                randentry = tmpentry = SaHpiRptEntryT()
##                tmpnode = []

                k = randrange(0,i,1)

                randentry= resources[k]
##                randentry = tmpnode

                tmpentry = oh_get_resource_data(rptable, randentry.ResourceEntity)

                self.assertEqual(not (tmpentry), 0)   
                self.assertEqual((r.objcmp(randentry, tmpentry) and r.objcmp(tmpentry, SaHpiRptEntryT)), 0)    
                resources.remove(randentry)
                i=i-1

if __name__=='__main__':
        unittest.main()    
