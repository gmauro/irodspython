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
from irods import *


class iRODSTestCase(unittest.TestCase):
    
    def setUp(self):
        status, self.myEnv = getRodsEnv()
        
        self.assertEqual(status, 0)
        
        self.conn, self.errMsg = rcConnect(self.myEnv.rodsHost, self.myEnv.rodsPort, 
                                           self.myEnv.rodsUserName, self.myEnv.rodsZone)
        
        self.assert_(self.conn)
        
        status = clientLogin(self.conn)
        self.assertEqual(status, 0)
        
        
    def tearDown(self):
        rcDisconnect(self.conn) 


def create_authCheckInp_t():
    tmp = authCheckInp_t()
    tmp.challenge = "challenge"         # char*
    tmp.response = "response"           # char *
    tmp.username = "username"           # char *
    return tmp

def test_authCheckInp_t(a1, a2):
    return a1.challenge == a2.challenge and \
           a1.response == a2.response and \
           a1.username == a2.username

def create_authCheckOut_t():
    tmp = authCheckOut_t()
    tmp.privLevel = 12                     # int
    tmp.clientPrivLevel = 12               # int
    tmp.serverResponse = "serverResponse"  # char *
    return tmp

def test_authCheckOut_t(a1, a2):
    return a1.privLevel == a2.privLevel and \
           a1.clientPrivLevel == a2.clientPrivLevel and \
           a1.serverResponse == a2.serverResponse

def create_authInfo_t():
    tmp = authInfo_t()
    tmp.authScheme = "authScheme"       # char []
    tmp.authFlag = 12                   # int
    tmp.flag = 12                       # int
    tmp.ppid = 12                       # int
    tmp.host = "host"                   # char []
    tmp.authStr = "authStr"             # char []
    return tmp

def test_authInfo_t(a1, a2):
    return a1.authScheme == a2.authScheme and \
           a1.authFlag == a2.authFlag and \
           a1.flag == a2.flag and \
           a1.ppid == a2.ppid and \
           a1.host == a2.host and \
           a1.authStr == a2.authStr

def create_authResponseInp_t():
    tmp = authResponseInp_t()
    tmp.response = "response"   # char *
    tmp.username = "username"   # char *
    return tmp

def test_authResponseInp_t(a1, a2):
    return a1.response == a2.response and \
           a1.username == a2.username

def create_authRequestOut_t():
    tmp = authRequestOut_t()
    tmp.challenge = "challenge"   # char *
    return tmp

def test_authRequestOut_t(a1, a2):
    return a1.challenge == a2.challenge

def create_bytesBuf_t():
    tmp = bytesBuf_t()
    tmp.setBuf("buf", len("buf"))
    return tmp

def init_bytesBuf_t(tmp):
    tmp.setBuf("buf", len("buf"))

def test_bytesBuf_t(b1, b2):
    return b1.getBuf() == b2.getBuf()

def create_chkObjPermAndStat_t():
    tmp = chkObjPermAndStat_t()
    tmp.objPath = "objPath"             # char []
    tmp.permission = "permission"       # char []
    tmp.flags = 12                      # int
    tmp.status = 12                     # int
    init_keyValPair_t(tmp.condInput)    # keyValPair_t
    return tmp

def test_chkObjPermAndStat_t(c1, c2):
    return c1.objPath == c2.objPath and \
           c1.permission == c2.permission and \
           c1.flags == c2.flags and \
           c1.status == c2.status and \
           test_keyValPair_t(c1.condInput, c2.condInput)

def create_collEnt_t():
    tmp = collEnt_t()
    tmp.objType = UNKNOWN_OBJ_T         # objType_t
    tmp.replNum = 12                    # int
    tmp.replStatus = 12                 # int
    tmp.dataMode = 12                   # int
    tmp.dataSize = 12                   # int
    tmp.collName = "collName"           # char *
    tmp.dataName = "dataName"           # char *
    tmp.dataId = "dataId"               # char *
    tmp.createTime = "createTime"       # char *
    tmp.modifyTime = "modifyTime"       # char *
    tmp.chksum = "chksum"               # char *
    tmp.resource = "resource"           # char *
    tmp.rescGrp = "rescGrp"             # char *
    tmp.phyPath = "phyPath"             # char *
    tmp.ownerName = "ownerName"         # char *
    init_specColl_t(tmp.specColl)      # specColl_t
    return tmp

def test_collEnt_t(c1, c2):
    return c1.objType == c2.objType and \
           c1.replNum == c2.replNum and \
           c1.replStatus == c2.replStatus and \
           c1.dataMode == c2.dataMode and \
           c1.dataSize == c2.dataSize and \
           c1.collName == c2.collName and \
           c1.dataName == c2.dataName and \
           c1.dataId == c2.dataId and \
           c1.createTime == c2.createTime and \
           c1.modifyTime == c2.modifyTime and \
           c1.chksum == c2.chksum and \
           c1.resource == c2.resource and \
           c1.rescGrp == c2.rescGrp and \
           c1.phyPath == c2.phyPath and \
           c1.ownerName == c2.ownerName and \
           test_specColl_t(c1.specColl, c2.specColl)

def create_collHandle_t():
    tmp = collHandle_t()
    tmp.state = COLL_CLOSED                         # collState_t
    tmp.inuseFlag = 12                              # int
    tmp.flags = 12                                  # int
    tmp.rowInx = 12                                 # int
    tmp.rodsObjStat = create_rodsObjStat_t()        # rodsObjStat_t *
    init_queryHandle_t(tmp.queryHandle)             # queryHandle_t
    init_genQueryInp_t(tmp.genQueryInp)             # genQueryInp_t
    init_dataObjInp_t(tmp.dataObjInp)               # dataObjInp_t
    init_dataObjSqlResult_t(tmp.dataObjSqlResult)   # dataObjSqlResult_t
    init_collSqlResult_t(tmp.collSqlResult)         # collSqlResult_t
    tmp.linkedObjPath = "linkedObjPath"             # char []
    tmp.prevdataId = "prevdataId"                   # char []
    return tmp

def test_collHandle_t(c1, c2):
    return c1.state == c2.state and \
           c1.inuseFlag == c2.inuseFlag and \
           c1.flags == c2.flags and \
           c1.rowInx == c2.rowInx and \
           test_rodsObjStat_t(c1.rodsObjStat, c2.rodsObjStat) and \
           test_queryHandle_t(c1.queryHandle, c2.queryHandle) and \
           test_genQueryInp_t(c1.genQueryInp, c2.genQueryInp) and \
           test_dataObjInp_t(c1.dataObjInp, c2.dataObjInp) and \
           test_dataObjSqlResult_t(c1.dataObjSqlResult, c2.dataObjSqlResult) and \
           test_collSqlResult_t(c1.collSqlResult, c2.collSqlResult) and \
           c1.linkedObjPath == c2.linkedObjPath and \
           c1.prevdataId == c2.prevdataId

def create_collInp_t():
    tmp = collInp_t()
    tmp.collName = "collName"           # char []
    tmp.flags = 12                      # int
    tmp.oprType = 12                    # int
    init_keyValPair_t(tmp.condInput)    # keyValPair_t
    return tmp

def test_collInp_t(c1, c2):
    return c1.collName == c2.collName and \
           c1.flags == c2.flags and \
           c1.oprType == c2.oprType and \
           test_keyValPair_t(c1.condInput, c2.condInput)

def create_collSqlResult_t():
    tmp = collSqlResult_t()
    tmp.rowCnt = 12                         # int
    tmp.attriCnt = 12                       # int
    tmp.continueInx = 12                    # int
    tmp.totalRowCount = 12                  # int
    init_sqlResult_t(tmp.collName)          # sqlResult_t
    init_sqlResult_t(tmp.collType)          # sqlResult_t
    init_sqlResult_t(tmp.collInfo1)         # sqlResult_t
    init_sqlResult_t(tmp.collInfo2)         # sqlResult_t
    init_sqlResult_t(tmp.collOwner)         # sqlResult_t
    init_sqlResult_t(tmp.collCreateTime)    # sqlResult_t
    init_sqlResult_t(tmp.collModifyTime)    # sqlResult_t
    return tmp

def init_collSqlResult_t(tmp):
    tmp.rowCnt = 12                         # int
    tmp.attriCnt = 12                       # int
    tmp.continueInx = 12                    # int
    tmp.totalRowCount = 12                  # int
    init_sqlResult_t(tmp.collName)          # sqlResult_t
    init_sqlResult_t(tmp.collType)          # sqlResult_t
    init_sqlResult_t(tmp.collInfo1)         # sqlResult_t
    init_sqlResult_t(tmp.collInfo2)         # sqlResult_t
    init_sqlResult_t(tmp.collOwner)         # sqlResult_t
    init_sqlResult_t(tmp.collCreateTime)    # sqlResult_t
    init_sqlResult_t(tmp.collModifyTime)    # sqlResult_t

def test_collSqlResult_t(c1, c2):
    return c1.rowCnt == c2.rowCnt and \
           c1.attriCnt == c2.attriCnt and \
           c1.continueInx == c2.continueInx and \
           c1.totalRowCount == c2.totalRowCount and \
           test_sqlResult_t(c1.collName, c2.collName) and \
           test_sqlResult_t(c1.collType, c2.collType) and \
           test_sqlResult_t(c1.collInfo1, c2.collInfo1) and \
           test_sqlResult_t(c1.collInfo2, c2.collInfo2) and \
           test_sqlResult_t(c1.collOwner, c2.collOwner) and \
           test_sqlResult_t(c1.collCreateTime, c2.collCreateTime) and \
           test_sqlResult_t(c1.collModifyTime, c2.collModifyTime)

def create_dataCopyInp_t():
    tmp = dataCopyInp_t()
    init_dataOprInp_t(tmp.dataOprInp)       # dataOprInp_t
    init_portalOprOut_t(tmp.portalOprOut)   # portalOprOut_t
    return tmp

def test_dataCopyInp_t(d1, d2):
    return test_dataOprInp_t(d1.dataOprInp, d2.dataOprInp) and \
           test_portalOprOut_t(d1.portalOprOut, d2.portalOprOut)

def create_dataObjCopyInp_t():
    tmp = dataObjCopyInp_t()
    init_dataObjInp_t(tmp.srcDataObjInp)    # dataObjInp_t
    init_dataObjInp_t(tmp.destDataObjInp)   # dataObjInp_t
    return tmp

def test_dataObjCopyInp_t(d1, d2):
    return test_dataObjInp_t(d1.srcDataObjInp, d2.srcDataObjInp) and \
           test_dataObjInp_t(d1.destDataObjInp, d2.destDataObjInp)

def create_dataObjInfo_t():
    tmp = dataObjInfo_t()
    tmp.objPath = "objPath"                     # char []
    tmp.rescName = "rescName"                   # char []
    tmp.rescGroupName = "rescGroupName"         # char []
    tmp.dataType = "dataType"                   # char []
    tmp.dataSize = 12                           # rodsLong_t
    tmp.chksum = "chksum"                       # char []
    tmp.version = "version"                     # char []
    tmp.filePath = "filePath"                   # char []
    tmp.rescInfo = create_rescInfo_t()          # rescinfo_t *
    tmp.dataOwnerName = "dataOwnerName"         # char []
    tmp.dataOwnerZone = "dataOwnerZone"         # char []
    tmp.replNum = 12                            # int
    tmp.replStatus = 12                         # int
    tmp.statusString = "statusString"           # char []
    tmp.dataId = 12                             # rodsLong_t
    tmp.collId = 12                             # rodsLong_t
    tmp.dataMapId = 12                          # int
    tmp.flags = 12                              # int
    tmp.dataComments = "dataComments"           # char []
    tmp.dataMode = "dataMode"                   # char []
    tmp.dataExpiry = "dataExpiry"               # char []
    tmp.dataCreate = "dataCreate"               # char []
    tmp.dataModify = "dataModify"               # char []
    tmp.dataAccess = "dataAccess"               # char []
    tmp.dataAccessInx = 12                      # int
    tmp.writeFlag = 12                          # int
    tmp.destRescName = "destRescName"           # char []
    tmp.backupRescName = "backupRescName"       # char []
    tmp.subPath = "subPath"                     # char []
    tmp.specColl = create_specColl_t()          # specColl_t *
    tmp.regUid = 12                             # int
    tmp.otherFlags = 12                         # int
    init_keyValPair_t(tmp.condInput)            # keyValPair_t
    tmp.next = None                             # dataObjInfo *
    return tmp

