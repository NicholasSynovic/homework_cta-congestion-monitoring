#! /bin/bash

# Source the optparse.bash file
source optparse.bash

# Define options
optparse.define short=c long=cluster-uri desc="MongoDB cluster URI" variable=mdb_uri
optparse.define short=p long=password desc="MongoDB password" variable=mdb_password
optparse.define short=u long=username desc="MongoDB username" variable=mdb_username

# Source the output file
source $( optparse.build )

if [ "$mdb_username" == "" ]; then
	echo "ERROR: Please provide a MongoDB username"
	exit 1
fi

if [ "$mdb_password" == "" ]; then
	echo "ERROR: Please provide a MongoDB account password"
	exit 1
fi

if [ "$mdb_uri" == "" ]; then
	echo "ERROR: Please provide a MongoDB cluster uri"
	exit 1
fi
