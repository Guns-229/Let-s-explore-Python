#!/bin/bash
find . -type d | while read N
do
     (
           cd "$N"
           if test "$?" = "0"
           then
               for file in *; do mv "$file" ${file// /%20}; done
           fi
     )
done