def test_dataObjInfo_t(d1, d2):
    next = False
    if d1.next:
        next = test_dataObjInfo_t(d1.next, d2.next)
    else:
        next = d2.next == None
        
    return d1.objPath == d2.objPath and \
           d1.rescName == d2.rescName and \
           d1.rescGroupName == d2.rescGroupName and \
           d1.dataType == d2.dataType and \
           d1.dataSize == d2.dataSize and \
           d1.chksum == d2.chksum and \
           d1.version == d2.version and \
           d1.filePath == d2.filePath and \
           test_rescInfo_t(d1.rescInfo, d2.rescInfo) and \
           d1.dataOwnerName == d2.dataOwnerName and \
           d1.dataOwnerZone == d2.dataOwnerZone and \
           d1.replNum == d2.replNum and \
           d1.replStatus == d2.replStatus and \
           d1.statusString == d2.statusString and \
           d1.dataId == d2.dataId and \
           d1.collId == d2.collId and \
           d1.dataMapId == d2.dataMapId and \
           d1.flags == d2.flags and \
           d1.dataComments == d2.dataComments and \
           d1.dataMode == d2.dataMode and \
           d1.dataExpiry == d2.dataExpiry and \
           d1.dataCreate == d2.dataCreate and \
           d1.dataModify == d2.dataModify and \
           d1.dataAccess == d2.dataAccess and \
           d1.dataAccessInx == d2.dataAccessInx and \
           d1.writeFlag == d2.writeFlag and \
           d1.destRescName == d2.destRescName and \
           d1.backupRescName == d2.backupRescName and \
           d1.subPath == d2.subPath and \
           test_specColl_t(d1.specColl, d2.specColl) and \
           d1.regUid == d2.regUid and \
           d1.otherFlags == d2.otherFlags and \
           test_keyValPair_t(d1.condInput, d2.condInput) and \
           next

def create_dataObjInp_t():
    tmp = dataObjInp_t()
    tmp.objPath = "objPath"             # char[]
    tmp.createMode = 12                 # int
    tmp.openFlags = 12                  # int
    tmp.offset = 12                     # rodsLong_t
    tmp.dataSize = 12                   # rodsLong_t
    tmp.numThreads = 12                 # int
    tmp.oprType = 12                    # int
    tmp.specColl = create_specColl_t()  # specColl *
    init_keyValPair_t(tmp.condInput)    # keyValPair_t
    return tmp

def init_dataObjInp_t(tmp):
    tmp.objPath = "objPath"             # char[]
    tmp.createMode = 12                 # int
    tmp.openFlags = 12                  # int
    tmp.offset = 12                     # rodsLong_t
    tmp.dataSize = 12                   # rodsLong_t
    tmp.numThreads = 12                 # int
    tmp.oprType = 12                    # int
    tmp.specColl = create_specColl_t()  # specColl *
    init_keyValPair_t(tmp.condInput)    # keyValPair_t

def test_dataObjInp_t(d1, d2):
    return d1.objPath == d2.objPath and \
           d1.createMode == d2.createMode and \
           d1.openFlags == d2.openFlags and \
           d1.offset == d2.offset and \
           d1.dataSize == d2.dataSize and \
           d1.numThreads == d2.numThreads and \
           d1.oprType == d2.oprType and \
           test_specColl_t(d1.specColl, d2.specColl) and \
           test_keyValPair_t(d1.condInput, d2.condInput)

def create_dataObjSqlResult_t():
    tmp = dataObjSqlResult_t()
    tmp.rowCnt = 12                        # int
    tmp.attriCnt = 12                      # int
    tmp.continueInx = 12                   # int
    tmp.totalRowCount = 12                 # int
    init_sqlResult_t(tmp.collName)         # sqlResult_t
    init_sqlResult_t(tmp.dataName)         # sqlResult_t
    init_sqlResult_t(tmp.dataMode)         # sqlResult_t
    init_sqlResult_t(tmp.dataSize)         # sqlResult_t
    init_sqlResult_t(tmp.createTime)       # sqlResult_t
    init_sqlResult_t(tmp.modifyTime)       # sqlResult_t
    init_sqlResult_t(tmp.chksum)           # sqlResult_t
    init_sqlResult_t(tmp.replStatus)       # sqlResult_t
    init_sqlResult_t(tmp.dataId)           # sqlResult_t
    init_sqlResult_t(tmp.resource)         # sqlResult_t
    init_sqlResult_t(tmp.phyPath)          # sqlResult_t
    init_sqlResult_t(tmp.ownerName)        # sqlResult_t
    init_sqlResult_t(tmp.replNum)          # sqlResult_t
    init_sqlResult_t(tmp.rescGrp)          # sqlResult_t
    init_sqlResult_t(tmp.dataType)         # sqlResult_t
    return tmp

def init_dataObjSqlResult_t(tmp):
    tmp.rowCnt = 12                        # int
    tmp.attriCnt = 12                      # int
    tmp.continueInx = 12                   # int
    tmp.totalRowCount = 12                 # int
    init_sqlResult_t(tmp.collName)         # sqlResult_t
    init_sqlResult_t(tmp.dataName)         # sqlResult_t
    init_sqlResult_t(tmp.dataMode)         # sqlResult_t
    init_sqlResult_t(tmp.dataSize)         # sqlResult_t
    init_sqlResult_t(tmp.createTime)       # sqlResult_t
    init_sqlResult_t(tmp.modifyTime)       # sqlResult_t
    init_sqlResult_t(tmp.chksum)           # sqlResult_t
    init_sqlResult_t(tmp.replStatus)       # sqlResult_t
    init_sqlResult_t(tmp.dataId)           # sqlResult_t
    init_sqlResult_t(tmp.resource)         # sqlResult_t
    init_sqlResult_t(tmp.phyPath)          # sqlResult_t
    init_sqlResult_t(tmp.ownerName)        # sqlResult_t
    init_sqlResult_t(tmp.replNum)          # sqlResult_t
    init_sqlResult_t(tmp.rescGrp)          # sqlResult_t
    init_sqlResult_t(tmp.dataType)         # sqlResult_t

def test_dataObjSqlResult_t(d1, d2):
    return d1.rowCnt == d2.rowCnt and \
           d1.attriCnt == d2.attriCnt and \
           d1.continueInx == d2.continueInx and \
           d1.totalRowCount == d2.totalRowCount and \
           test_sqlResult_t(d1.collName, d2.collName) and \
           test_sqlResult_t(d1.dataName, d2.dataName) and \
           test_sqlResult_t(d1.dataMode, d2.dataMode) and \
           test_sqlResult_t(d1.dataSize, d2.dataSize) and \
           test_sqlResult_t(d1.createTime, d2.createTime) and \
           test_sqlResult_t(d1.modifyTime, d2.modifyTime) and \
           test_sqlResult_t(d1.chksum, d2.chksum) and \
           test_sqlResult_t(d1.replStatus, d2.replStatus) and \
           test_sqlResult_t(d1.dataId, d2.dataId) and \
           test_sqlResult_t(d1.resource, d2.resource) and \
           test_sqlResult_t(d1.phyPath, d2.phyPath) and \
           test_sqlResult_t(d1.ownerName, d2.ownerName) and \
           test_sqlResult_t(d1.replNum, d2.replNum) and \
           test_sqlResult_t(d1.rescGrp, d2.rescGrp) and \
           test_sqlResult_t(d1.dataType, d2.dataType)

def create_dataOprInp_t():
    tmp = dataOprInp_t()
    tmp.oprType = 12                    # int
    tmp.numThreads = 12                 # int
    tmp.srcL3descInx = 12               # int
    tmp.destL3descInx = 12              # int
    tmp.srcRescTypeInx = 12             # int
    tmp.destRescTypeInx = 12            # int
    tmp.offset = 12                     # rodsLong_t
    tmp.dataSize = 12                   # rodsLong_t
    init_keyValPair_t(tmp.condInput)    # keyValPair
    return tmp

def test_dataOprInp_t(t1, t2):
    return t1.oprType == t2.oprType and \
           t1.numThreads == t2.numThreads and \
           t1.srcL3descInx == t2.srcL3descInx and \
           t1.destL3descInx == t2.destL3descInx and \
           t1.srcRescTypeInx == t2.srcRescTypeInx and \
           t1.destRescTypeInx == t2.destRescTypeInx and \
           t1.offset == t2.offset and \
           t1.dataSize == t2.dataSize and \
           test_keyValPair_t(t1.condInput, t2.condInput)

def init_dataOprInp_t(t1):
    t1.oprType = 12                    # int
    t1.numThreads = 12                 # int
    t1.srcL3descInx = 12               # int
    t1.destL3descInx = 12              # int
    t1.srcRescTypeInx = 12             # int
    t1.destRescTypeInx = 12            # int
    t1.offset = 12                     # rodsLong_t
    t1.dataSize = 12                   # rodsLong_t
    init_keyValPair_t(t1.condInput)    # keyValPair

def create_execCmd_t():
    tmp = execCmd_t()
    tmp.cmd = "cmd"                         # char []
    tmp.cmdArgv = "cmdArgv"                 # char []
    tmp.execAddr = "execAddr"               # char []
    tmp.hintPath = "hintPath"               # char []
    tmp.addPathToArgv = 12                  # int
    tmp.dummy = 12                          # int
    init_keyValPair_t(tmp.condInput)        # keyValPair_t
    return tmp

def test_execCmd_t(e1, e2):
    return e1.cmd == e2.cmd and \
           e1.cmdArgv == e2.cmdArgv and \
           e1.execAddr == e2.execAddr and \
           e1.hintPath == e2.hintPath and \
           e1.addPathToArgv == e2.addPathToArgv and \
           e1.dummy == e2.dummy and \
           test_keyValPair_t(e1.condInput, e2.condInput)

def create_execCmdOut_t():
    tmp = execCmdOut_t()
    init_bytesBuf_t(tmp.stdoutBuf)      # bytesBuf_t
    init_bytesBuf_t(tmp.stderrBuf)      # bytesBuf_t
    tmp.status = 12                     # int
    return tmp

def test_execCmdOut_t(e1, e2):
    return test_bytesBuf_t(e1.stdoutBuf, e2.stdoutBuf) and \
           test_bytesBuf_t(e1.stderrBuf, e2.stderrBuf) and \
           e1.status == e2.status

def create_execMyRuleInp_t():
    tmp = execMyRuleInp_t()
    tmp.myRule = "myRule"                           # char []
    init_rodsHostAddr_t(tmp.addr)                   # rodsHostAddr_t
    init_keyValPair_t(tmp.condInput)                # keyValPair_t
    tmp.outParamDesc = "outParamDesc"               # char []
    tmp.inpParamArray = create_msParamArray_t()     # msParamArray_t *
    return tmp

def test_execMyRuleInp_t(e1, e2):
    return e1.myRule == e2.myRule and \
           test_rodsHostAddr_t(e1.addr, e2.addr) and \
           test_keyValPair_t(e1.condInput, e2.condInput) and \
           e1.outParamDesc == e2.outParamDesc and \
           test_msParamArray_t(e1.inpParamArray, e2.inpParamArray)

