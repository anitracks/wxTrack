#!/bin/bash
#
# just saving how generateDS.py is called
#
# Seth McNeill
# 2013 October 18

# requires that the generateDS.py package be installed first.

# collect the needed files from the internet
wget "http://graphical.weather.gov/xml/DWMLgen/schema/DWML.xsd"
wget "http://www.nws.noaa.gov/view/current_observation.xsd"

generateDS.py -f \
  -o ForeWx_api.py \
  -s ForeWx_proc.py \
  --super=ForeWx_api \
  --member-specs=list \
  DWML.xsd


generateDS.py -f \
  -o curWx_api.py \
  -s curWx_proc.py \
  --super=curWx_api \
  --member-specs=list \
  current_observation.xsd
