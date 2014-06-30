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

class testDataObj(iRODSTestCase):

    def test_collInp_t(self):
        v1 = create_collInp_t()
        v2 = create_collInp_t()
        self.assertTrue(test_collInp_t(v1, v2))
 
    def test_dataCopyInp_t(self):
        v1 = create_dataCopyInp_t()
        v2 = create_dataCopyInp_t()
        self.assertTrue(test_dataCopyInp_t(v1, v2))
   
    def test_dataObjCopyInp_t(self):
        v1 = create_dataObjCopyInp_t()
        v2 = create_dataObjCopyInp_t()
        self.assertTrue(test_dataObjCopyInp_t(v1, v2))

    def test_dataObjInp_t(self):
        v1 = create_dataObjInp_t()
        v2 = create_dataObjInp_t()
        self.assertTrue(test_dataObjInp_t(v1, v2))
    
    def test_dataOprInp_t(self):
        v1 =  create_dataOprInp_t()
        v2 =  create_dataOprInp_t()
        self.assertTrue(test_dataOprInp_t(v1, v2))
     
    def test_openedDataObjInp_t(self):
        v1 =  create_openedDataObjInp_t()
        v2 =  create_openedDataObjInp_t()
        self.assertTrue(test_openedDataObjInp_t(v1, v2))
    
    def test_openStat_t(self):
        v1 = create_openStat_t()
        v2 = create_openStat_t()
        self.assertTrue(test_openStat_t(v1, v2))
    
    def test_portalOprOut_t(self):
        v1 = create_portalOprOut_t()
        v2 = create_portalOprOut_t()
        self.assertTrue(test_portalOprOut_t(v1, v2))
    
    def test_portList_t(self):
        v1 = create_portList_t()
        v2 = create_portList_t()
        self.assertTrue(test_portList_t(v1, v2))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testDataObj))
    
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())
