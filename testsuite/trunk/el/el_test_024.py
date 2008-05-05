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


class TestSequence(unittest.TestCase):
       
    """
    runTest : EL test
 *
 * This test verifies failure of oh_el_get when el == None
 *
 * Return value: 0 on success, 1 on failure
    """
    
    def runTest(self):
        
        el = oh_el()
        entry = oh_el_entry()
        prev = next = None
        #prev = next = SaHpiEventLogEntryIdT() 
        retc = None

        # test case 1: el == None
        el = None

        retc, prev, next, entry = oh_el_get(el, SAHPI_NEWEST_ENTRY)
        self.assertEqual (retc == SA_OK,False)
        
if __name__=='__main__':
        unittest.main()  
