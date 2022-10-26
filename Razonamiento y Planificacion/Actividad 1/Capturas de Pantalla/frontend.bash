#!/bin/bash

#  frontend.bash

#  This file is part of Planner frontend

#  Copyright (C) 2022, Edgar Uriel Domínguez Espinoza

#  Planner frontend is free  software; you can redistribute it and/or modify  it under the terms
#  of  the GNU  General Public  License as  published by  the Free  Software Foundation;  either
#  version 2 of the License, or (at your option) any later version.

#  Planner frontend is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
#  without even  the implied warranty  of MERCHANTABILITY or  FITNESS FOR A  PARTICULAR PURPOSE.
#  See the GNU General Public License for more details.

#  You  should have  received  a copy  of  the GNU  General Public  License  along with  Planner
#  frontend;  if  not,  see  <http://www.gnu.org/licenses/>   or  write  to  the  Free  Software
#  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#  
help() {
    echo "Help message: Use full paths."
    echo "-P           Set Plan [output] file"
    echo "-c           Set costbound, only if planner need it"
    echo "-d           Set domain file, default domain.pddl"
    echo "-i           Set image file, default singularity.img"
    echo "-m           Set memory available for Singularity un bytes, default 12582912 (12GB)"
    echo "-p           Set problem file, default problem.pddl"
    echo "-r           Set runtime directory, default ."
    echo "-s           Set Singularity file script, default Singularity"
    echo "-t           Set max execution time in seconds, default 7200 (2hr)"
    exit 0
}
# BEGIN: default variables
RUNDIR=`pwd`
DOMAIN="$RUNDIR/domain.pddl"
PROBLEM="$RUNDIR/problem.pddl"
#  FIXME: This variable is not working
PLANFILE="$RUNDIR/sas_plan"
COSTBOUND=42 # only in cost-bounded track
SINGULARITY_FILE="$RUNDIR/Singularity"
SINGULARITY_IMAGE="$RUNDIR/singularity.img"
TIME=7200 # Two hours
MEMORY=12582912 # 12GB

# END: default variables
while getopts :P:c:d:i:m:p:r:s:t: option
do
    case "${option}"
    in
	P) PLANFILE=${OPTARG} ;;
	c) COSTBOUND=${OPTARG} ;;
	d) DOMAIN=${OPTARG} ;;
	i) SINGULARITY_IMAGE=${OPTARG} ;;
	m) MEMORY=${OPTARG} ;;
	p) PROBLEM=${OPTARG} ;;
	r) RUNDIR=${OPTARG} ;;
	s) SINGULARITY_FILE=${OPTARG} ;;
	t) TIME=${OPTARG} ;;
	?) help ;;
    esac
done

#BEGIN: Validations
[ -d $RUNDIR ] && echo "$RUNDIR exists on your filesystem" ||  mkdir -p $RUNDIR
[ -f $DOMAIN ] && echo "$DOMAIN file exists" || { echo "$DOMAIN file doesn't exist"; exit 1; }
[ -f $PROBLEM ] && echo "$PROBLEM file exists" || { echo "$PROBLEM file doesn't exist"; exit 1; }
[ -f $SINGULARITY_FILE ] && echo "$SINGULARITY_FILE file exists" || { echo "$SINGULARITY_FILE file doesn't exist"; exit 1; }
# END: Validations

echo "Building Sigularity image..."
[ -f $SINGULARITY_IMAGE ] && rm $SINGULARITY_IMAGE
echo "You must provide sudo credentials"
sudo singularity build $SINGULARITY_IMAGE $SINGULARITY_FILE 1>$SINGULARITY_FILE-stdout.log 2>$SINGULARITY_FILE-stderr.log
echo "Setting memory and time limits to $MEMORY bytes and $TIME seconds"
ulimit -t $TIME
ulimit -v $MEMORY
echo "Executing the planner..."
singularity run -C -H $RUNDIR $SINGULARITY_IMAGE $DOMAIN $PROBLEM $PLANFILE $COSTBOUND 1>>$SINGULARITY_FILE-stdout.log 2>>$SINGULARITY_FILE-stderr.log
echo "Done. Please check $SINGULARITY_FILE-stdout.log and $SINGULARITY_FILE-stderr.log for details."
exit 0
