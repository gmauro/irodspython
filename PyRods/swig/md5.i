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
  UINT4 state[4];
  UINT4 count[2];
  unsigned char buffer[64];
} MD5_CTX;

/**********************************************************************/

%extend MD5_CTX{

    void set_MD5_CTX_state(int idx, UINT4 el) {
        if ( (idx >= 0) && (idx < 4) ) {
            $self->state[idx] = el;
        }
    }
    
    UINT4 get_MD5_CTX_state(int idx) {
        if ( (idx >= 0) && (idx < 4) ) {
            return $self->state[idx];
        }
        return 0;
    }

    void set_MD5_CTX_count(int idx, UINT4 el) {
        if ( (idx >= 0) && (idx < 2) ) {
            $self->count[idx] = el;
        }
    }
    
    UINT4 get_MD5_CTX_count(int idx) {
        if ( (idx >= 0) && (idx < 2) ) {
            return $self->count[idx];
        }
        return 0;
    }

    void set_MD5_CTX_buffer(char * md5Buf) {
        strncpy((char *)$self->buffer, md5Buf, 64);
    }
    
    char * get_MD5_CTX_buffer() {
        return (char*) $self->buffer;
    }
    
}

/*****************************************************************************/

int chksumLocFile (char *fileName, char *chksumStr, int use_sha256);

/*****************************************************************************/

%inline %{

PyObject * MD5Digest(char * md5Buf) {
    MD5_CTX context;
    unsigned char * digest = (unsigned char *) malloc(sizeof(unsigned char) * (RESPONSE_LEN+2));
    
    MD5Init(&context);
    MD5Update(&context, (unsigned char*) md5Buf, CHALLENGE_LEN+MAX_PASSWORD_LEN);
    MD5Final(digest, &context);
    
    return Py_BuildValue("s", (char *) digest);
}
%}

/*****************************************************************************/

int md5ToStr (unsigned char *digest, char *chksumStr);

/*****************************************************************************/

int rcChksumLocFile (char *fileName, char *chksumFlag, keyValPair_t *condInput, int use_sha256);

/*****************************************************************************/
