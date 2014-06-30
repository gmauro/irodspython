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

typedef struct GeneralUpdateInp {
   int type;
   inxValPair_t values;
} generalUpdateInp_t;


%extend GeneralUpdateInp {
    ~GeneralUpdateInp() {
        if ($self) {
            clearInxVal(&$self->values);
            free($self);
        }
    }
}

%ignore GenQueryInp::condInput;
%ignore GenQueryInp::selectInp;
%ignore GenQueryInp::sqlCondInp;

typedef struct GenQueryInp {
    int maxRows; 
    int continueInx; 
    int rowOffset;
    int options;
    keyValPair_t condInput;
    inxIvalPair_t selectInp; 
    inxValPair_t sqlCondInp; 
} genQueryInp_t;

%extend GenQueryInp {
    ~GenQueryInp() {
        if ($self) {
            clearGenQueryInp($self);
            free($self);
        }
    }
    
    void initCondInput(char **keyWord, char **value, int len) {
        int i;
        clearKeyVal(&$self->condInput);
        for (i=0 ; i<len ; i++) {
            addKeyVal(&$self->condInput, keyWord[i], value[i]);
        }
    }
    
    void addCondInput(char *kw, char * value) {
        addKeyVal(&$self->condInput, kw, value);
    }
    
    void setCondInput(keyValPair_t *keyValPair) {
        clearKeyVal(&$self->condInput);
        if (keyValPair != NULL) {
            for (int i = 0 ; i < keyValPair->len ; i++) {
                addKeyVal(&$self->condInput,
                          keyValPair->keyWord[i],
                          keyValPair->value[i]);
            }
        }
    }
    
    keyValPair_t * getCondInput() {
        return &$self->condInput;
    }
    
    void initSelectInp(int *inx, int *value, int len) {
        int i;
        clearInxIval(&$self->selectInp);
        for (i=0 ; i<len ; i++) {
            addInxIval(&$self->selectInp, inx[i], value[i]);
        }
    }
    
    void addSelectInp(int inx, int value) {
        addInxIval(&$self->selectInp, inx, value);
    }
    
    void setSelectInp(inxIvalPair_t *inxIvalPair) {
        clearInxIval(&$self->selectInp);
        if (inxIvalPair != NULL) {
            for (int i = 0 ; i < inxIvalPair->len ; i++) {
                addInxIval(&$self->selectInp,
                          inxIvalPair->inx[i],
                          inxIvalPair->value[i]);
            }
        }
    }
    
    inxIvalPair_t * getSelectInp() {
        return &$self->selectInp;
    }
    
    void initSqlCondInp(int *inx, char **value, int len) {
        int i;
        clearInxVal(&$self->sqlCondInp);
        for (i=0 ; i<len ; i++) {
            addInxVal(&$self->sqlCondInp, inx[i], value[i]);
        }
    }
    
    void addSqlCondInp(int inx, char * value) {
        addInxVal(&$self->sqlCondInp, inx, value);
    }
    
    void setSqlCondInp(inxValPair_t *inxValPair) {
        clearInxVal(&$self->sqlCondInp);
        if (inxValPair != NULL) {
            for (int i = 0 ; i < inxValPair->len ; i++) {
                addInxVal(&$self->sqlCondInp,
                          inxValPair->inx[i],
                          inxValPair->value[i]);
            }
        }
    }
    
    inxValPair_t * getSqlCondInp() {
        return &$self->sqlCondInp;
    }
}

%{
void clear_GenQueryInp(genQueryInp_t * genQueryInp) {
    if (genQueryInp) {
        clearGenQueryInp(genQueryInp);
    }
}
%}

typedef struct GenQueryOut {
    int rowCnt;
    int attriCnt;
    int continueInx;
    int totalRowCount; 
    sqlResult_t sqlResult[MAX_SQL_ATTR]; 
} genQueryOut_t; 

