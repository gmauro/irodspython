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

typedef struct DataObjInfo {
    char objPath[MAX_NAME_LEN];
    char rescName[NAME_LEN];
    char rescGroupName[NAME_LEN];
    char dataType[NAME_LEN];
    rodsLong_t dataSize;
    char chksum[NAME_LEN];
    char version[NAME_LEN];
    char filePath[MAX_NAME_LEN];
    rescInfo_t *rescInfo;
    char dataOwnerName[NAME_LEN];
    char dataOwnerZone[NAME_LEN];
    int  replNum;
    int  replStatus;
    char statusString[NAME_LEN];
    rodsLong_t  dataId;
    rodsLong_t  collId;
    int  dataMapId;
    int flags;
    char dataComments[LONG_NAME_LEN];
    char dataMode[SHORT_STR_LEN];
    char dataExpiry[TIME_LEN];
    char dataCreate[TIME_LEN];
    char dataModify[TIME_LEN];
    char dataAccess[NAME_LEN];
    int  dataAccessInx;
    int  writeFlag;
    char destRescName[NAME_LEN];
    char backupRescName[NAME_LEN];
    char subPath[MAX_NAME_LEN];
    specColl_t *specColl;
    int regUid;
    int otherFlags;
    keyValPair_t condInput;
    struct DataObjInfo *next;
} dataObjInfo_t;

%extend DataObjInfo {
    ~DataObjInfo() {
        if ($self) {
            free($self->rescInfo);
            delete_SpecColl($self->specColl);
            delete_DataObjInfo($self->next);
            clearKeyVal(&$self->condInput);
            free($self);
       }
    }
}


typedef struct MiscSvrInfo {
    int serverType;
    unsigned int serverBootTime;
    char relVersion[NAME_LEN];
    char apiVersion[NAME_LEN];
    char rodsZone[NAME_LEN];
} miscSvrInfo_t;

typedef struct rodsObjStat {
    rodsLong_t          objSize;
    objType_t           objType;
    unsigned int        dataMode;
    char                dataId[NAME_LEN];
    char                chksum[NAME_LEN];
    char                ownerName[NAME_LEN];
    char                ownerZone[NAME_LEN];
    char                createTime[TIME_LEN];
    char                modifyTime[TIME_LEN];
    specColl_t          *specColl;
} rodsObjStat_t;

%extend rodsObjStat {

    ~rodsObjStat() {
        if ($self != NULL) {
            delete_SpecColl($self->specColl);
            free($self);
        }
    }

};


%{
int MyClearTagStruct(tagStruct_t *tag)
{
    int i;

    if (tag == NULL || tag->len <= 0)
		return (0);

    for (i = 0; i < tag->len; i++) {
		free(tag->preTag[i]);
		free(tag->postTag[i]);
		free(tag->keyWord[i]);
    }
	
	free(tag->preTag);
	free(tag->postTag);
	free(tag->keyWord);    
	memset(tag, 0, sizeof (tagStruct_t));
    return(0);
}

%}

%ignore TagStruct::preTag;
%ignore TagStruct::postTag;
%ignore TagStruct::keyWord;

typedef struct TagStruct {
    int len;
    char **preTag;
    char **postTag;
    char **keyWord;
} tagStruct_t;


%extend TagStruct {
    
    ~TagStruct() {
        if ($self) {
            MyClearTagStruct($self);
            free($self);
           }
       }
    
    
    char ** getPreTag(size_t *len) {
        *len = $self->len;
        return $self->preTag;
    }
    
    char * getPreTag(int n) {
        if ( (n >=0) && (n < $self->len) ) {
            char * tag = $self->preTag[n];
            return tag;
        } else
            return NULL;
    }

    char * getPostTag(int n) {
        if ( (n >=0) && (n < $self->len) )
            return $self->postTag[n];
        else
            return NULL;
    }
    
    char ** getPostTag(size_t *len) {
        *len = $self->len;
        return $self->postTag;
    }
    
    char ** getKeyWord(size_t *len) {
        *len = $self->len;
        return $self->keyWord;
    }

    char * getKeyWord(int n) {
        if ( (n >=0) && (n < $self->len) )
            return $self->keyWord[n];
        else
            return NULL;
    }

}
    


