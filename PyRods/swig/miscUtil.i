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

typedef struct CollEnt {
    objType_t objType;
    int replNum;
    int replStatus;
    unsigned int dataMode;
    rodsLong_t dataSize;
    char *collName;
    char *dataName;
    char *dataId;
    char *createTime;
    char *modifyTime;
    char *chksum;
    char *resource;
    char *rescGrp;
    char *phyPath;
    char *ownerName;
    specColl_t specColl; 
} collEnt_t;

%extend CollEnt {

    ~CollEnt() {
        if ($self != NULL) {
            free($self->collName);
            free($self->dataName);
            free($self->dataId);
            free($self->createTime);
            free($self->modifyTime);
            free($self->chksum);
            free($self->resource);
            free($self->rescGrp);
            free($self->phyPath);
            free($self->ownerName);
            free($self);
        }
    }

};

typedef enum {
    COLL_CLOSED,
    COLL_OPENED,
    COLL_DATA_OBJ_QUERIED,
    COLL_COLL_OBJ_QUERIED
} collState_t;

typedef enum {
    RC_COMM,
    RS_COMM
} connType_t;

typedef struct CollHandle {
    collState_t state;
    int inuseFlag;
    int flags;
    int rowInx;
    rodsObjStat_t *rodsObjStat;
    queryHandle_t queryHandle;
    genQueryInp_t genQueryInp;
    dataObjInp_t dataObjInp;
    dataObjSqlResult_t dataObjSqlResult;
    collSqlResult_t collSqlResult;
    char linkedObjPath[MAX_NAME_LEN];
    char prevdataId[NAME_LEN];
} collHandle_t;

%extend CollHandle {

    ~CollHandle() {
        if ($self != NULL) {
            delete_rodsObjStat($self->rodsObjStat);
            clear_QueryHandle(&$self->queryHandle);
            clear_GenQueryInp(&$self->genQueryInp);
            clear_DataObjInp(&$self->dataObjInp);
            clear_DataObjSqlResult(&$self->dataObjSqlResult);
            clear_CollSqlResult(&$self->collSqlResult);
            free($self);
        }
    }

};

typedef struct CollSqlResult {
    int rowCnt;
    int attriCnt;
    int continueInx;
    int totalRowCount;
    sqlResult_t collName; 
    sqlResult_t collType; 
    sqlResult_t collInfo1; 
    sqlResult_t collInfo2;
    sqlResult_t collOwner;
    sqlResult_t collCreateTime;
    sqlResult_t collModifyTime;
} collSqlResult_t;

%extend CollSqlResult {
    ~CollSqlResult() {
        if ($self) {
            clear_SqlResult(&$self->collName);
            clear_SqlResult(&$self->collType);
            clear_SqlResult(&$self->collInfo1);
            clear_SqlResult(&$self->collInfo2);
            clear_SqlResult(&$self->collOwner);
            clear_SqlResult(&$self->collCreateTime);
            clear_SqlResult(&$self->collModifyTime);
            free($self);
       }
   }
};
%{
void clear_CollSqlResult(collSqlResult_t * collSqlResult) {
    if (collSqlResult) {
            clear_SqlResult(&collSqlResult->collName);
            clear_SqlResult(&collSqlResult->collType);
            clear_SqlResult(&collSqlResult->collInfo1);
            clear_SqlResult(&collSqlResult->collInfo2);
            clear_SqlResult(&collSqlResult->collOwner);
            clear_SqlResult(&collSqlResult->collCreateTime);
            clear_SqlResult(&collSqlResult->collModifyTime);
        }
}
%}

typedef struct DataObjSqlResult {
    int rowCnt;
    int attriCnt;
    int continueInx;
    int totalRowCount;
    sqlResult_t collName;
    sqlResult_t dataName;
    sqlResult_t dataMode;
    sqlResult_t dataSize;
    sqlResult_t createTime;
    sqlResult_t modifyTime;
    sqlResult_t chksum;
    sqlResult_t replStatus;
    sqlResult_t dataId;
    sqlResult_t resource;
    sqlResult_t phyPath;
    sqlResult_t ownerName;
    sqlResult_t replNum;
    sqlResult_t rescGrp;
    sqlResult_t dataType;
} dataObjSqlResult_t;