def create_fileChmodInp_t():
    tmp = fileChmodInp_t()
    tmp.fileType = UNIX_FILE_TYPE       # fileDriverType_t
    init_rodsHostAddr_t(tmp.addr)       # rodsHostAddr_t
    tmp.fileName = "fileName"           # char []
    tmp.mode = 12                       # int
    return tmp

def test_fileChmodInp_t(f1, f2):
    return f1.fileType == f2.fileType and \
           test_rodsHostAddr_t(f1.addr, f2.addr) and \
           f1.fileName == f2.fileName and \
           f1.mode == f2.mode

def create_fileChksumInp_t():
    tmp = fileChksumInp_t()
    tmp.fileType = UNIX_FILE_TYPE       # fileDriverType_t
    init_rodsHostAddr_t(tmp.addr,)      # rodsHostAddr_t
    tmp.fileName = "fileName"           # char []
    tmp.flag = 12                       # int
    return tmp

def test_fileChksumInp_t(f1, f2):
    return f1.fileType == f2.fileType and \
           test_rodsHostAddr_t(f1.addr, f2.addr) and \
           f1.fileName == f2.fileName and \
           f1.flag == f2.flag

def create_fileCloseInp_t():
    tmp = fileCloseInp_t()
    tmp.fileInx = 12                       # int
    return tmp

def test_fileCloseInp_t(f1, f2):
    return f1.fileInx == f2.fileInx

def create_fileClosedirInp_t():
    tmp = fileClosedirInp_t()
    tmp.fileInx = 12                       # int
    return tmp

def test_fileClosedirInp_t(f1, f2):
    return f1.fileInx == f2.fileInx

def create_fileFstatInp_t():
    tmp = fileFstatInp_t()
    tmp.fileInx = 12                       # int
    return tmp

def test_fileFstatInp_t(f1, f2):
    return f1.fileInx == f2.fileInx

def create_fileFsyncInp_t():
    tmp = fileFsyncInp_t()
    tmp.fileInx = 12                       # int
    return tmp

def test_fileFsyncInp_t(f1, f2):
    return f1.fileInx == f2.fileInx

def create_fileGetFsFreeSpaceInp_t():
    tmp = fileGetFsFreeSpaceInp_t()
    tmp.fileType = UNIX_FILE_TYPE       # fileDriverType_t
    init_rodsHostAddr_t(tmp.addr)       # rodsHostAddr_t
    tmp.fileName = "fileName"           # char []
    tmp.flag = 12                       # int
    return tmp

def test_fileGetFsFreeSpaceInp_t(f1, f2):
    return f1.fileType == f2.fileType and \
           test_rodsHostAddr_t(f1.addr, f2.addr) and \
           f1.fileName == f2.fileName and \
           f1.flag == f2.flag

def create_fileGetFsFreeSpaceOut_t():
    tmp = fileGetFsFreeSpaceOut_t()
    tmp.size = 12                       # int
    return tmp

def test_fileGetFsFreeSpaceOut_t(f1, f2):
    return f1.size == f2.size

def create_fileLseekInp_t():
    tmp = fileLseekInp_t()
    tmp.fileInx = 12                # int
    tmp.offset = 12                 # rodsLong_t
    tmp.whence = 12                 # int
    return tmp

def test_fileLseekInp_t(f1, f2):
    return f1.fileInx == f2.fileInx and \
           f1.offset == f2.offset and \
           f1.whence == f2.whence

def create_fileLseekOut_t():
    tmp = fileLseekOut_t()
    tmp.offset = 12                 # rodsLong_t
    return tmp

def test_fileLseekOut_t(f1, f2):
    return f1.offset == f2.offset

def create_fileMkdirInp_t():
    tmp = fileMkdirInp_t()
    tmp.fileType = UNIX_FILE_TYPE       # fileDriverType_t
    init_rodsHostAddr_t(tmp.addr)       # rodsHostAddr_t
    tmp.dirName = "dirName"             # char []
    tmp.mode = 12                       # int
    init_keyValPair_t(tmp.condInput)    # keyValPair_t
    return tmp

def test_fileMkdirInp_t(f1, f2):
    return f1.fileType == f2.fileType and \
           test_rodsHostAddr_t(f1.addr, f2.addr) and \
           f1.dirName == f2.dirName and \
           f1.mode == f2.mode and \
           test_keyValPair_t(f1.condInput, f2.condInput)

def create_fileOpenInp_t():
    tmp = fileOpenInp_t()
    tmp.fileType = UNIX_FILE_TYPE       # fileDriverType_t
    tmp.otherFlags = 12                 # int
    init_rodsHostAddr_t(tmp.addr)       # rodsHostAddr_t
    tmp.fileName = "fileName"           # char []
    tmp.flags = 12                      # int
    tmp.mode = 12                       # int
    tmp.dataSize = 12                   # rodsLong_t
    init_keyValPair_t(tmp.condInput)    # keyValPair_t
    return tmp

def test_fileOpenInp_t(f1, f2):
    return f1.fileType == f2.fileType and \
           f1.otherFlags == f2.otherFlags and \
           test_rodsHostAddr_t(f1.addr, f2.addr) and \
           f1.fileName == f2.fileName and \
           f1.flags == f2.flags and \
           f1.mode == f2.mode and \
           f1.dataSize == f2.dataSize and \
           test_keyValPair_t(f1.condInput, f2.condInput)

def create_fileOpendirInp_t():
    tmp = fileOpendirInp_t()
    tmp.fileType = UNIX_FILE_TYPE    # fileDriverType_t
    init_rodsHostAddr_t(tmp.addr)    # rodsHostAddr_t
    tmp.dirName = "dirName"          # char []
    return tmp

def test_fileOpendirInp_t(f1, f2):
    return f1.fileType == f2.fileType and \
           test_rodsHostAddr_t(f1.addr, f2.addr) and \
           f1.dirName == f2.dirName

def create_fileReadInp_t():
    tmp = fileReadInp_t()
    tmp.fileInx = 12            # int
    tmp.len = 12                # int
    return tmp

def test_fileReadInp_t(f1, f2):
    return f1.fileInx == f2.fileInx and \
           f1.len == f2.len

def create_fileRenameInp_t():
    tmp = fileRenameInp_t()
    tmp.fileType = UNIX_FILE_TYPE    # fileDriverType_t
    init_rodsHostAddr_t(tmp.addr)    # rodsHostAddr_t
    tmp.oldFileName = "oldFileName"  # char []
    tmp.newFileName = "newFileName"  # char []
    return tmp

def test_fileRenameInp_t(f1, f2):
    return f1.fileType == f2.fileType and \
           test_rodsHostAddr_t(f1.addr, f2.addr) and \
           f1.oldFileName == f2.oldFileName and \
           f1.newFileName == f2.newFileName

def create_fileRestartInfo_t():
    tmp = fileRestartInfo_t()
    tmp.fileName = "fileName"           # char []
    tmp.objPath = "objPath"             # char []
    tmp.numSeg = 12                     # int
    tmp.status = FILE_NOT_RESTART       # fileRestartStatus_t
    tmp.fileSize = 12                   # rodsLong_t
    #tmp.dataSeg                        # dataSeg_t [] 
    return tmp

def init_fileRestartInfo_t(tmp):
    tmp.fileName = "fileName"           # char []
    tmp.objPath = "objPath"             # char []
    tmp.numSeg = 12                     # int
    tmp.status = FILE_NOT_RESTART       # fileRestartStatus_t
    tmp.fileSize = 12                   # rodsLong_t
    #tmp.dataSeg                        # dataSeg_t [] 

def test_fileRestartInfo_t(f1, f2):
    return f1.fileName == f2.fileName and \
           f1.objPath == f2.objPath and \
           f1.numSeg == f2.numSeg and \
           f1.status == f2.status and \
           f1.fileSize == f2.fileSize
           

def create_fileRestart_t():
    tmp = fileRestart_t()
    tmp.flags = FILE_RESTART_OFF        # fileRestartFlag_t
    tmp.writtenSinceUpdated = 12        # rodsLong_t
    tmp.infoFile = "infoFile"           # char []
    init_fileRestartInfo_t(tmp.info)    # fileRestartInfo_t
    return tmp

def init_fileRestart_t(tmp):
    tmp.flags = FILE_RESTART_OFF        # fileRestartFlag_t
    tmp.writtenSinceUpdated = 12        # rodsLong_t
    tmp.infoFile = "infoFile"           # char []
    init_fileRestartInfo_t(tmp.info)    # fileRestartInfo_t

def test_fileRestart_t(f1, f2):
    return f1.flags == f2.flags and \
           f1.writtenSinceUpdated == f2.writtenSinceUpdated and \
           f1.infoFile == f2.infoFile and \
           test_fileRestartInfo_t(f1.info, f2.info)

def create_fileRmdirInp_t():
    tmp = fileRmdirInp_t()
    tmp.fileType = UNIX_FILE_TYPE    # fileDriverType_t
    tmp.flags = 12                   # int
    init_rodsHostAddr_t(tmp.addr)    # rodsHostAddr_t
    tmp.dirName = "dirName"          # char []
    return tmp

def test_fileRmdirInp_t(f1, f2):
    return f1.fileType == f2.fileType and \
           f1.flags == f2.flags and \
           test_rodsHostAddr_t(f1.addr, f2.addr) and \
           f1.dirName == f2.dirName

def create_fileStageInp_t():
    tmp = fileStageInp_t()
    tmp.fileType = UNIX_FILE_TYPE    # fileDriverType_t
    init_rodsHostAddr_t(tmp.addr)    # rodsHostAddr_t
    tmp.fileName = "fileName"        # char []
    tmp.flag = 12                       # int
    return tmp

def test_fileStageInp_t(f1, f2):
    return f1.fileType == f2.fileType and \
           test_rodsHostAddr_t(f1.addr, f2.addr) and \
           f1.fileName == f2.fileName and \
           f1.flag == f2.flag

def create_fileStatInp_t():
    tmp = fileStatInp_t()
    tmp.fileType = UNIX_FILE_TYPE    # fileDriverType_t
    init_rodsHostAddr_t(tmp.addr)    # rodsHostAddr_t
    tmp.fileName = "fileName"        # char []
    return tmp

def test_fileStatInp_t(f1, f2):
    return f1.fileType == f2.fileType and \
           test_rodsHostAddr_t(f1.addr, f2.addr) and \
           f1.fileName == f2.fileName

def create_fileUnlinkInp_t():
    tmp = fileUnlinkInp_t()
    tmp.fileType = UNIX_FILE_TYPE    # fileDriverType_t
    init_rodsHostAddr_t(tmp.addr)    # rodsHostAddr_t
    tmp.fileName = "fileName"        # char []
    return tmp

def test_fileUnlinkInp_t(f1, f2):
    return f1.fileType == f2.fileType and \
           test_rodsHostAddr_t(f1.addr, f2.addr) and \
           f1.fileName == f2.fileName

def create_fileWriteInp_t():
    tmp = fileWriteInp_t()
    tmp.fileInx = 12            # int
    tmp.len = 12                # int
    return tmp

def test_fileWriteInp_t(f1, f2):
    return f1.fileInx == f2.fileInx and \
           f1.len == f2.len

def create_generalAdminInp_t():
    tmp = generalAdminInp_t()
    tmp.arg0 = "arg0"             # char *
    tmp.arg1 = "arg1"             # char *
    tmp.arg2 = "arg2"             # char *
    tmp.arg3 = "arg3"             # char *
    tmp.arg4 = "arg4"             # char *
    tmp.arg5 = "arg5"             # char *
    tmp.arg6 = "arg6"             # char *
    tmp.arg7 = "arg7"             # char *
    tmp.arg8 = "arg8"             # char *
    tmp.arg9 = "arg9"             # char *
    return tmp

