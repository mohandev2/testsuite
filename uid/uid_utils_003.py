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

#!/usr/bin/env python

from openhpi import *
import unittest

class TestSequence(unittest.TestCase):
    """
    runTest : Get 10 new unique ids. Get 10 more with the same entity paths.
    Passes if returned ids are equal to previous ones,
    otherwise fails.

    Return value: 0 on success, 1 on failure
    """
    iid = [0,1,2,3,4,5,6,7,8,9,10]
    def runTest(self):
        
        ep = SaHpiEntityPathT()
        self.assertEqual(oh_uid_initialize(),0)
        oh_init_ep(ep)
        
        for i in range (0, 10):
            ep.Entry[0].EntityLocation = i
            self.iid[i] = oh_uid_from_entity_path(ep)
        
        for i in range (0, 10):
            ep.Entry[0].EntityLocation = i
            rid = oh_uid_from_entity_path(ep)
            self.assertEqual((self.iid[i] != rid), 0)
                              
if __name__=='__main__':
        unittest.main()        