%extend DataObjSqlResult {
    ~DataObjSqlResult() {
        if ($self) {
            clear_SqlResult(&$self->collName);
            clear_SqlResult(&$self->dataName);
            clear_SqlResult(&$self->dataMode);
            clear_SqlResult(&$self->dataSize);
            clear_SqlResult(&$self->createTime);
            clear_SqlResult(&$self->modifyTime);
            clear_SqlResult(&$self->chksum);
            clear_SqlResult(&$self->replStatus);
            clear_SqlResult(&$self->dataId);
            clear_SqlResult(&$self->resource);
            clear_SqlResult(&$self->phyPath);
            clear_SqlResult(&$self->ownerName);
            clear_SqlResult(&$self->replNum);
            clear_SqlResult(&$self->rescGrp);
            clear_SqlResult(&$self->dataType);
            free($self);
       }
   }
};

%{
void clear_DataObjSqlResult(dataObjSqlResult_t * dataObjSqlResult) {
    if (dataObjSqlResult) {
            clear_SqlResult(&dataObjSqlResult->collName);
            clear_SqlResult(&dataObjSqlResult->dataName);
            clear_SqlResult(&dataObjSqlResult->dataMode);
            clear_SqlResult(&dataObjSqlResult->dataSize);
            clear_SqlResult(&dataObjSqlResult->createTime);
            clear_SqlResult(&dataObjSqlResult->modifyTime);
            clear_SqlResult(&dataObjSqlResult->chksum);
            clear_SqlResult(&dataObjSqlResult->replStatus);
            clear_SqlResult(&dataObjSqlResult->dataId);
            clear_SqlResult(&dataObjSqlResult->resource);
            clear_SqlResult(&dataObjSqlResult->phyPath);
            clear_SqlResult(&dataObjSqlResult->ownerName);
            clear_SqlResult(&dataObjSqlResult->replNum);
            clear_SqlResult(&dataObjSqlResult->rescGrp);
            clear_SqlResult(&dataObjSqlResult->dataType);
        }
}
%}

typedef struct QueryHandle {
    void *conn;
    connType_t connType;
    funcPtr querySpecColl;
    funcPtr genQuery;
} queryHandle_t;

%extend QueryHandle {

    ~QueryHandle() {
        if ($self) {
            if ($self->connType == RC_COMM) {
                delete_rcComm_t((rcComm_t*)$self->conn);
            } /*else {
                free($self->conn);
            }*/
            free($self);
        }
    }

    rcComm_t * get_rcComm() {
        return (rcComm_t *)$self->conn;
    }

};

%{
void clear_QueryHandle(queryHandle_t * queryHandle) {
    if (queryHandle) {
            if (queryHandle->connType == RC_COMM) {
                delete_rcComm_t((rcComm_t*)queryHandle->conn);
            } /*else {
                free(queryHandle->conn);
            }*/
        }
}
%}


/*****************************************************************************/

int getRodsObjType (rcComm_t *conn, rodsPath_t *rodsPath);

/*****************************************************************************/

int mkColl (rcComm_t *conn, char *collection);

/*****************************************************************************/

int mkCollR (rcComm_t *conn, char *startColl, char *destColl);

/*****************************************************************************/

int mkdirR (char *startDir, char *destDir, int mode);

/*****************************************************************************/

int myChmod (char *inPath, uint dataMode);

/*****************************************************************************/

%inline %{
PyObject * queryCollAcl(rcComm_t *conn, char *collName, char *zoneHint) {
    genQueryOut_t *genQueryOut = NULL;
    int status = queryCollAcl(conn, collName, zoneHint, &genQueryOut);
    return Py_BuildValue("(iO)", 
                         status, 
                         SWIG_NewPointerObj(SWIG_as_voidptr(genQueryOut), 
                                            SWIGTYPE_p_GenQueryOut, 0 |  0 ));
}
%}

/*****************************************************************************/

%inline %{
PyObject * queryCollAclSpecific(rcComm_t *conn, char *collName, 
                                char *zoneHint) {
    genQueryOut_t *genQueryOut = NULL;
    int status = queryCollAclSpecific (conn, collName, zoneHint, &genQueryOut);
    return Py_BuildValue("(iO)", 
                         status, 
                         SWIG_NewPointerObj(SWIG_as_voidptr(genQueryOut), 
                                            SWIGTYPE_p_GenQueryOut, 0 |  0 ));
}
%}

