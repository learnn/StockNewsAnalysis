#!/bin/bash
#CONVERT ALL CSV TO JSON
for entry in "dataset"/*
do
    /usr/bin/node s2_helper.js "$entry"
done