typedef enum {
    NO_SPEC_COLL,
    STRUCT_FILE_COLL,
    MOUNTED_COLL,
    LINKED_COLL
} specCollClass_t;

typedef enum {
    HAAW_STRUCT_FILE_T,
    TAR_STRUCT_FILE_T, 
    MSSO_STRUCT_FILE_T 
} structFileType_t;

typedef struct SpecColl {
    specCollClass_t collClass;
    structFileType_t type;
    char collection[MAX_NAME_LEN];
    char objPath[MAX_NAME_LEN];
    char resource[NAME_LEN];
    char phyPath[MAX_NAME_LEN];
    char cacheDir[MAX_NAME_LEN];
    int cacheDirty; 
    int replNum;
} specColl_t;

%extend SpecColl {

    ~SpecColl() {
        if ($self != NULL) {
            free($self);
        }
    }

};

typedef struct Subfile {
    rodsHostAddr_t addr;
    char subFilePath[MAX_NAME_LEN];
    int mode;
    int flags;
    rodsLong_t offset;
    specColl_t *specColl;
} subFile_t;

%extend Subfile {
    ~Subfile() {
        if ($self) {
            delete_SpecColl($self->specColl);
            free($self);
        }
    }
}

%{
void clear_Subfile(subFile_t * subFile) {
    if (subFile) {
            delete_SpecColl(subFile->specColl);
        }
}
%}

/*****************************************************************************/

%ignore KeyValPair::keyWord;
%ignore KeyValPair::value;
%ignore KeyValPair::len;

typedef struct KeyValPair {
    int len;
    char **keyWord;
    char **value;
} keyValPair_t;

%extend KeyValPair {

    ~KeyValPair() {
        if ($self) {
            clearKeyVal($self);
            free($self);
           }
       }
    
    void init(char **keyWord, char **value, int len) {
        int i;
        clearKeyVal($self);
        memset ($self, 0, sizeof(keyValPair_t));
        for (i=0 ; i<len ; i++) {
            addKeyVal($self, keyWord[i], value[i]);
        }
    }
    
    int getLen() {
        return $self->len;
    }
    
    char ** getKeyWords(size_t *len) {
        *len = $self->len;
        return $self->keyWord;
    }
    
    char * getKeyWord(int n) {
        if ( (n >=0) && (n < $self->len) )
            return $self->keyWord[n];
        else
            return NULL;
    }
    
    char ** getValues(size_t *len) {
        *len = $self->len;
        return $self->value;
    }
    
    char * getValue(int n) {
        if ( (n >=0) && (n < $self->len) )
            return $self->value[n];
        else
            return NULL;
    }
    
    void clear() {
        clearKeyVal($self);
    }

    int add(char *keyWord, char *value) {
        return addKeyVal($self, keyWord, value);
    }

    char * getValByKey(char *keyWord) {
        return getValByKey($self, keyWord);
    }

    PyObject * __str__() {
        char str[1024];
        strcpy (str,"keyValPair_t:\n");
        for (int i = 0 ; i < $self->len ; i ++) {
            char tmp[1024];
            sprintf(tmp, " %s - %s\n", $self->keyWord[i], $self->value[i]); 
            strcat(str, tmp);
        }
        return  Py_BuildValue("s", str);
    }

}



/*****************************************************************************/


%ignore InxIvalPair::inx;
%ignore InxIvalPair::value;
%ignore InxIvalPair::len;

typedef struct InxIvalPair {
    int len;
    int *inx;
    int *value;
} inxIvalPair_t;