def test_generalAdminInp_t(g1, g2):
    return g1.arg0 == g2.arg0 and \
           g1.arg1 == g2.arg1 and \
           g1.arg2 == g2.arg2 and \
           g1.arg3 == g2.arg3 and \
           g1.arg4 == g2.arg4 and \
           g1.arg5 == g2.arg5 and \
           g1.arg6 == g2.arg6 and \
           g1.arg7 == g2.arg7 and \
           g1.arg8 == g2.arg8 and \
           g1.arg9 == g2.arg9

def create_generalUpdateInp_t():
    tmp = generalUpdateInp_t()
    tmp.type = 12                       # int
    init_inxValPair_t(tmp.values)       # inxValPair_t
    return tmp

def test_generalUpdateInp_t(g1, g2):
    return g1.type == g2.type and \
           test_inxValPair_t(g1.values, g2.values)

def create_genQueryInp_t():
    tmp = genQueryInp_t()
    tmp.maxRows = 12                         # int
    tmp.continueInx = 12                     # int
    tmp.rowOffset = 12                       # int
    tmp.options = 12                         # int
    tmp.setCondInput(create_keyValPair_t())  # keyValPair_t
    tmp.setSelectInp(create_inxIvalPair_t()) # inxIvalPair_t
    tmp.setSqlCondInp(create_inxValPair_t()) # inxValPair_t
    return tmp

def init_genQueryInp_t(tmp):
    tmp.maxRows = 12                         # int
    tmp.continueInx = 12                     # int
    tmp.rowOffset = 12                       # int
    tmp.options = 12                         # int
    tmp.setCondInput(create_keyValPair_t())  # keyValPair_t
    tmp.setSelectInp(create_inxIvalPair_t()) # inxIvalPair_t
    tmp.setSqlCondInp(create_inxValPair_t()) # inxValPair_t

def test_genQueryInp_t(g1, g2):
    return g1.maxRows == g2.maxRows and \
           g1.continueInx == g2.continueInx and \
           g1.rowOffset == g2.rowOffset and \
           g1.options == g2.options and \
           test_keyValPair_t(g1.getCondInput(), g2.getCondInput()) and \
           test_inxIvalPair_t(g1.getSelectInp(), g2.getSelectInp()) and \
           test_inxValPair_t(g1.getSqlCondInp(), g2.getSqlCondInp())

def create_genQueryOut_t():
    tmp = genQueryOut_t()
    tmp.rowCnt = 12                     # int
    tmp.attriCnt = 12                   # int
    tmp.continueInx = 12                # int
    tmp.totalRowCount = 12              # int
    init_sqlResult_t(tmp.sqlResult)     # sqlResult_t []
    return tmp

def test_genQueryOut_t(g1, g2):
    return g1.rowCnt == g2.rowCnt and \
           g1.attriCnt == g2.attriCnt and \
           g1.continueInx == g2.continueInx and \
           g1.totalRowCount == g2.totalRowCount and \
           test_sqlResult_t(g1.sqlResult, g2.sqlResult)

def create_getTempPasswordOut_t():
    tmp = getTempPasswordOut_t()
    tmp.stringToHashWith = "stringToHashWith"         # char []
    return tmp

def test_getTempPasswordOut_t(g1, g2):
    return g1.stringToHashWith == g2.stringToHashWith

def create_getXmsgTicketInp_t():
    tmp = getXmsgTicketInp_t()
    tmp.expireTime = 12     # unsigned int
    tmp.flag = 12           # unsigned int
    return tmp

def test_getXmsgTicketInp_t(g1, g2):
    return g1.expireTime == g2.expireTime and \
           g1.flag == g2.flag

def create_gsiAuthRequestOut_t():
    tmp = gsiAuthRequestOut_t()
    tmp.serverDN = "serverDN"      # char *
    return tmp

def test_gsiAuthRequestOut_t(g1, g2):
    return g1.serverDN == g2.serverDN

def create_inxIvalPair_t():
    tmp = inxIvalPair_t()
    tmp.init([1, 2, 3],
             [12, 13, 14],
            3)
    return tmp

def init_inxIvalPair_t(tmp):
    tmp.init([1, 2, 3],
             [12, 13, 14],
            3)

def test_inxIvalPair_t(k1, k2):
    if k1.getLen() != k2.getLen():
        return False
    if k1.getInx() != k2.getInx():
        return False
    if k1.getValue() != k2.getValue():
        return False
    return True

def create_inxValPair_t():
    tmp = inxValPair_t()
    tmp.init([1, 2, 3],
             ["1", "2", "3"],
            3)
    return tmp

def init_inxValPair_t(tmp):
    tmp.init([1, 2, 3],
             ["1", "2", "3"],
            3)

def test_inxValPair_t(k1, k2):
    if k1.getLen() != k2.getLen():
        return False
    if k1.getInx() != k2.getInx():
        return False
    if k1.getValue() != k2.getValue():
        return False
    return True 

def create_keyValPair_t():
    tmp = keyValPair_t()
    tmp.init(["first", "second", "third"],
             ["1", "2", "3"],
            3)
    return tmp
   
def init_keyValPair_t(keyValPair1):
    keyValPair1.init(["first", "second", "third"],
                     ["1", "2", "3"],
                     3)

def test_keyValPair_t(k1, k2):
    if k1.getLen() != k2.getLen():
        return False
    if k1.getKeyWords() != k2.getKeyWords():
        return False
    if k1.getValues() != k2.getValues():
        return False
    return True 

def create_MD5_CTX():
    tmp = MD5_CTX()
    tmp.set_MD5_CTX_state(0, 1)         # UINT4 state[4];
    tmp.set_MD5_CTX_state(1, 2)
    tmp.set_MD5_CTX_state(2, 3)
    tmp.set_MD5_CTX_state(3, 4)
    tmp.set_MD5_CTX_count(0, 1)         # UINT4 count[2];
    tmp.set_MD5_CTX_count(1, 2)
    tmp.set_MD5_CTX_buffer("buffer")    # unsigned char [64]
    return tmp

def test_MD5_CTX(m1, m2):
    return m1.get_MD5_CTX_state(0) == m2.get_MD5_CTX_state(0) and \
           m1.get_MD5_CTX_state(1) == m2.get_MD5_CTX_state(1) and \
           m1.get_MD5_CTX_state(2) == m2.get_MD5_CTX_state(2) and \
           m1.get_MD5_CTX_state(3) == m2.get_MD5_CTX_state(3) and \
           m1.get_MD5_CTX_count(0) == m2.get_MD5_CTX_count(0) and \
           m1.get_MD5_CTX_count(1) == m2.get_MD5_CTX_count(1) and \
           m1.get_MD5_CTX_buffer() == m2.get_MD5_CTX_buffer()

def create_miscSvrInfo_t():
    tmp = miscSvrInfo_t()
    tmp.serverType = 12             # int
    tmp.serverBootTime = 12         # unsigned int
    tmp.relVersion = "relVersion"   # char []
    tmp.apiVersion = "apiVersion"   # char []
    tmp.rodsZone = "rodsZone"       # char []
    return tmp

def test_miscSvrInfo_t(m1, m2):
    return m1.serverType == m2.serverType and \
           m1.serverBootTime == m2.serverBootTime and \
           m1.relVersion == m2.relVersion and \
           m1.apiVersion == m2.apiVersion and \
           m1.rodsZone == m2.rodsZone

def create_modAccessControlInp_t():
    tmp = modAccessControlInp_t()
    tmp.recursiveFlag = 12            # int
    tmp.accessLevel = "accessLevel"   # char *
    tmp.userName = "userName"         # char *
    tmp.zone = "zone"                 # char *
    tmp.path = "path"                 # char *
    return tmp

def test_modAccessControlInp_t(m1, m2):
    return m1.recursiveFlag == m2.recursiveFlag and \
           m1.accessLevel == m2.accessLevel and \
           m1.userName == m2.userName and \
           m1.zone == m2.zone and \
           m1.path == m2.path

def create_modAVUMetadataInp_t():
    tmp = modAVUMetadataInp_t()
    tmp.arg0 = "arg0"           # char *
    tmp.arg1 = "arg1"           # char *
    tmp.arg2 = "arg2"           # char *
    tmp.arg3 = "arg3"           # char *
    tmp.arg4 = "arg4"           # char *
    tmp.arg5 = "arg5"           # char *
    tmp.arg6 = "arg6"           # char *
    tmp.arg7 = "arg7"           # char *
    tmp.arg8 = "arg8"           # char *
    tmp.arg9 = "arg9"           # char *
    return tmp

def test_modAVUMetadataInp_t(m1, m2):
    return m1.arg0 == m2.arg0 and \
           m1.arg1 == m2.arg1 and \
           m1.arg2 == m2.arg2 and \
           m1.arg3 == m2.arg3 and \
           m1.arg4 == m2.arg4 and \
           m1.arg5 == m2.arg5 and \
           m1.arg6 == m2.arg6 and \
           m1.arg7 == m2.arg7 and \
           m1.arg8 == m2.arg8 and \
           m1.arg9 == m2.arg9

def create_modDataObjMeta_t():
    tmp = modDataObjMeta_t()
    tmp.dataObjInfo = create_dataObjInfo_t()        # dataObjInfo_t
    tmp.regParam = create_keyValPair_t()            # keyValPair_t
    return tmp

def test_modDataObjMeta_t(m1, m2):
    return test_dataObjInfo_t(m1.dataObjInfo, m2.dataObjInfo) and \
           test_keyValPair_t(m1.regParam, m2.regParam)

def create_msParam_t():
    tmp = msParam_t()
    tmp.label = "label"                     # char *
    tmp.type = "type"                       # char *
    #tmp.inOutStruct = inOutStruct
    #tmp.inpOutBuf = create_bytesBuf_t()     # bytesBuf_t
    return tmp

def test_msParam_t(m1, m2):
    return m1.label == m2.label and \
           m1.type == m2.type# and \
           #test_bytesBuf_t(m1.inpOutBuf, m2.inpOutBuf)

def create_msParamArray_t():
    tmp = msParamArray_t()
    tmp.len = 0                # int
    tmp.oprType = 12            # int
    #tmp.msParam = msParam      # msParam_t **
    return tmp

def test_msParamArray_t(m1, m2):
    return m1.len == m2.len and \
           m2.oprType == m2.oprType

def create_openedDataObjInp_t():
    tmp = openedDataObjInp_t()
    tmp.l1descInx = 12               # int
    tmp.len = 12                     # int
    tmp.whence = 12                  # int
    tmp.oprType = 12                 # int
    tmp.offset = 12                  # rodsLong_t
    tmp.bytesWritten = 12            # rodsLong_t
    init_keyValPair_t(tmp.condInput) # keyValPair_t
    return tmp

def test_openedDataObjInp_t(o1, o2):
    return o1.l1descInx == o2.l1descInx and \
           o1.len == o2.len and \
           o1.whence == o2.whence and \
           o1.oprType == o2.oprType and \
           o1.offset == o2.offset and \
           o1.bytesWritten == o2.bytesWritten and \
           test_keyValPair_t(o1.condInput, o2.condInput)

def create_openStat_t():
    tmp = openStat_t()
    tmp.dataSize = 12           # rodsLong_t
    tmp.dataType = "dataType"   # char []
    tmp.dataMode = "dataMode"   # char []
    tmp.l3descInx = 12          # int
    tmp.replStatus = 12         # int
    tmp.rescTypeInx = 12        # int
    tmp.replNum = 12            # int
    return tmp

def test_openStat_t(o1, o2):
    return o1.dataSize == o2.dataSize and \
           o1.dataType == o2.dataType and \
           o1.dataMode == o2.dataMode and \
           o1.l3descInx == o2.l3descInx and \
           o1.replStatus == o2.replStatus and \
           o1.rescTypeInx == o2.rescTypeInx and \
           o1.replNum == o2.replNum

