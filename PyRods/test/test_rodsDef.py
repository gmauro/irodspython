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

class testRodsDef(iRODSTestCase):

    def test_bytesBuf_t(self):
        v1 = create_bytesBuf_t()
        v2 = create_bytesBuf_t()
        self.assertTrue(test_bytesBuf_t(v1, v2))
 
    def test_getTempPasswordOut_t(self):
        v1 = create_getTempPasswordOut_t()
        v2 = create_getTempPasswordOut_t()
        self.assertTrue(test_getTempPasswordOut_t(v1, v2))
 
    def test_rodsDirent_t(self):
        v1 = create_rodsDirent_t()
        v2 = create_rodsDirent_t()
        self.assertTrue(test_rodsDirent_t(v1, v2))
 
    def test_rodsHostAddr_t(self):
        v1 = create_rodsHostAddr_t()
        v2 = create_rodsHostAddr_t()
        self.assertTrue(test_rodsHostAddr_t(v1, v2))
 
    def test_rodsRestart_t(self):
        v1 = create_rodsRestart_t()
        v2 = create_rodsRestart_t()
        self.assertTrue(test_rodsRestart_t(v1, v2))
 
    def test_rodsStat_t(self):
        v1 = create_rodsStat_t()
        v2 = create_rodsStat_t()
        self.assertTrue(test_rodsStat_t(v1, v2))

    def test_version_t(self):
        v1 = create_version_t()
        v2 = create_version_t()
        self.assertTrue(test_version_t(v1, v2))

    def test_transferStat_t(self):
        v1 = create_transferStat_t()
        v2 = create_transferStat_t()
        self.assertTrue(test_transferStat_t(v1, v2))

    def test_operProgress_t(self):
        v1 = create_operProgress_t()
        v2 = create_operProgress_t()
        self.assertTrue(test_operProgress_t(v1, v2))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testRodsDef))
    
    return suite


if __name__ == "__main__":
    unittest.TextTestRunner(verbosity=2).run(suite())