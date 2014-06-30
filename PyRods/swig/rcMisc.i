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

/*****************************************************************************/

int addInxIval (inxIvalPair_t *inxIvalPair, int inx, int value);

/*****************************************************************************/

int addInxVal (inxValPair_t *inxValPair, int inx, char *value);

/*****************************************************************************/

int addKeyVal (keyValPair_t *condInput, char *keyWord, char *value);

/*****************************************************************************/

int addTagStruct (tagStruct_t *condInput, char *preTag, char *postTag, 
char *keyWord);

/*****************************************************************************/

int chkStateForResume (rcComm_t *conn, rodsRestart_t *rodsRestart,
char *targPath, rodsArguments_t *rodsArgs, objType_t objType,
keyValPair_t *condInput, int deleteFlag);

/*****************************************************************************/

%inline %{
PyObject * getLocalTimeFromRodsTime(char *timeStrIn) {
    char localTime[TIME_LEN];
    getLocalTimeFromRodsTime(timeStrIn, localTime);
    return Py_BuildValue("s", localTime);
}
%}

/*****************************************************************************/

int getMountedSubPhyPath (char *logMountPoint, char *phyMountPoint, 
char *logSubPath, char *phySubPathOut);

/*****************************************************************************/

%inline %{
PyObject * getSpecCollTypeStr (specColl_t *specColl) {
    char * typeStr = (char *) malloc(NAME_LEN);
    getSpecCollTypeStr(specColl, typeStr);
    return Py_BuildValue("s", typeStr);
}
%}

/*****************************************************************************/

sqlResult_t * getSqlResultByInx (genQueryOut_t *genQueryOut, int attriInx);

/*****************************************************************************/

int openRestartFile (char *restartFile, rodsRestart_t *rodsRestart,
rodsArguments_t *rodsArgs);

/*****************************************************************************/

%inline %{
PyObject * parseUserName(char *fullUserNameIn) {
    char userName[NAME_LEN];
    char userZone[NAME_LEN];
    int status = parseUserName(fullUserNameIn, userName, userZone);
    return Py_BuildValue("(iss)", 
                         status, 
                         userName,
                         userZone);
}
%}

/*****************************************************************************/

int printError(rcComm_t *Conn, int status, char *routineName);

/*****************************************************************************/

int printErrorStack (rError_t *rError);

/*****************************************************************************/

void printReleaseInfo(char *cmdName);

/*****************************************************************************/

int procAndWrriteRestartFile (rodsRestart_t *rodsRestart, char *donePath);
%rename procAndWriteRestartFile procAndWrriteRestartFile;

/*****************************************************************************/


%inline %{
rodsHostAddr_t * rcGetRemoteZoneResc(rcComm_t *conn, dataObjInp_t *dataObjInp) {
    rodsHostAddr_t *rescAddr = NULL;
    rcGetRemoteZoneResc (conn, dataObjInp, &rescAddr);
    return rescAddr;
}
%}

/*****************************************************************************/

%inline %{
PyObject * rcGetTempPassword(rcComm_t *conn) {
    getTempPasswordOut_t *getTempPasswordOut = NULL;
    rcGetTempPassword(conn, &getTempPasswordOut);
    PyObject * ret = Py_BuildValue("s", getTempPasswordOut->stringToHashWith);
    if (getTempPasswordOut)
        free(getTempPasswordOut);
    return ret;
}
%}

/*****************************************************************************/

int rcRmColl (rcComm_t *conn, collInp_t *rmCollInp, int vFlag);

/*****************************************************************************/

int resolveSpecCollType (char *type, char *collection, char *collInfo1,
char *collInfo2, specColl_t *specColl);

/*****************************************************************************/

int setStateForRestart (rcComm_t *conn, rodsRestart_t *rodsRestart,
rodsPath_t *targPath, rodsArguments_t *rodsArgs);

/*****************************************************************************/