def create_operProgress_t():
    tmp = operProgress_t()
    tmp.oprType = 12                # int
    tmp.flag = 12                   # int'
    tmp.totalNumFiles = 12          # rodsLong_t
    tmp.totalFileSize = 12          # rodsLong_t
    tmp.totalNumFilesDone = 12      # rodsLong_t
    tmp.totalFileSizeDone = 12      # rodsLong_t
    tmp.curFileName = "curFileName" # char []
    tmp.curFileSize = 12            # rodsLong_t
    tmp.curFileSizeDone = 12        # rodsLong_t
    return tmp

def init_operProgress_t(tmp):
    tmp.oprType = 12                # int
    tmp.flag = 12                   # int
    tmp.totalNumFiles = 12          # rodsLong_t
    tmp.totalFileSize = 12          # rodsLong_t
    tmp.totalNumFilesDone = 12      # rodsLong_t
    tmp.totalFileSizeDone = 12      # rodsLong_t
    tmp.curFileName = "curFileName" # char []
    tmp.curFileSize = 12            # rodsLong_t
    tmp.curFileSizeDone = 12        # rodsLong_t

def test_operProgress_t(o1, o2):
    return o1.oprType == o2.oprType and \
           o1.flag == o2.flag and \
           o1.totalNumFiles == o2.totalNumFiles and \
           o1.totalFileSize == o2.totalFileSize and \
           o1.totalNumFilesDone == o2.totalNumFilesDone and \
           o1.totalFileSizeDone == o2.totalFileSizeDone and \
           o1.curFileName == o2.curFileName and \
           o1.curFileSize == o2.curFileSize and \
           o1.curFileSizeDone == o2.curFileSizeDone

def create_portalOprOut_t():
    tmp = portalOprOut_t()
    tmp.status = 12                 # int
    tmp.l1descInx = 12              # int
    tmp.numThreads = 12             # int
    tmp.chksum = "chksum"           # char []
    init_portList_t(tmp.portList)   # portList_t
    return tmp

def init_portalOprOut_t(tmp):
    tmp.status = 12                 # int
    tmp.l1descInx = 12              # int
    tmp.numThreads = 12             # int
    tmp.chksum = "chksum"           # char []
    init_portList_t(tmp.portList)   # portList_t

def test_portalOprOut_t(p1, p2):
    return p1.status == p2.status and \
           p1.l1descInx == p2.l1descInx and \
           p1.numThreads == p2.numThreads and \
           p1.chksum == p2.chksum and \
           test_portList_t(p1.portList, p2.portList)

def create_portList_t():
    tmp = portList_t()
    tmp.portNum = 12          # int
    tmp.cookie = 12           # int
    tmp.windowSize = 12       # int
    tmp.hostAddr = "hostAddr" # char []
    return tmp

def init_portList_t(p1):
    p1.portNum = 12           # int
    p1.cookie = 12            # int
    p1.windowSize = 12        # int
    p1.hostAddr = "hostAddr"  # char []

def test_portList_t(p1, p2):
    return p1.portNum == p2.portNum and \
           p1.cookie == p2.cookie and \
           p1.windowSize == p2.windowSize and \
           p1.hostAddr == p2.hostAddr

def create_queryHandle_t():
    tmp = queryHandle_t()
    tmp.conn = create_rcComm_t()        # void *
    tmp.connType = RC_COMM              # connType_t
    #funcPtr querySpecColl;
    #funcPtr genQuery;
    return tmp

def init_queryHandle_t(tmp):
    tmp.conn = create_rcComm_t()        # void *
    tmp.connType = RC_COMM              # connType_t

def test_queryHandle_t(q1, q2):
    return test_rcComm_t(q1.get_rcComm(), q2.get_rcComm()) and \
           q1.connType == q2.connType

def create_rcComm_t():
    tmp = rcComm_t()
    tmp.irodsProt = NATIVE_PROT               # irodsProt_t
    tmp.host = "host"                         # char []
    tmp.sock = 12                             # int
    tmp.portNum = 12                          # int
    tmp.loggedIn = 12                         # int
    #tmp.localAddr                            # sockaddr_in
    #tmp.remoteAddr                           # sockaddr_in
    init_userInfo_t(tmp.proxyUser)            # userInfo_t
    init_userInfo_t(tmp.clientUser)           # userInfo_t
    tmp.svrVersion = create_version_t()       # version_t
    tmp.rError = create_rError_t()            # rError_t
    tmp.flag = 12                             # int
    init_transferStat_t(tmp.transStat)        # transferStat_t
    tmp.apiInx = 12                           # int
    tmp.status = 12                           # int
    tmp.windowSize = 12                       # int
    tmp.reconnectedSock = 12                  # int
    #tmp.reconnTime                           # time_t
    tmp.agentState = PROCESSING_STATE         # procState_t
    tmp.clientState = PROCESSING_STATE        # procState_t
    tmp.reconnThrState = PROCESSING_STATE     # procState_t
    init_operProgress_t(tmp.operProgress)     # operProgress_t
    init_fileRestart_t(tmp.fileRestart)       # fileRestart_t
    return tmp

def test_rcComm_t(r1, r2):
    return r1.irodsProt == r2.irodsProt and \
           r1.host == r2.host and \
           r1.sock == r2.sock and \
           r1.portNum == r2.portNum and \
           r1.loggedIn == r2.loggedIn and \
           test_userInfo_t(r1.proxyUser, r2.proxyUser) and \
           test_userInfo_t(r1.clientUser, r2.clientUser) and \
           test_version_t(r1.svrVersion, r2.svrVersion) and \
           test_rError_t(r1.rError, r2.rError) and \
           r1.flag == r2.flag and \
           test_transferStat_t(r1.transStat, r2.transStat) and \
           r1.apiInx == r2.apiInx and \
           r1.status == r2.status and \
           r1.windowSize == r2.windowSize and \
           r1.reconnectedSock == r2.reconnectedSock and \
           r1.agentState == r2.agentState and \
           r1.clientState == r2.clientState and \
           r1.reconnThrState == r2.reconnThrState and \
           test_operProgress_t(r1.operProgress, r2.operProgress) and \
           test_fileRestart_t(r1.fileRestart, r2.fileRestart)

def create_rcvXmsgInp_t():
    tmp = rcvXmsgInp_t()
    tmp.rcvTicket = 12                  # unsigned int
    tmp.msgNumber = 12                  # unsigned int
    tmp.seqNumber = 12                  # unsigned int
    tmp.msgCondition = "msgCondition"   # char []
    return tmp

def test_rcvXmsgInp_t(r1, r2):
    return r1.rcvTicket == r2.rcvTicket and \
           r1.msgNumber == r2.msgNumber and \
           r1.seqNumber == r2.seqNumber and \
           r1.msgCondition == r2.msgCondition

def create_rcvXmsgOut_t():
    tmp = rcvXmsgOut_t()
    tmp.msgType = "msgType"             # char []
    tmp.sendUserName = "sendUserName"   # char []
    tmp.sendAddr = "sendAddr"           # char []
    tmp.msgNumber = 12                  # unsigned int
    tmp.seqNumber = 12                  # unsigned int
    tmp.msg = "msg"                     # char *
    return tmp

def test_rcvXmsgOut_t(r1, r2):
    return r1.msgType == r2.msgType and \
           r1.sendUserName == r2.sendUserName and \
           r1.sendAddr == r2.sendAddr and \
           r1.sendUserName == r2.sendUserName and \
           r1.seqNumber == r2.seqNumber and \
           r1.msg == r2.msg

def create_regReplica_t():
    tmp = regReplica_t()
    tmp.srcDataObjInfo = create_dataObjInfo_t()     # dataObjInfo_t *
    tmp.destDataObjInfo = create_dataObjInfo_t()    # dataObjInfo_t *
    init_keyValPair_t(tmp.condInput)                # keyValPair_t
    return tmp

def test_regReplica_t(r1, r2):
    return test_dataObjInfo_t(r1.srcDataObjInfo, r2.srcDataObjInfo) and \
           test_dataObjInfo_t(r1.destDataObjInfo, r2.destDataObjInfo) and \
           test_keyValPair_t(r1.condInput, r2.condInput)

def create_rescInfo_t():
    tmp = rescInfo_t()
    tmp.rescName = "rescName"                       # char []
    tmp.rescId = 12                                 # rodsLong_t
    tmp.zoneName = "zoneName"                       # char []
    tmp.rescLoc = "rescLoc"                         # char []
    tmp.rescType = "rescType"                       # char []
    tmp.rescTypeInx = 12                            # int
    tmp.rescClassInx = 12                           # int
    tmp.rescStatus = 12                             # int
    tmp.paraOpr = 12                                # int
    tmp.rescClass = "rescClass"                     # char []
    tmp.rescVaultPath = "rescVaultPath"             # char []
    tmp.rescInfo = "rescInfo"                       # char []
    tmp.rescComments = "rescComments"               # char []
    tmp.gateWayAddr = "gateWayAddr"                 # char []
    tmp.rescMaxObjSize = 12                         # rodsLong_t
    tmp.freeSpace = 12                              # rodsLong_t
    tmp.freeSpaceTimeStamp = "freeSpaceTimeStamp"   # char []
    #tmp.freeSpaceTime                              #  time_t
    tmp.rescCreate = "rescCreate"                   # char []
    tmp.rescModify = "rescModify"                   # char []
    #tmp.rodsServerHost                             # void *
    tmp.quotaLimit = 12                             # rodsLong_t
    tmp.quotaOverrun = 12                           # rodsLong_t
    return tmp

def test_rescInfo_t(r1, r2):
    return r1.rescId == r2.rescId and \
           r1.zoneName == r2.zoneName and \
           r1.rescLoc == r2.rescLoc and \
           r1.rescType == r2.rescType and \
           r1.rescTypeInx == r2.rescTypeInx and \
           r1.rescClassInx == r2.rescClassInx and \
           r1.rescStatus == r2.rescStatus and \
           r1.paraOpr == r2.paraOpr and \
           r1.rescClass == r2.rescClass and \
           r1.rescVaultPath == r2.rescVaultPath and \
           r1.rescInfo == r2.rescInfo and \
           r1.rescComments == r2.rescComments and \
           r1.gateWayAddr == r2.gateWayAddr and \
           r1.rescMaxObjSize == r2.rescMaxObjSize and \
           r1.freeSpace == r2.freeSpace and \
           r1.freeSpaceTimeStamp == r2.freeSpaceTimeStamp and \
           r1.rescCreate == r2.rescCreate and \
           r1.rescModify == r2.rescModify and \
           r1.quotaLimit == r2.quotaLimit and \
           r1.quotaOverrun == r2.quotaOverrun

def create_rErrMsg_t():
    tmp = rErrMsg_t()
    tmp.status = 12         # int
    tmp.msg = "msg"         # char []
    return tmp

def test_rErrMsg_t(r1, r2):
    return r1.status == r2.status and \
           r2.msg == r2.msg

def create_rError_t():
    tmp = rError_t()
    tmp.len = 12           # int
    #tmp.errMsg            # rErrMsg_t **
    return tmp

def test_rError_t(r1, r2): #errMsg
    return r1.len == r2.len

