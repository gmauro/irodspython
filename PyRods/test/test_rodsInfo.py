# Copyright (c) 2013, University of Liverpool
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
# Author       : Jerome Fuselier
#

import unittest
from common import *
from irods import *

class testRodsInfo(iRODSTestCase):

    def test_dataObjInfo_t(self):
        v1 = create_dataObjInfo_t()
        v2 = create_dataObjInfo_t()
        self.assertTrue(test_dataObjInfo_t(v1, v2))
  
    def test_miscSvrInfo_t(self):
        v1 = create_miscSvrInfo_t()
        v2 = create_miscSvrInfo_t()
        self.assertTrue(test_miscSvrInfo_t(v1, v2))
  
    def test_rodsObjStat_t(self):
        v1 = create_rodsObjStat_t()
        v2 = create_rodsObjStat_t()
        self.assertTrue(test_rodsObjStat_t(v1, v2))
  
    def test_tagStruct_t(self):
        v1 = create_tagStruct_t()
        v2 = create_tagStruct_t()
        self.assertTrue(test_tagStruct_t(v1, v2))
  
    def test_specColl_t(self):
        v1 = create_specColl_t()
        v2 = create_specColl_t()
        self.assertTrue(test_specColl_t(v1, v2))
  
    def test_subFile_t(self):
        v1 = create_subFile_t()
        v2 = create_subFile_t()
        self.assertTrue(test_subFile_t(v1, v2))
  
    def test_keyValPair_t(self):
        v1 = create_keyValPair_t()
        v2 = create_keyValPair_t()
        self.assertTrue(test_keyValPair_t(v1, v2))
  
    def test_inxIvalPair_t(self):
        v1 = create_inxIvalPair_t()
        v2 = create_inxIvalPair_t()
        self.assertTrue(test_inxIvalPair_t(v1, v2))
  
    def test_inxIvalPair_t(self):
        v1 = create_inxIvalPair_t()
        v2 = create_inxIvalPair_t()
        self.assertTrue(test_inxIvalPair_t(v1, v2))
 
    def test_rescInfo_t(self):
        v1 = create_rescInfo_t()
        v2 = create_rescInfo_t()
        self.assertTrue(test_rescInfo_t(v1, v2))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testRodsInfo))
    
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