/*****************************************************************************/

%inline %{
PyObject * queryCollInColl(queryHandle_t *queryHandle, char *collection,
                           int flags, genQueryInp_t *genQueryInp) {
    genQueryOut_t *genQueryOut = NULL;
    int status = queryCollInColl(queryHandle, collection, flags, genQueryInp, &genQueryOut);
    return Py_BuildValue("(iO)", 
                         status, 
                         SWIG_NewPointerObj(SWIG_as_voidptr(genQueryOut), 
                                            SWIGTYPE_p_GenQueryOut, 0 |  0 ));
}
%}

/*****************************************************************************/

%inline %{
PyObject * queryCollInheritance(rcComm_t *conn, char *collName) {
    genQueryOut_t *genQueryOut = NULL;
    int status = queryCollInheritance(conn, collName, &genQueryOut);
    return Py_BuildValue("(iO)", 
                         status, 
                         SWIG_NewPointerObj(SWIG_as_voidptr(genQueryOut), 
                                            SWIGTYPE_p_GenQueryOut, 0 |  0 ));
}
%}

/*****************************************************************************/

%inline %{
PyObject * queryDataObjInColl(queryHandle_t *queryHandle, char *collection,
                                   int flags, genQueryInp_t *genQueryInp, 
                                   keyValPair_t *condInput) {
    genQueryOut_t *genQueryOut = NULL;
    int status = queryDataObjInColl(queryHandle, collection, flags, genQueryInp, 
                       &genQueryOut, condInput);
    return Py_BuildValue("(iO)", 
                         status, 
                         SWIG_NewPointerObj(SWIG_as_voidptr(genQueryOut), 
                                            SWIGTYPE_p_GenQueryOut, 0 |  0 ));
}
%}

/*****************************************************************************/

%inline %{
PyObject * queryDataObjAcl(rcComm_t *conn, char *dataId, char *zoneHint) {
    genQueryOut_t *genQueryOut = NULL;
    int status = queryDataObjAcl(conn, dataId, zoneHint, &genQueryOut);
    return Py_BuildValue("(iO)", 
                         status, 
                         SWIG_NewPointerObj(SWIG_as_voidptr(genQueryOut), 
                                            SWIGTYPE_p_GenQueryOut, 0 |  0 ));
}
%}

/*****************************************************************************/

int rclCloseCollection(collHandle_t *collHandle);

/*****************************************************************************/

int rclInitQueryHandle(queryHandle_t *queryHandle, rcComm_t *conn);

/*****************************************************************************/

int rclOpenCollection (rcComm_t *conn, char *collection, 
int flag, collHandle_t *collHandle);

%inline %{

PyObject * rclOpenCollection(rcComm_t *conn, char *collection, 
                                int flag) {
    collHandle_t * collHandle = (collHandle_t*) malloc(sizeof(collHandle_t));
    memset(collHandle, 0, sizeof(collHandle_t));
    int status;
    
    status = rclOpenCollection(conn, collection, flag, collHandle);
    return Py_BuildValue("(iO)", 
                         status, 
                         SWIG_NewPointerObj(SWIG_as_voidptr(collHandle), 
                                            SWIGTYPE_p_CollHandle, 0 |  0 ));
}

%}

/*****************************************************************************/

%inline %{
PyObject * rclReadCollection(rcComm_t *conn, collHandle_t *collHandle) {
    collEnt_t * collEnt = (collEnt_t*) malloc(sizeof(collEnt_t));
    memset(collEnt, 0, sizeof(collEnt_t));
    int status = rclReadCollection(conn, collHandle, collEnt);
    return Py_BuildValue("(iO)", 
                         status, 
                         SWIG_NewPointerObj(SWIG_as_voidptr(collEnt), 
                                            SWIGTYPE_p_CollEnt, 0 |  0 ));
}
%}

/*****************************************************************************/

int setQueryFlag(rodsArguments_t *rodsArgs);

/*****************************************************************************/

int setQueryInpForData(int flags, genQueryInp_t *genQueryInp);

/*****************************************************************************/
