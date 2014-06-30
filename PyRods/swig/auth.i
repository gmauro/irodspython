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

typedef struct {
   char *challenge;
   char *response;
   char *username;
} authCheckInp_t;

%extend authCheckInp_t {
    ~authCheckInp_t() {
        if ($self) {
            free($self->challenge);
            free($self->response);
            free($self->username);
            free($self);
       }
       
   }
};

typedef struct {
   int  privLevel;
   int  clientPrivLevel;
   char *serverResponse;
} authCheckOut_t;

%extend authCheckOut_t {
    ~authCheckOut_t() {
        if ($self != NULL) {
            free($self->serverResponse);
            free($self);
       }
       
   }
};

typedef struct {
   char *response;
   char *username;
} authResponseInp_t;

%extend authResponseInp_t {
    ~authResponseInp_t() {
        if ($self) {
            free($self->response);
            free($self->username);
            free($self);
       }
       
   }
};

typedef struct {
   char *challenge;
} authRequestOut_t;

%extend authRequestOut_t {
    ~authRequestOut_t() {
        if ($self) {
            free($self->challenge);
            free($self);
       }
       
   }
};

typedef struct {
   char *serverDN;
} gsiAuthRequestOut_t;

%extend gsiAuthRequestOut_t {
    ~gsiAuthRequestOut_t() {
        if ($self) {
            free($self->serverDN);
            free($self);
       }
       
   }
};

/*****************************************************************************/

%inline %{
PyObject * rcAuthCheck(rcComm_t *conn, authCheckInp_t *authCheckInp) {
    authCheckOut_t *authCheckOut = NULL;
    int status = rcAuthCheck(conn, authCheckInp, &authCheckOut);
    return Py_BuildValue("(iO)", 
                         status, 
                         SWIG_NewPointerObj(SWIG_as_voidptr(authCheckOut), 
                                            SWIGTYPE_p_authCheckOut_t, 0 |  0 ));
}
%}

/*****************************************************************************/

%inline %{
PyObject * rcAuthRequest(rcComm_t *conn) {
    authRequestOut_t *authReqOut = NULL;
    int status = rcAuthRequest(conn, &authReqOut);
    return Py_BuildValue("(iO)", 
                         status, 
                         SWIG_NewPointerObj(SWIG_as_voidptr(authReqOut), 
                                            SWIGTYPE_p_authRequestOut_t, 0 |  0 ));
}
%}

/*****************************************************************************/

int rcAuthResponse(rcComm_t *conn, authResponseInp_t *authResponseInp );

/*****************************************************************************/

%inline %{
PyObject * rcGsiAuthRequest(rcComm_t *conn) {
    gsiAuthRequestOut_t *gsiAuthRequestOut = NULL;
    int status = rcGsiAuthRequest(conn, &gsiAuthRequestOut);
    return Py_BuildValue("(iO)", 
                         status, 
                         SWIG_NewPointerObj(SWIG_as_voidptr(gsiAuthRequestOut), 
                                            SWIGTYPE_p_gsiAuthRequestOut_t, 0 |  0 ));
}
%}

/*****************************************************************************/