%extend InxIvalPair {
   
   ~InxIvalPair() {
        if ($self != NULL) {
            clearInxIval($self);
            free($self);
        }
   }
    
    void init(int *inx, int *value, int len) {
        int i;
        clearInxIval($self);
        memset ($self, 0, sizeof(inxIvalPair_t));
        for (i=0 ; i<len ; i++) {
            addInxIval($self, inx[i], value[i]);
        }
    }

    void clear() {
        clearInxIval($self);
    }

   int getLen() {
        return $self->len;
   }
    
   int * getInx(size_t *len) {
        *len = $self->len;
        return $self->inx;
   }
    
    int * getValue(size_t *len) {
        *len = $self->len;
        return $self->value;
    }

    int add(int inx, int value) {
        return addInxIval($self, inx, value);
    }

    int getIvalByInx(int inx) {
        int out_value = 0;
        getIvalByInx($self, inx, &out_value);
        return out_value;
    }

    PyObject * __str__() {
        char str[1024];
        strcpy (str,"inxIValPair_t:\n");
        for (int i = 0 ; i < $self->len ; i ++) {
            char tmp[1024];
            sprintf(tmp, " %d - %d\n", $self->inx[i], $self->value[i]); 
            strcat(str, tmp);
        }
        return  Py_BuildValue("s", str);
    }
}


/*****************************************************************************/

%ignore InxValPair::inx;
%ignore InxValPair::value;
%ignore InxValPair::len;

typedef struct InxValPair {
    int len;
    int *inx;
    char **value;
} inxValPair_t;

%extend InxValPair {

    ~InxValPair() {
        if ($self != NULL) {
            clearInxVal($self);
            free($self);
        }
    }
    
    void init(int *inx, char **value, int len) {
        int i;
        clearInxVal($self);
        memset ($self, 0, sizeof(inxValPair_t));
        for (i=0 ; i<len ; i++) {
            addInxVal($self, inx[i], value[i]);
        }
    }
    
    void clear() {
        clearInxVal($self);
    }
    
   int getLen() {
        return $self->len;
   }
    
   int * getInx(size_t *len) {
        *len = $self->len;
        return $self->inx;
   }
    
    char ** getValue(size_t *len) {
        *len = $self->len;
        return $self->value;
    }

    int add(int inx, char *value) {
        return addInxVal($self, inx, value);
    }

    char * getValByInx(int inx) {
        return getValByInx($self, inx);
    }

    PyObject * __str__() {
        char str[1024];
        strcpy (str,"inxValPair_t:\n");
        for (int i = 0 ; i < $self->len ; i ++) {
            char tmp[1024];
            sprintf(tmp, " %d - %s\n", $self->inx[i], $self->value[i]); 
            strcat(str, tmp);
        }
        return  Py_BuildValue("s", str);
    }

}


typedef struct RescInfo
{
    char rescName[NAME_LEN];
    rodsLong_t rescId;
    char zoneName[NAME_LEN];
    char rescLoc[NAME_LEN];
    char rescType[NAME_LEN];
    int rescTypeInx;
    int rescClassInx;
    int rescStatus;
    int paraOpr;
    char rescClass[NAME_LEN];
    char rescVaultPath[MAX_NAME_LEN];
    char rescInfo[LONG_NAME_LEN];
    char rescComments[LONG_NAME_LEN];
    char gateWayAddr[NAME_LEN];
    rodsLong_t rescMaxObjSize;
    rodsLong_t freeSpace;
    char freeSpaceTimeStamp[TIME_LEN];
    time_t freeSpaceTime;
    char rescCreate[TIME_LEN];
    char rescModify[TIME_LEN];
    void *rodsServerHost;
    rodsLong_t quotaLimit;
    rodsLong_t quotaOverrun;
} rescInfo_t;


/*****************************************************************************/

%inline %{
miscSvrInfo_t * rcGetMiscSvrInfo(rcComm_t *conn) {
    miscSvrInfo_t * outSvrInfo = NULL;
    rcGetMiscSvrInfo(conn, &outSvrInfo);
    return outSvrInfo;
}
%}

/*****************************************************************************/

%inline %{
rodsObjStat_t * rcObjStat(rcComm_t *conn, dataObjInp_t *dataObjInp) {
    rodsObjStat_t * rodsObjStatOut = NULL;
    rcObjStat(conn, dataObjInp, &rodsObjStatOut);
    return rodsObjStatOut;
}
%}

/*****************************************************************************/