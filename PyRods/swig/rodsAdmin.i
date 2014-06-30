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
   char *arg0;
   char *arg1;
   char *arg2;
   char *arg3;
   char *arg4;
   char *arg5;
   char *arg6;
   char *arg7;
   char *arg8;
   char *arg9;
} generalAdminInp_t;

%extend generalAdminInp_t {

    ~generalAdminInp_t() {
        if ($self != NULL) {
            free($self->arg0);
            free($self->arg1);
            free($self->arg2);
            free($self->arg3);
            free($self->arg4);
            free($self->arg5);
            free($self->arg6);
            free($self->arg7);
            free($self->arg8);
            free($self->arg9);
            free($self);
        }
    }

};

typedef struct {
   char *arg0;
   char *arg1;
   char *arg2;
   char *arg3;
   char *arg4;
   char *arg5;
   char *arg6;
   char *arg7;
   char *arg8;
   char *arg9;
} userAdminInp_t;

%extend userAdminInp_t {

    ~userAdminInp_t() {
        if ($self != NULL) {
            free($self->arg0);
            free($self->arg1);
            free($self->arg2);
            free($self->arg3);
            free($self->arg4);
            free($self->arg5);
            free($self->arg6);
            free($self->arg7);
            free($self->arg8);
            free($self->arg9);
            free($self);
        }
    }

};

/*****************************************************************************/

int rcGeneralAdmin (rcComm_t *conn, generalAdminInp_t *generalAdminInp);

/*****************************************************************************/

int rcUserAdmin (rcComm_t *conn, userAdminInp_t *userAdminInp);

/*****************************************************************************/