def create_rodsArguments_t():
    tmp = rodsArguments_t()
    tmp.add = 12                                        # int
    tmp.age = 12                                        # int
    tmp.agevalue = 12                                   # int
    tmp.all = 12                                        # int
    tmp.accessControl = 12                              # int
    tmp.admin = 12                                      # int
    tmp.ascitime = 12                                   # int
    tmp.attr = 12                                       # int
    tmp.noattr = 12                                     # int
    tmp.attrStr = "attrStr"                             # char *
    tmp.bulk = 12                                       # int
    tmp.backupMode  = 12                                # int
    tmp.condition = 12                                  # int
    tmp.conditionString = "conditionString"             # char *
    tmp.collection = 12                                 # int
    tmp.collectionString = "collectionString"           # char *
    tmp.dataObjects = 12                                # int
    tmp.dim = 12                                        # int
    tmp.dryrun = 12                                     # int
    tmp.echo = 12                                       # int
    tmp.empty = 12                                      # int
    tmp.force = 12                                      # int
    tmp.file = 12                                       # int
    tmp.fileString = "fileString"                       # char *
    tmp.rescGroup = 12                                  # int
    tmp.rescGroupString = "rescGroupString"             # char *
    tmp.header = 12                                     # int
    tmp.help = 12                                       # int
    tmp.hostAddr = 12                                   # int
    tmp.hostAddrString = "hostAddrString"               # char *
    tmp.input = 12                                      # int
    tmp.redirectConn = 12                               # int
    tmp.checksum = 12                                   # int
    tmp.verifyChecksum = 12                             # int
    tmp.dataType = 12                                   # int
    tmp.dataTypeString  = "dataTypeString"              # char *
    tmp.longOption = 12                                 # int
    tmp.link = 12                                       # int
    tmp.rlock = 12                                      # int
    tmp.wlock = 12                                      # int
    tmp.veryLongOption = 12                             # int
    tmp.mountCollection = 12                            # int
    tmp.mountType  = "mountType"                        # char *
    tmp.replNum = 12                                    # int
    tmp.replNumValue = "replNumValue"                   # char *
    tmp.noPage = 12                                     # int
    tmp.number = 12                                     # int
    tmp.numberValue = 12                                # int
    tmp.physicalPath = 12                               # int
    tmp.physicalPathString = "physicalPathString"       # char *
    tmp.logicalPath = 12                                # int
    tmp.logicalPathString = "logicalPathString"         # char *
    tmp.progressFlag = 12                               # int
    tmp.option = 12                                     # int
    tmp.optionString = "optionString"                   # char *
    tmp.orphan = 12                                     # int
    tmp.purgeCache = 12                                 # int
    tmp.bundle = 12                                     # int
    tmp.prompt = 12                                     # int
    tmp.query = 12                                      # int
    tmp.queryStr = "queryStr"                           # char *
    tmp.rbudp = 12                                      # int
    tmp.reg = 12                                        # int
    tmp.recursive = 12                                  # int
    tmp.resource = 12                                   # int
    tmp.resourceString = "resourceString"               # char *
    tmp.remove = 12                                     # int
    tmp.sizeFlag = 12                                   # int
    tmp.size = 12                                       # rodsLong_t
    tmp.srcResc = 12                                    # int
    tmp.srcRescString = "srcRescString"                 # char *
    tmp.subset = 12                                     # int
    tmp.subsetByVal = 12                                # int
    tmp.subsetStr = "subsetStr"                         # char *
    tmp.test = 12                                       # int
    tmp.ticket = 12                                     # int
    tmp.ticketString = "ticketString"                   # char *
    tmp.reconnect = 12                                  # int
    tmp.user = 12                                       # int
    tmp.userString = "userString"                       # char *
    tmp.unmount = 12                                    # int
    tmp.verbose = 12                                    # int
    tmp.veryVerbose = 12                                # int
    tmp.zone = 12                                       # int
    tmp.zoneName = "zoneName"                           # char *
    tmp.verify = 12                                     # int
    tmp.var = 12                                        # int
    tmp.varStr = "varStr"                               # char *
    tmp.extract  = 12                                   # int
    tmp.restart = 12                                    # int
    tmp.restartFileString = "restartFileString"         # char *
    tmp.lfrestart = 12                                  # int
    tmp.lfrestartFileString = "lfrestartFileString"     # char *
    tmp.version = 12                                    # int
    tmp.retries = 12                                    # int
    tmp.retriesValue = 12                               # int
    tmp.regRepl = 12                                    # int
    tmp.excludeFile = 12                                # int
    tmp.excludeFileString = "excludeFileString"         # char *
    tmp.parallel = 12                                   # int
    tmp.serial = 12                                     # int
    tmp.masterIcat = 12                                 # int
    tmp.silent = 12                                     # int
    tmp.sql = 12                                        # int
    tmp.optind = 12                                     # int
    return tmp

def test_rodsArguments_t(r1, r2):
    return r1.add == r2.add and \
           r1.age == r2.age and \
           r1.agevalue == r2.agevalue and \
           r1.all == r2.all and \
           r1.accessControl == r2.accessControl and \
           r1.admin == r2.admin and \
           r1.ascitime == r2.ascitime and \
           r1.attr == r2.attr and \
           r1.noattr == r2.noattr and \
           r1.attrStr == r2.attrStr and \
           r1.bulk == r2.bulk and \
           r1.backupMode  == r2.backupMode and \
           r1.condition == r2.condition and \
           r1.conditionString == r2.conditionString and \
           r1.collection == r2.collection and \
           r1.collectionString == r2.collectionString and \
           r1.dataObjects == r2.dataObjects and \
           r1.dim == r2.dim and \
           r1.dryrun == r2.dryrun and \
           r1.echo == r2.echo and \
           r1.empty == r2.empty and \
           r1.force == r2.force and \
           r1.file == r2.file and \
           r1.fileString == r2.fileString and \
           r1.rescGroup == r2.rescGroup and \
           r1.rescGroupString == r2.rescGroupString and \
           r1.header == r2.header and \
           r1.help == r2.help and \
           r1.hostAddr == r2.hostAddr and \
           r1.hostAddrString == r2.hostAddrString and \
           r1.input == r2.input and \
           r1.redirectConn == r2.redirectConn and \
           r1.checksum == r2.checksum and \
           r1.verifyChecksum == r2.verifyChecksum and \
           r1.dataType == r2.dataType and \
           r1.dataTypeString  == r2.dataTypeString and \
           r1.longOption == r2.longOption and \
           r1.link == r2.link and \
           r1.rlock == r2.rlock and \
           r1.wlock == r2.wlock and \
           r1.veryLongOption == r2.veryLongOption and \
           r1.mountCollection == r2.mountCollection and \
           r1.mountType  == r2.mountType and \
           r1.replNum == r2.replNum and \
           r1.replNumValue == r2.replNumValue and \
           r1.noPage == r2.noPage and \
           r1.number == r2.number and \
           r1.numberValue == r2.numberValue and \
           r1.physicalPath == r2.physicalPath and \
           r1.physicalPathString == r2.physicalPathString and \
           r1.logicalPath == r2.logicalPath and \
           r1.logicalPathString == r2.logicalPathString and \
           r1.progressFlag == r2.progressFlag and \
           r1.option == r2.option and \
           r1.optionString == r2.optionString and \
           r1.orphan == r2.orphan and \
           r1.purgeCache == r2.purgeCache and \
           r1.bundle == r2.bundle and \
           r1.prompt == r2.prompt and \
           r1.query == r2.query and \
           r1.queryStr == r2.queryStr and \
           r1.rbudp == r2.rbudp and \
           r1.reg == r2.reg and \
           r1.recursive == r2.recursive and \
           r1.resource == r2.resource and \
           r1.resourceString == r2.resourceString and \
           r1.remove == r2.remove and \
           r1.sizeFlag == r2.sizeFlag and \
           r1.size == r2.size and \
           r1.srcResc == r2.srcResc and \
           r1.srcRescString == r2.srcRescString and \
           r1.subset == r2.subset and \
           r1.subsetByVal == r2.subsetByVal and \
           r1.subsetStr == r2.subsetStr and \
           r1.test == r2.test and \
           r1.ticket == r2.ticket and \
           r1.ticketString == r2.ticketString and \
           r1.reconnect == r2.reconnect and \
           r1.user == r2.user and \
           r1.userString == r2.userString and \
           r1.unmount == r2.unmount and \
           r1.verbose == r2.verbose and \
           r1.veryVerbose == r2.veryVerbose and \
           r1.zone == r2.zone and \
           r1.zoneName == r2.zoneName and \
           r1.verify == r2.verify and \
           r1.var == r2.var and \
           r1.varStr == r2.varStr and \
           r1.extract  == r2.extract and \
           r1.restart == r2.restart and \
           r1.restartFileString == r2.restartFileString and \
           r1.lfrestart == r2.lfrestart and \
           r1.lfrestartFileString == r2.lfrestartFileString and \
           r1.version == r2.version and \
           r1.retries == r2.retries and \
           r1.retriesValue == r2.retriesValue and \
           r1.regRepl == r2.regRepl and \
           r1.excludeFile == r2.excludeFile and \
           r1.excludeFileString == r2.excludeFileString and \
           r1.parallel == r2.parallel and \
           r1.serial == r2.serial and \
           r1.masterIcat == r2.masterIcat and \
           r1.silent == r2.silent and \
           r1.sql == r2.sql and \
           r1.optind == r2.optind

def create_rodsDirent_t():
    tmp = rodsDirent_t()
    tmp.d_offset = 12           #  unsigned int
    tmp.d_ino = 12              #  unsigned int
    tmp.d_reclen = 12           #  unsigned int
    tmp.d_namlen = 12           #  unsigned int
    tmp.d_name = "d_name"       # char []
    return tmp

def test_rodsDirent_t(r1, r2):
    return r1.d_offset == r2.d_offset and \
           r1.d_ino == r2.d_ino and \
           r1.d_reclen == r2.d_reclen and \
           r1.d_namlen == r2.d_namlen and \
           r1.d_name == r2.d_name

def create_rodsEnv():
    tmp = rodsEnv()
    tmp.rodsUserName = "rodsUserName"           # char []
    tmp.rodsHost = "rodsHost"                   # char []
    tmp.rodsPort = 12                           # int
    tmp.xmsgHost = "xmsgHost"                   # char []
    tmp.xmsgPort = 12                           # int
    tmp.rodsHome = "rodsHome"                   # char []
    tmp.rodsCwd = "rodsCwd"                     # char []
    tmp.rodsAuthScheme = "rodsAuthScheme"       # char []
    tmp.rodsDefResource = "rodsDefResource"     # char []
    tmp.rodsZone = "rodsZone"                   # int
    tmp.rodsServerDn = "rodsServerDn"           # char *
    tmp.rodsLogLevel = 12                       # int
    tmp.rodsAuthFileName = "rodsAuthFileName"   # char []
    tmp.rodsDebug = "rodsDebug"                 # char []
    return tmp

def test_rodsEnv(r1, r2):
    return r1.rodsUserName == r2.rodsUserName and \
           r1.rodsHost == r2.rodsHost and \
           r1.rodsPort == r2.rodsPort and \
           r1.xmsgHost == r2.xmsgHost and \
           r1.xmsgPort == r2.xmsgPort and \
           r1.rodsHome == r2.rodsHome and \
           r1.rodsCwd == r2.rodsCwd and \
           r1.rodsAuthScheme == r2.rodsAuthScheme and \
           r1.rodsDefResource == r2.rodsDefResource and \
           r1.rodsZone == r2.rodsZone and \
           r1.rodsServerDn == r2.rodsServerDn and \
           r1.rodsLogLevel == r2.rodsLogLevel and \
           r1.rodsAuthFileName == r2.rodsAuthFileName and \
           r1.rodsDebug == r2.rodsDebug

def create_rodsHostAddr_t():
    tmp = rodsHostAddr_t()
    tmp.hostAddr = "hostAddr"       # char []
    tmp.zoneName = "zoneName"       # char []
    tmp.portNum = 12                # int
    tmp.dummyInt = 12               # int
    return tmp

def init_rodsHostAddr_t(tmp):
    tmp.hostAddr = "hostAddr"       # char []
    tmp.zoneName = "zoneName"       # char []
    tmp.portNum = 12                # int
    tmp.dummyInt = 12               # int

