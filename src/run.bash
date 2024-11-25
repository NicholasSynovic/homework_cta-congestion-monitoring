#!/bin/bash

# Source the optparse.bash file -----------------------------------------------
source optparse.bash
# Define options
optparse.define short=k long=key desc="CTA API Key" variable=key
optparse.define short=j long=json-dir desc="Directory to write JSON files" variable=jsonDir
optparse.define short=u long=username desc="MongoDB username" variable=username
optparse.define short=p long=password desc="MongoDB password" variable=password
optparse.define short=c long=cluster-uri desc="MongoDB cluster URI" variable=uri
# Source the output file ------------------------------------------------------
source $( optparse.build )

if [ "$key" == "" ]; then
    echo "Please provide a key"
    exit 1
fi

if [ "$jsonDir" == "" ]; then
    echo "Please provide a JSON directory"
    exit 1
fi

if [ "$username" == "" ]; then
    echo "Please provide a MongoDB username"
    exit 1
fi

if [ "$password" == "" ]; then
    echo "Please provide a MongoDB password"
    exit 1
fi

if [ "$uri" == "" ]; then
    echo "Please provide a MongoDB cluser URI"
    exit 1
fi

./cta2json/env/bin/python3.10 ./cta2json/main.py \
    --key $key \
    --output-dir $jsonDir

./json2MongoDB/env/bin/python3.10 ./json2MongoDB/main.py \
    --input-dir $jsonDir \
    --username $username \
    --password $password \
    --cluster-uri $uri

tar -czvf json_files.$(date +%s).tar.gz $jsonDir/*.json

rm $jsonDir/*.json
