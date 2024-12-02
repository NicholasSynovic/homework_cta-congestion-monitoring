#!/bin/bash

while :
do
    ./ingest_CTAAlerts -o cta-alerts.$(date +%s).json -l .
    sleep 5m
done
