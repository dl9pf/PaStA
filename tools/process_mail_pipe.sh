#!/bin/bash

# Copyright (c) OTH Regensburg, 2017-2018
#
# Author:
#   Ralf Ramsauer <ralf.ramsauer@othr.de>
#
# This work is licensed under the terms of the GNU GPL, version 2.  See
# the COPYING file in the top-level directory.

LISTNAME=$1
BASEDIR=$2
TMP=$(mktemp)

cat /dev/stdin > $TMP
./process_mail.sh $LISTNAME $BASEDIR $TMP
RET=$?
rm $TMP
exit $RET