def test_rodsHostAddr_t(r1, r2):
    return r1.hostAddr == r2.hostAddr and \
           r1.zoneName == r2.zoneName and \
           r1.portNum == r2.portNum and \
           r1.dummyInt == r2.dummyInt

def create_rodsObjStat_t():
    tmp = rodsObjStat_t()
    tmp.objSize = 12                        # int
    tmp.objType = UNKNOWN_OBJ_T             # objType_t
    tmp.dataMode = 12                       # int
    tmp.dataId = "dataId"                   # char []
    tmp.chksum = "chksum"                   # char []
    tmp.ownerName = "ownerName"             # char []
    tmp.ownerZone = "ownerZone"             # char []
    tmp.createTime = "createTime"           # char []
    tmp.modifyTime = "modifyTime"           # char []
    tmp.specColl = create_specColl_t()      # specColl_t
    return tmp

def init_rodsObjStat_t(tmp):
    tmp.objSize = 12                        # int
    tmp.objType = UNKNOWN_OBJ_T             # objType_t
    tmp.dataMode = 12                       # int
    tmp.dataId = "dataId"                   # char []
    tmp.chksum = "chksum"                   # char []
    tmp.ownerName = "ownerName"             # char []
    tmp.ownerZone = "ownerZone"             # char []
    tmp.createTime = "createTime"           # char []
    tmp.modifyTime = "modifyTime"           # char []
    tmp.specColl = create_specColl_t()      # specColl_t

def test_rodsObjStat_t(r1, r2):
    return r1.objSize == r2.objSize and \
           r1.objType == r2.objType and \
           r1.dataMode == r2.dataMode and \
           r1.dataId == r2.dataId and \
           r1.chksum == r2.chksum and \
           r1.ownerName == r2.ownerName and \
           r1.ownerZone == r2.ownerZone and \
           r1.createTime == r2.createTime and \
           r1.modifyTime == r2.modifyTime and \
           test_specColl_t(r1.specColl, r2.specColl)

def create_rodsPath_t():
    tmp = rodsPath_t()
    tmp.objType = UNKNOWN_OBJ_T                 # objType_t
    tmp.objState = UNKNOWN_ST                   # objStat_t
    tmp.size = 12                               # rodsLong_t
    tmp.objMode = 12                            # unsigned int
    tmp.inPath = "inPath"                       # char []
    tmp.outPath = "outPath"                     # char []
    tmp.dataId = "dataId"                       # char []
    tmp.chksum = "chksum"                       # char []
    tmp.rodsObjStat = create_rodsObjStat_t()    # rodsObjStat_t
    return tmp

def test_rodsPath_t(r1, r2):
    return r1.objType == r2.objType and \
           r1.objState == r2.objState and \
           r1.size == r2.size and \
           r1.objMode == r2.objMode and \
           r1.inPath == r2.inPath and \
           r1.outPath == r2.outPath and \
           r1.dataId == r2.dataId and \
           r1.chksum == r2.chksum and \
           test_rodsObjStat_t(r1.rodsObjStat, r2.rodsObjStat)

def create_rodsPathInp_t():
    tmp = rodsPathInp_t()
    tmp.numSrc = 12                         # int
    tmp.srcPath = create_rodsPath_t()       # rodsPath_t *
    tmp.destPath = create_rodsPath_t()      # rodsPath_t *
    tmp.targPath = create_rodsPath_t()      # rodsPath_t *
    tmp.resolved = 12                       # int
    return tmp

def test_rodsPathInp_t(r1, r2):
    return r1.numSrc == r2.numSrc and \
           test_rodsPath_t(r1.srcPath, r2.srcPath) and \
           test_rodsPath_t(r1.destPath, r2.destPath) and \
           test_rodsPath_t(r1.targPath, r2.targPath) and \
           r1.resolved == r2.resolved

def create_rodsRestart_t():
    tmp = rodsRestart_t()
    tmp.restartFile = "restartFile"     # char []
    tmp.fd = 12                         # int
    tmp.doneCnt = 12                    # int
    tmp.collection = "collection"       # char []
    tmp.lastDonePath = "lastDonePath"   # char []
    tmp.oprType = "oprType"             # char []
    tmp.curCnt = 12                     # int
    tmp.restartState = 12               # int
    return tmp

def test_rodsRestart_t(r1, r2):
    return r1.restartFile == r2.restartFile and \
           r1.fd == r2.fd and \
           r1.doneCnt == r2.doneCnt and \
           r1.collection == r2.collection and \
           r1.lastDonePath == r2.lastDonePath and \
           r1.oprType == r2.oprType and \
           r1.curCnt == r2.curCnt and \
           r1.restartState == r2.restartState

def create_rodsStat_t():
    tmp = rodsStat_t()
    tmp.st_size = 12            # rodsLong_t
    tmp.st_dev = 12             # unsigned int
    tmp.st_ino = 12             # unsigned int
    tmp.st_mode = 12            # unsigned int
    tmp.st_nlink = 12           # unsigned int
    tmp.st_uid = 12             # unsigned int
    tmp.st_gid = 12             # unsigned int
    tmp.st_rdev = 12            # unsigned int
    tmp.st_atim = 12            # unsigned int
    tmp.st_mtim = 12            # unsigned int
    tmp.st_ctim = 12            # unsigned int
    tmp.st_blksize = 12         # unsigned int
    tmp.st_blocks = 12          # unsigned int
    return tmp

def test_rodsStat_t(r1, r2):
    return r1.st_size == r2.st_size and \
           r1.st_dev == r2.st_dev and \
           r1.st_ino == r2.st_ino and \
           r1.st_mode == r2.st_mode and \
           r1.st_nlink == r2.st_nlink and \
           r1.st_uid == r2.st_uid and \
           r1.st_gid == r2.st_gid and \
           r1.st_rdev == r2.st_rdev and \
           r1.st_atim == r2.st_atim and \
           r1.st_mtim == r2.st_mtim and \
           r1.st_ctim == r2.st_ctim and \
           r1.st_blksize == r2.st_blksize and \
           r1.st_blocks == r2.st_blocks

def create_ruleExecDelInp_t():
    tmp = ruleExecDelInp_t()
    tmp.ruleExecId = "ruleExecId"       # char []
    return tmp

def test_ruleExecDelInp_t(r1, r2):
    return r1.ruleExecId == r2.ruleExecId

def create_ruleExecModInp_t():
    tmp = ruleExecModInp_t()
    tmp.ruleId = "ruleId"                   # char []
    init_keyValPair_t(tmp.condInput)        # keyValPair_t
    return tmp

def test_ruleExecModInp_t(r1, r2):
    return r1.ruleId == r2.ruleId and \
           test_keyValPair_t(r1.condInput, r2.condInput)

def create_ruleExecSubmitInp_t():
    tmp = ruleExecSubmitInp_t()
    tmp.ruleName = "ruleName"                       # char []
    tmp.reiFilePath = "reiFilePath"                 # char []
    tmp.userName = "userName"                       # char []
    tmp.exeAddress = "exeAddress"                   # char []
    tmp.exeTime = "exeTime"                         # char []
    tmp.exeFrequency = "exeFrequency"               # char []
    tmp.priority = "priority"                       # char []
    tmp.lastExecTime = "lastExecTime"               # char []
    tmp.exeStatus = "exeStatus"                     # char []
    tmp.estimateExeTime = "estimateExeTime"         # char []
    tmp.notificationAddr = "notificationAddr"       # char []
    init_keyValPair_t(tmp.condInput)                # keyValPair_t
    tmp.packedReiAndArgBBuf = create_bytesBuf_t()   # bytesBuf_t *
    tmp.ruleExecId = "ruleExecId"                   # char []
    return tmp

def test_ruleExecSubmitInp_t(r1, r2):
    return r1.ruleName == r2.ruleName and \
           r1.reiFilePath == r2.reiFilePath and \
           r1.userName == r2.userName and \
           r1.exeAddress == r2.exeAddress and \
           r1.exeTime == r2.exeTime and \
           r1.exeFrequency == r2.exeFrequency and \
           r1.priority == r2.priority and \
           r1.lastExecTime == r2.lastExecTime and \
           r1.exeStatus == r2.exeStatus and \
           r1.estimateExeTime == r2.estimateExeTime and \
           r1.notificationAddr == r2.notificationAddr and \
           test_keyValPair_t(r1.condInput, r2.condInput) and \
           test_bytesBuf_t(r1.packedReiAndArgBBuf, r2.packedReiAndArgBBuf) and \
           r1.ruleExecId == r2.ruleExecId

def create_sendXmsgInfo_t():
    tmp = sendXmsgInp_t()
    tmp.msgNumber = 12                 # unsigned int
    tmp.msgType = "msgType"            # char []
    tmp.numRcv = 12                    # unsigned int
    tmp.flag = 12                      # int
    tmp.msg = "msg"                    # char *
    tmp.numDeli = 12                   # int
    #tmp.deliAddress = deliAddress     # char **
    #tmp.deliPort = deliPort           # unsigned int *
    tmp.miscInfo = "miscInfo"          # char *
    return tmp

def init_sendXmsgInfo_t(tmp):
    tmp.msgNumber = 12                 # unsigned int
    tmp.msgType = "msgType"            # char []
    tmp.numRcv = 12                    # unsigned int
    tmp.flag = 12                      # int
    tmp.msg = "msg"                    # char *
    tmp.numDeli = 12                   # int
    #tmp.deliAddress = deliAddress     # char **
    #tmp.deliPort = deliPort           # unsigned int *
    tmp.miscInfo = "miscInfo"          # char *

def test_sendXmsgInfo_t(s1, s2):
    return s1.msgNumber == s2.msgNumber and \
           s1.msgType == s2.msgType and \
           s1.numRcv == s2.numRcv and \
           s1.flag == s2.flag and \
           s1.msg == s2.msg and \
           s1.numDeli == s2.numDeli and \
           s1.miscInfo == s2.miscInfo

def create_sendXmsgInp_t():
    tmp = sendXmsgInp_t()
    init_xmsgTicketInfo_t(tmp.ticket)           # xmsgTicketInfo_t
    tmp.sendAddr = "sendAddr"                   # char []
    init_sendXmsgInfo_t(tmp.sendXmsgInfo)       # sendXmsgInfo_t
    return tmp

def init_sendXmsgInp_t(tmp):
    init_xmsgTicketInfo_t(tmp.ticket)           # xmsgTicketInfo_t
    tmp.sendAddr = "sendAddr"                   # char []
    init_sendXmsgInfo_t(tmp.sendXmsgInfo)       # sendXmsgInfo_t

def test_sendXmsgInp_t(s1, s2):
    return test_xmsgTicketInfo_t(s1.ticket, s2.ticket) and \
           s1.sendAddr == s2.sendAddr and \
           test_sendXmsgInfo_t(s1.sendXmsgInfo, s2.sendXmsgInfo)

def create_simpleQueryInp_t():
    tmp = simpleQueryInp_t()
    tmp.sql = "sql"             # char *
    tmp.arg1 = "arg1"           # char *
    tmp.arg2 = "arg2"           # char *
    tmp.arg3 = "arg3"           # char *
    tmp.arg4 = "arg4"           # char *
    tmp.control = 12            # int
    tmp.form = 12               # int
    tmp.maxBufSize = 12         # int
    return tmp

def test_simpleQueryInp_t(s1, s2):
    return s1.sql == s2.sql and \
           s1.arg1 == s2.arg1 and \
           s1.arg2 == s2.arg2 and \
           s1.arg3 == s2.arg3 and \
           s1.arg4 == s2.arg4 and \
           s1.control == s2.control and \
           s1.form == s2.form and \
           s1.maxBufSize == s2.maxBufSize

def create_simpleQueryOut_t():
    tmp = simpleQueryOut_t()
    tmp.control = 12            # int
    tmp.outBuf = "outBuf"       # char *
    return tmp

