/* Copyright (c) 2013, University of Liverpool
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 *
 * Author       : Jerome Fuselier
 */
 
 %{

#include "authCheck.h"
#include "authRequest.h"
#include "authResponse.h"
#include "gsiAuthRequest.h"
#include "chkObjPermAndStat.h"
#include "dataCopy.h"
#include "dataGet.h"
#include "dataPut.h"
#include "dataObjChksum.h"
#include "dataObjClose.h"
#include "dataObjCreate.h"
#include "dataObjCreateAndStat.h"
#include "dataObjFsync.h"
#include "dataObjGet.h"
#include "dataObjInpOut.h"
#include "dataObjLock.h"
#include "dataObjLseek.h"
#include "dataObjOpen.h"
#include "dataObjOpenAndStat.h"
#include "dataObjPhymv.h"
#include "dataObjPut.h"
#include "dataObjRead.h"
#include "dataObjRename.h"
#include "dataObjRepl.h"
#include "dataObjRsync.h"
#include "dataObjTrim.h"
#include "dataObjTruncate.h"
#include "dataObjUnlink.h"
#include "dataObjWrite.h"
#include "getRodsEnv.h"
#include "miscUtil.h"
#include "getRemoteZoneResc.h"
#include "getTempPassword.h"
#include "rmColl.h"
#include "userAdmin.h"
#include "generalAdmin.h"
#include "rodsDef.h"
#include "rodsErrorTable.h"
#include "execMyRule.h"
#include "ruleExecDel.h"
#include "ruleExecMod.h"
#include "ruleExecSubmit.h"
#include "fileChmod.h"
#include "fileChksum.h"
#include "fileClose.h"
#include "fileClosedir.h"
#include "fileCreate.h"
#include "fileFstat.h"
#include "fileFsync.h"
#include "fileGet.h"
#include "fileGetFsFreeSpace.h"
#include "fileLseek.h"
#include "fileMkdir.h"
#include "fileOpen.h"
#include "fileOpendir.h"
#include "filePut.h"
#include "fileRead.h"
#include "fileReaddir.h"
#include "fileRename.h"
#include "fileRmdir.h"
#include "fileOpen.h"
#include "fileStage.h"
#include "fileStat.h"
#include "fileTruncate.h"
#include "fileUnlink.h"
#include "fileWrite.h"
#include "l3FileGetSingleBuf.h"
#include "l3FilePutSingleBuf.h"
#include "getMiscSvrInfo.h"
#include "objStat.h"
#include "closeCollection.h"
#include "collCreate.h"
#include "collRepl.h"
#include "modColl.h"
#include "openCollection.h"
#include "phyPathReg.h"
#include "readCollection.h"
#include "regDataObj.h"
#include "regColl.h"
#include "regReplica.h"
#include "syncMountedColl.h"
#include "unregDataObj.h"
#include "rodsKeyWdDef.h"
#include "modAVUMetadata.h"
#include "modDataObjMeta.h"
#include "rodsPath.h"
#include "generalUpdate.h"
#include "querySpecColl.h"
#include "rodsGenQuery.h"
#include "simpleQuery.h"
#include "structFileBundle.h"
#include "structFileExtract.h"
#include "subStructFileClose.h"
#include "subStructFileClosedir.h"
#include "subStructFileCreate.h"
#include "subStructFileFstat.h"
#include "subStructFileGet.h"
#include "subStructFileLseek.h"
#include "subStructFileMkdir.h"
#include "subStructFileOpen.h"
#include "subStructFileOpendir.h"
#include "subStructFilePut.h"
#include "subStructFileReaddir.h"
#include "subStructFileRename.h"
#include "subStructFileRmdir.h"
#include "subStructFileTruncate.h"
#include "subStructFileUnlink.h"
#include "subStructFileWrite.h"
#include "getXmsgTicket.h"
#include "rcvXmsg.h"
#include "sendXmsg.h"
#include "stringOpr.h"





// Add destructor signatures so they can be used by any other destructors

SWIGINTERN void delete_authCheckInp_t(authCheckInp_t *self);
SWIGINTERN void delete_authCheckOut_t(authCheckOut_t *self);
SWIGINTERN void delete_authResponseInp_t(authResponseInp_t *self);
SWIGINTERN void delete_authRequestOut_t(authRequestOut_t *self);
SWIGINTERN void delete_BytesBuf(struct BytesBuf *self);
SWIGINTERN void delete_chkObjPermAndStat_t(chkObjPermAndStat_t *self);
SWIGINTERN void delete_CollEnt(struct CollEnt *self);
SWIGINTERN void delete_CollHandle(struct CollHandle *self);
SWIGINTERN void delete_CollInp(struct CollInp *self);
SWIGINTERN void delete_DataObjInfo(struct DataObjInfo *self);
SWIGINTERN void delete_DataObjInp(struct DataObjInp *self);
SWIGINTERN void delete_DataOprInp(struct DataOprInp *self);
SWIGINTERN void delete_ExecCmd(struct ExecCmd *self);
SWIGINTERN void delete_ExecMyRuleInp(struct ExecMyRuleInp *self);
SWIGINTERN void delete_fileMkdirInp_t(fileMkdirInp_t *self);
SWIGINTERN void delete_fileOpenInp_t(fileOpenInp_t *self);
SWIGINTERN void delete_generalAdminInp_t(generalAdminInp_t *self);
SWIGINTERN void delete_GenQueryInp(struct GenQueryInp *self);
SWIGINTERN void delete_GenQueryOut(struct GenQueryOut *self);
SWIGINTERN void delete_gsiAuthRequestOut_t(gsiAuthRequestOut_t *self);
SWIGINTERN void delete_InxIvalPair(struct InxIvalPair *self);
SWIGINTERN void delete_InxValPair(struct InxValPair *self);
SWIGINTERN void delete_KeyValPair(struct KeyValPair *self);
SWIGINTERN void delete_modAccessControlInp_t(modAccessControlInp_t *self);
SWIGINTERN void delete_modAVUMetadataInp_t(modAVUMetadataInp_t *self);
SWIGINTERN void delete_modDataObjMeta_t(modDataObjMeta_t *self);
SWIGINTERN void delete_MsParam(struct MsParam *self);
SWIGINTERN void delete_MsParamArray(struct MsParamArray *self);
SWIGINTERN void delete_OpenedDataObjInp(struct OpenedDataObjInp *self);
SWIGINTERN void delete_QueryHandle(struct QueryHandle *self);
SWIGINTERN void delete_rcComm_t(rcComm_t *self);
SWIGINTERN void delete_RcvXmsgOut(struct RcvXmsgOut *self);
SWIGINTERN void delete_regReplica_t(regReplica_t *self);
SWIGINTERN void delete_rodsArguments_t(rodsArguments_t *self);
SWIGINTERN void delete_rodsEnv(rodsEnv *self);
SWIGINTERN void delete_rodsObjStat(struct rodsObjStat *self);
SWIGINTERN void delete_RodsPath(struct RodsPath *self);
SWIGINTERN void delete_RodsPathInp(struct RodsPathInp *self);
SWIGINTERN void delete_ruleExecModInp_t(ruleExecModInp_t *self);
SWIGINTERN void delete_ruleExecSubmitInp_t(ruleExecSubmitInp_t *self);
SWIGINTERN void delete_SendXmsgInfo(struct SendXmsgInfo *self);
SWIGINTERN void delete_simpleQueryInp_t(simpleQueryInp_t *self);
SWIGINTERN void delete_simpleQueryOut_t(simpleQueryOut_t *self);
SWIGINTERN void delete_SpecColl(struct SpecColl *self);
SWIGINTERN void delete_SqlResult(struct SqlResult *self);
SWIGINTERN void delete_StructFileExtAndRegInp(struct StructFileExtAndRegInp *self);
SWIGINTERN void delete_StructFileOprInp(struct StructFileOprInp *self);
SWIGINTERN void delete_Subfile(struct Subfile *self);
SWIGINTERN void delete_unregDataObj_t(unregDataObj_t *self);
SWIGINTERN void delete_userAdminInp_t(userAdminInp_t *self);

void clear_BytesBuf(bytesBuf_t * bytesBuf);
void clear_CollSqlResult(collSqlResult_t * collSqlResult);
void clear_DataObjInp(dataObjInp_t * dataObjInp);
void clear_DataOprInp(dataOprInp_t * dataOprInp);
void clear_DataObjSqlResult(dataObjSqlResult_t * dataObjSqlResult);
void clear_GenQueryInp(genQueryInp_t * genQueryInp);
void clear_InxIvalPair(inxIvalPair_t * inxIvalPair);
void clear_InxValPair(inxValPair_t * inxValPair);
void clear_KeyValPair(keyValPair_t * keyValPair);
void clear_QueryHandle(queryHandle_t * queryHandle);
void clear_SendXmsgInfo(sendXmsgInfo_t * sendXmsgInfo);
void clear_SqlResult(sqlResult_t * sqlResult);
void clear_Subfile(subFile_t * subFile);

%}