%extend GenQueryOut {

    ~GenQueryOut() {
        if ($self) {
            freeGenQueryOut(&$self);
            free($self);
        }
    }

    void release() {
        freeGenQueryOut(&$self);
    }

    PyObject * getSqlResult() {
  		int i;
  		PyObject *l = PyList_New($self->rowCnt);
 		for (i = 0; i < $self->rowCnt; i++) {
      		PyObject *o = SWIG_NewPointerObj(SWIG_as_voidptr(&$self->sqlResult[i]), SWIGTYPE_p_SqlResult, 0 |  0 );
    		PyList_SetItem(l, i, o);
  		}
   		return l;
    }
        
    PyObject * getSqlResultIdx(int idx) {
    	if ($self->attriCnt == 1) {
			char *tResult;
			tResult = $self->sqlResult[0].value;
			tResult += idx * $self->sqlResult[0].len;
			return Py_BuildValue("s", tResult);
		} else {
			int a;
			PyObject *tuple = PyTuple_New($self->attriCnt);
    		for ( a = 0 ; a < $self->attriCnt ; a++ ) {
				char *tResult;
				tResult = $self->sqlResult[a].value;
				tResult += idx * $self->sqlResult[a].len;
				
				PyTuple_SetItem(tuple, a, Py_BuildValue("s", tResult));
			}    	
			return tuple;
		}
    }    
    
    
    PyObject * getSqlResultByInxIdx(int inx, int idx) {
		sqlResult_t *rescName = getSqlResultByInx($self, inx);
		char *tResult;
		tResult = rescName[0].value;
		tResult += idx * rescName[0].len;
		return Py_BuildValue("s", tResult);
    }

}

typedef struct {
   char *sql;
   char *arg1;
   char *arg2;
   char *arg3;
   char *arg4;
   int control;
   int form;
   int maxBufSize;
} simpleQueryInp_t;

%extend simpleQueryInp_t {

    ~simpleQueryInp_t() {
        if ($self) {
            free($self->sql);
            free($self->arg1);
            free($self->arg2);
            free($self->arg3);
            free($self->arg4);
            free($self);
        }
    }

};

typedef struct {
   int control;
   char *outBuf;
} simpleQueryOut_t;

%extend simpleQueryOut_t {

    ~simpleQueryOut_t() {
        if ($self) {
            free($self->outBuf);
            free($self);
        }
    }

};


typedef struct SqlResult {
    int attriInx;
    int len;
    char *value;
} sqlResult_t;

%extend SqlResult {

    ~SqlResult() {
        if ($self) {
            free($self->value);
            free($self);
        }
    }

};

%{
void clear_SqlResult(sqlResult_t * sqlResult) {
    if (sqlResult)
        free(sqlResult->value);
}
%}

/*****************************************************************************/

int rcGeneralUpdate (rcComm_t *conn, generalUpdateInp_t *generalUpdateInp);

/*****************************************************************************/

%inline %{
genQueryOut_t * rcGenQuery(rcComm_t *conn, genQueryInp_t *genQueryInp) {
    genQueryOut_t *genQueryOut = NULL;
    rcGenQuery(conn, genQueryInp, &genQueryOut);
    return genQueryOut;
}
%}

/*****************************************************************************/

%inline %{
genQueryOut_t * rcQuerySpecColl(rcComm_t *conn, dataObjInp_t *querySpecCollInp) {
    genQueryOut_t *genQueryOut = NULL;
    rcQuerySpecColl(conn, querySpecCollInp, &genQueryOut);
    return genQueryOut;
}
%}

/*****************************************************************************/

%inline %{
simpleQueryOut_t * rcSimpleQuery(rcComm_t *conn, simpleQueryInp_t *simpleQueryInp) {
    simpleQueryOut_t *simpleQueryOut = NULL;
    rcSimpleQuery(conn, simpleQueryInp, &simpleQueryOut);
    return simpleQueryOut;
}
%}

/*****************************************************************************/