def test_simpleQueryOut_t(s1, s2):
    return s1.control == s2.control and \
           s1.outBuf == s2.outBuf

def create_specColl_t():
    tmp = specColl_t()
    tmp.collClass =  NO_SPEC_COLL   # specCollClass_t
    tmp.type = HAAW_STRUCT_FILE_T   # structFileType_t
    tmp.collection = "collection"   # char []
    tmp.objPath = "objPath"         # char []
    tmp.resource = "resource"       # char []
    tmp.phyPath = "phyPath"         # char []
    tmp.cacheDir = "cacheDir"       # char []
    tmp.cacheDirty = 12             # int
    tmp.replNum = 12                # int
    return tmp

def init_specColl_t(tmp):
    tmp.collClass =  NO_SPEC_COLL   # specCollClass_t
    tmp.type = HAAW_STRUCT_FILE_T   # structFileType_t
    tmp.collection = "collection"   # char []
    tmp.objPath = "objPath"         # char []
    tmp.resource = "resource"       # char []
    tmp.phyPath = "phyPath"         # char []
    tmp.cacheDir = "cacheDir"       # char []
    tmp.cacheDirty = 12             # int
    tmp.replNum = 12                # int

def test_specColl_t(s1, s2):
    return s1.collClass == s2.collClass and \
           s1.type == s2.type and \
           s1.collection == s2.collection and \
           s1.objPath == s2.objPath and \
           s1.resource == s2.resource and \
           s1.phyPath == s2.phyPath and \
           s1.cacheDir == s2.cacheDir and \
           s1.cacheDirty == s2.cacheDirty and \
           s1.replNum == s2.replNum

def create_sqlResult_t():
    tmp = sqlResult_t()
    tmp.attriInx = 12           # int
    tmp.len = 12                # int
    tmp.value = "value"         # char *
    return tmp

def init_sqlResult_t(tmp):
    tmp.attriInx = 12           # int
    tmp.len = 12                # int
    tmp.value = "value"         # char *

def test_sqlResult_t(s1, s2):
    return s1.attriInx == s2.attriInx and \
           s1.len == s2.len and \
           s1.value == s2.value

def create_structFileExtAndRegInp_t():
    tmp = structFileExtAndRegInp_t()
    tmp.objPath = "objPath"                 # char []
    tmp.collection = "collection"           # char []
    tmp.oprType = 12                        # int
    tmp.flags = 12                          # int
    init_keyValPair_t(tmp.condInput)        # keyValPair_t
    return tmp

def test_structFileExtAndRegInp_t(s1, s2):
    return s1.objPath == s2.objPath and \
           s1.collection == s2.collection and \
           s1.oprType == s2.oprType and \
           s1.flags == s2.flags and \
           test_keyValPair_t(s1.condInput, s2.condInput)

def create_structFileOprInp_t():
    tmp = structFileOprInp_t()
    init_rodsHostAddr_t(tmp.addr)           # rodsHostAddr_t
    tmp.oprType = 12                        # int
    tmp.flags = 12                          # int
    tmp.specColl = create_specColl_t()      # specColl_t
    init_keyValPair_t(tmp.condInput)        # keyValPair_t
    return tmp

def test_structFileOprInp_t(s1, s2):
    return test_rodsHostAddr_t(s1.addr, s2.addr) and \
           s1.oprType == s2.oprType and \
           s1.flags == s2.flags and \
           test_specColl_t(s1.specColl, s2.specColl) and \
           test_keyValPair_t(s1.condInput, s2.condInput)

def create_subFile_t():
    tmp = subFile_t()
    init_rodsHostAddr_t(tmp.addr)       # rodsHostAddr_t
    tmp.subFilePath = "subFilePath"     # char []
    tmp.mode = 12                       # int
    tmp.flags = 12                      # int
    tmp.offset = 12                     # rodsLong_t
    tmp.specColl = create_specColl_t()  # specColl_t *
    return tmp

def init_subFile_t(tmp):
    init_rodsHostAddr_t(tmp.addr)       # rodsHostAddr_t
    tmp.subFilePath = "subFilePath"     # char []
    tmp.mode = 12                       # int
    tmp.flags = 12                      # int
    tmp.offset = 12                     # rodsLong_t
    tmp.specColl = create_specColl_t()  # specColl_t *

def test_subFile_t(s1, s2):
    return test_rodsHostAddr_t(s1.addr, s2.addr) and \
           s1.subFilePath == s2.subFilePath and \
           s1.mode == s2.mode and \
           s1.flags == s2.flags and \
           s1.offset == s2.offset and \
           test_specColl_t(s1.specColl, s2.specColl)

def create_subStructFileFdOprInp_t():
    tmp = subStructFileFdOprInp_t()
    init_rodsHostAddr_t(tmp.addr)   # rodsHostAddr_t
    tmp.type = HAAW_STRUCT_FILE_T   # structFileType_t
    tmp.fd = 12                     # int
    tmp.len = 12                    # int
    return tmp

def test_subStructFileFdOprInp_t(s1, s2):
    return test_rodsHostAddr_t(s1.addr, s2.addr) and \
           s1.type == s2.type and \
           s1.fd == s2.fd and \
           s1.len == s2.len

def create_subStructFileLseekInp_t():
    tmp = subStructFileLseekInp_t()
    init_rodsHostAddr_t(tmp.addr)    # rodsHostAddr_t
    tmp.type = HAAW_STRUCT_FILE_T    # structFileType_t
    tmp.fd = 12                      # int
    tmp.offset = 12                  # rodsLong_t
    tmp.whence = 12                  # int
    return tmp

def test_subStructFileLseekInp_t(s1, s2):
    return test_rodsHostAddr_t(s1.addr, s2.addr) and \
           s1.type == s2.type and \
           s1.fd == s2.fd and \
           s1.offset == s2.offset and \
           s1.whence == s2.whence

def create_subStructFileRenameInp_t():
    tmp = subStructFileRenameInp_t()
    init_subFile_t(tmp.subFile)             # subFile_t
    tmp.newSubFilePath = "newSubFilePath"   # char []
    return tmp

def test_subStructFileRenameInp_t(s1, s2):
    return test_subFile_t(s1.subFile, s2.subFile) and \
           s1.newSubFilePath == s2.newSubFilePath

def create_tagStruct_t():
    tmp = transferStat_t()
    tmp.len = 12
    #tmp.preTag        # char **
    #tmp.postTag        # char **
    #tmp.keyWord        # char **
    return tmp

def test_tagStruct_t(t1, t2):
    return t1.len == t2.len

def create_transferStat_t():
    tmp = transferStat_t()
    tmp.numThreads = 12             # int 
    tmp.flags = 12                  # int
    tmp.bytesWritten = 12           # rodsLong_t
    return tmp

def init_transferStat_t(tmp):
    tmp.numThreads = 12             # int 
    tmp.flags = 12                  # int
    tmp.bytesWritten = 12           # rodsLong_t

def test_transferStat_t(t1, t2):
    return t1.numThreads == t2.numThreads and \
           t1.flags == t2.flags and \
           t1.bytesWritten == t2.bytesWritten

def create_unregDataObj_t():
    tmp = unregDataObj_t()
    tmp.dataObjInfo = create_dataObjInfo_t()    # dataObjInfo_t * 
    tmp.condInput = create_keyValPair_t()       # keyValPair_t *
    return tmp

def test_unregDataObj_t(r1, r2):
    return test_dataObjInfo_t(r1.dataObjInfo, r2.dataObjInfo) and \
           test_keyValPair_t(r1.condInput, r2.condInput)

def create_userAdminInp_t():
    tmp = userAdminInp_t()
    tmp.arg0 = "arg0"             # char *
    tmp.arg1 = "arg1"             # char *
    tmp.arg2 = "arg2"             # char *
    tmp.arg3 = "arg3"             # char *
    tmp.arg4 = "arg4"             # char *
    tmp.arg5 = "arg5"             # char *
    tmp.arg6 = "arg6"             # char *
    tmp.arg7 = "arg7"             # char *
    tmp.arg8 = "arg8"             # char *
    tmp.arg9 = "arg9"             # char *
    return tmp

def test_userAdminInp_t(u1, u2):
    return u1.arg0 == u2.arg0 and \
           u1.arg1 == u2.arg1 and \
           u1.arg2 == u2.arg2 and \
           u1.arg3 == u2.arg3 and \
           u1.arg4 == u2.arg4 and \
           u1.arg5 == u2.arg5 and \
           u1.arg6 == u2.arg6 and \
           u1.arg7 == u2.arg7 and \
           u1.arg8 == u2.arg8 and \
           u1.arg9 == u2.arg9

def create_userInfo_t():
    tmp = userInfo_t()
    tmp.userName = "userName"                       # char []
    tmp.rodsZone = "rodsZone"                       # char []
    tmp.userType = "userType"                       # char []
    tmp.sysUid = 12                                 # int
    tmp.authInfo = create_authInfo_t()              # authInfo_t
    tmp.userOtherInfo = create_userOtherInfo_t()    #  userOtherInfo_t
    return tmp

def init_userInfo_t(tmp):
    tmp.userName = "userName"                       # char []
    tmp.rodsZone = "rodsZone"                       # char []
    tmp.userType = "userType"                       # char []
    tmp.sysUid = 12                                 # int
    tmp.authInfo = create_authInfo_t()              # authInfo_t
    tmp.userOtherInfo = create_userOtherInfo_t()    #  userOtherInfo_t

def test_userInfo_t(u1, u2):
    return u1.userName == u2.userName and \
           u1.rodsZone == u2.rodsZone and \
           u1.userType == u2.userType and \
           u1.sysUid == u2.sysUid and \
           test_authInfo_t(u1.authInfo, u2.authInfo) and \
           test_userOtherInfo_t(u1.userOtherInfo, u2.userOtherInfo)

def create_userOtherInfo_t():
    tmp = userOtherInfo_t()
    tmp.userInfo = "userInfo"               # char []
    tmp.userComments = "userComments"       # char []
    tmp.userCreate = "userCreate"           # char []
    tmp.userModify = "userModify"           # char []
    return tmp

def test_userOtherInfo_t(u1, u2):
    return u1.userInfo == u2.userInfo and \
           u1.userComments == u2.userComments and \
           u1.userCreate == u2.userCreate and \
           u1.userModify == u2.userModify

def create_version_t():
    tmp = version_t()
    tmp.status = 12                     # int
    tmp.relVersion = "relVersion"       # char []
    tmp.apiVersion = "apiVersion"       # char []
    tmp.reconnPort = 12                 # int
    tmp.reconnAddr = "reconnAddr"       # char []
    tmp.cookie = 12                     # int
    return tmp

def test_version_t(v1, v2):
    return v1.status == v2.status and \
           v1.relVersion == v2.relVersion and \
           v1.apiVersion == v2.apiVersion and \
           v1.reconnPort == v2.reconnPort and \
           v1.reconnAddr == v2.reconnAddr and \
           v1.cookie == v2.cookie

def create_xmsgTicketInfo_t():
    tmp = xmsgTicketInfo_t()
    tmp.sendTicket = 12     # unsigned int 
    tmp.rcvTicket = 12      # unsigned int 
    tmp.expireTime = 12     # unsigned int 
    tmp.flag = 12           # unsigned int 
    return tmp

def init_xmsgTicketInfo_t(tmp):
    tmp.sendTicket = 12     # unsigned int 
    tmp.rcvTicket = 12      # unsigned int 
    tmp.expireTime = 12     # unsigned int 
    tmp.flag = 12           # unsigned int

def test_xmsgTicketInfo_t(v1, v2):
    return v1.sendTicket == v2.sendTicket and \
           v1.rcvTicket == v2.rcvTicket and \
           v1.expireTime == v2.expireTime and \
           v1.flag == v2.flag
